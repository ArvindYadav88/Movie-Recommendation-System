from sqlalchemy import Column, Integer, String, TIMESTAMP
from database import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

class Recommendation(Base):
    __tablename__ = "recommendations"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    username = Column(String)
    input_movie_id = Column(Integer)
    input_movie = Column(String)
    recommended_movie_id = Column(Integer)
    recommended_movie = Column(String)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)