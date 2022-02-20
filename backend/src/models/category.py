from datetime import datetime

from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    DateTime,
    Boolean,
    Text
)

from utils.model_base import Base


class CategoryModel(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, index=True)
    parent_id = Column(Integer, ForeignKey("category.id"), primary_key=True, nullable=False)
    name = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    image = Column(String(255))
    sort_order = Column(Integer)
    active = Column(Boolean, default=False)
    created_at = Column(DateTime(), default=datetime.utcnow)
    updated_at = Column(DateTime(), default=datetime.utcnow)


class CategoryTagModel(Base):
    __tablename__ = 'category_tag'

    id = Column(Integer, primary_key=True, index=True)
    category_id = Column(Integer, ForeignKey(CategoryModel.id), primary_key=True, nullable=False)
    seo_title = Column(String(255))
    seo_desc = Column(Text)
    seo_keywords = Column(String(255))
    h1_tag = Column(String(255))
    h2_tag = Column(String(255))
    h3_tag = Column(String(255))
    alt_img_tag = Column(String(255))
