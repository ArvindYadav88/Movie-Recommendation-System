from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
import models, schemas, auth,database

import pickle
import pandas as pd

models.Base.metadata.create_all(bind=database.engine)
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Model load - path:The model folder is located one level above the backend folder.
movies = pd.DataFrame()
similarity = []
try:
    movies_dict = pickle.load(open("../model/movie_dict.pkl", 'rb'))
    movies = pd.DataFrame(movies_dict)
    similarity = pickle.load(open("../model/similarity.pkl", 'rb'))
    print(f"Model loaded. Total movies: {len(movies)}")
except Exception as e:
    print("Model load error:", e)

@app.post("/signup")
def signup(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    try:
        db_user = db.query(models.User).filter(models.User.username == user.username).first()
        if db_user:
            raise HTTPException(status_code=400, detail="Username already exists")
        
        db_email = db.query(models.User).filter(models.User.email == user.email).first()
        if db_email:
            raise HTTPException(status_code=400, detail="Email already exists")
        
        hashed_pw = auth.get_password_hash(user.password)
        new_user = models.User(username=user.username, email=user.email, hashed_password=hashed_pw)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return {"msg": "User created successfully"}
        
    except Exception as e:
        print("Signup Error:", str(e))  # Terminal me exact error dikhega
        raise HTTPException(status_code=500, detail=f"Internal error: {str(e)}")
@app.get('/')
def home():
    return {'msg:''Your Authentication App'}

@app.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(database.get_db)):
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if not db_user or not auth.verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    
    token = auth.create_access_token(data={"sub": db_user.username})
    return {"access_token": token, "token_type": "bearer"}

def recommend(movie_title):
    try:
        movie_index = movies[movies['title'] == movie_title].index[0]
        distances = similarity[movie_index]
        movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
        recommend_movies = []
        for i in movies_list:
            movie_row = movies.iloc[i[0]]
            recommend_movies.append({
                "id": int(movie_row.movie_id),
                "title": movie_row.title
            })
        return recommend_movies
    except Exception as e:
        print("Recommend error:", e)
        return []

@app.get("/movies")
def get_movies(current_user: models.User = Depends(auth.get_current_user)):
    return movies[['movie_id', 'title']].to_dict('records')

@app.post("/recommend")
def recommend_api(req: schemas.RecommendReq, current_user: models.User = Depends(auth.get_current_user), db: Session = Depends(database.get_db)):
    recs = recommend(req.movie_title)
    for m in recs:
        new_rec = models.Recommendation(
            user_id=current_user.id,
            username=current_user.username,
            input_movie_id=req.movie_id,
            input_movie=req.movie_title,
            recommended_movie_id=m["id"],
            recommended_movie=m["title"]
        )
        db.add(new_rec)
    db.commit()
    return {"recommendations": recs}