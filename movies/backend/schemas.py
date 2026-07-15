from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class RecommendReq(BaseModel):
    movie_id: int
    movie_title: str