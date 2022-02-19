from datetime import datetime

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from utils.model_base import Base


class Users(Base):
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(64), unique=True, index=True)
    name = Column(String(64), index=True)
    password = Column(String(128))
    created_at = Column(DateTime(), default=datetime.utcnow)
