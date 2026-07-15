
# 🎬 Movie Recommendation System

A Movie Recommendation System built using **Machine Learning (NLP)**, **FastAPI**, **Streamlit**, and **PostgreSQL**. The application recommends movies similar to the user's selected movie using **Bag of Words**, **CountVectorizer**, and **TF-IDF**.

---

## 🚀 Features

* User Signup and Login
* JWT Authentication
* Movie Recommendation System
* Streamlit User Interface
* FastAPI REST APIs
* PostgreSQL Database
* Recommendation History

---

## 🛠️ Tech Stack

* **Frontend:** Streamlit
* **Backend:** FastAPI
* **Database:** PostgreSQL
* **Machine Learning:** Scikit-learn (CountVectorizer & Cosine Similarity)
* **Language:** Python

---

## 📂 Project Structure

```text
PYTHON/
├── backend/
│   ├── main.py
│   ├── auth.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── requirements.txt
│
├── frontend/
│   ├── app.py
│   └── pages/
│       ├── home.py
│       ├── login.py
│       └── signup.py
│
├── model/
│   ├── movie_dict.pkl
│   ├── similarity.pkl
│   ├── tmdb_5000_movies.csv
│   └── tmdb_5000_credits.csv
│
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

1. Install the required packages:

```bash
pip install -r backend/requirements.txt
```

2. Start the FastAPI server:

```bash
cd backend
uvicorn main:app --reload
```

3. Run the Streamlit application:

```bash
cd frontend
streamlit run app.py
```

---

## 📡 API Endpoints

| Method | Endpoint     | Description               |
| ------ | ------------ | ------------------------- |
| POST   | `/signup`    | Register a new user       |
| POST   | `/login`     | User login                |
| GET    | `/movies`    | Get movie list            |
| POST   | `/recommend` | Get movie recommendations |

---

## 🤖 Machine Learning Workflow

TMDB Dataset → Data Preprocessing → Feature Engineering → CountVectorizer → Cosine Similarity → Movie Recommendation

---

## 📌 Future Enhancements

* Movie Posters
* Watchlist
* Favorites
* Search Movies
* User Profile
* Cloud Deployment

---

## 👨‍💻 Author

**Arvind Yadav**

**Tech Stack:** Python • FastAPI • Streamlit • PostgreSQL • Machine Learning • SQL


