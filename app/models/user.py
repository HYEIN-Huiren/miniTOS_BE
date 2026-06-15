from sqlalchemy import Column, String, Integer

from app.core.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    
    role = Column(String, nullable=False, default="VIEWER")