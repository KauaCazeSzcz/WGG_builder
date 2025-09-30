""""""

from sqlalchemy import Column, Table, Integer, Boolean, Text, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base = declarative_base()

class User(Base):
    """Users table"""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    email = Column(String(100), unique=True, nullable=True, index=True)
    password_hash = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=func.now())
    last_login = Column(DateTime, nullable=True)

    def __repr__(self):
        return f"<User {self.username} ({self.email})>"
    
class SystemLog(Base):
    """Logs system actions"""

    __tablename__ = "system_log"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=True)
    action = Column(String(50), nullable=False)
    details = Column(Text, nullable=True)
    created_at = Column(DateTime, default=func.now())