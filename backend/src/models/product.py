from datetime import datetime

from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    DateTime,
    Boolean,
    Text,
    Enum,
    DECIMAL
)

from models.attribute import AttributeModel
from models.category import CategoryModel
from utils.model_base import Base


class ProductModel(Base):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True, index=True)
    category_id = Column(Integer, ForeignKey(CategoryModel.id), primary_key=True, nullable=False)
    name = Column(String(255), nullable=False)
    sku = Column(String(10), nullable=False)
    description = Column(Text, nullable=False)
    active = Column(Boolean, default=False)
    created_at = Column(DateTime(), default=datetime.utcnow)
    updated_at = Column(DateTime(), default=datetime.utcnow)


class ProductMetaModel(Base):
    __tablename__ = 'product_meta'

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey(ProductModel.id), primary_key=True, nullable=False)
    quantity = Column(Integer, nullable=False)
    original_price = Column(DECIMAL(10, 2), nullable=False)
    discount_price = Column(DECIMAL(10, 2), nullable=True)
    tax_percentage = Column(DECIMAL(10, 2), nullable=True)
    created_at = Column(DateTime(), default=datetime.utcnow)
    updated_at = Column(DateTime(), default=datetime.utcnow)


class ProductImgModel(Base):
    __tablename__ = 'product_img'

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey(ProductModel.id), primary_key=True, nullable=False)
    img = Column(String(255), nullable=False)
    thumb_img = Column(String(255), nullable=False)
    alt_img_tag = Column(String(255), nullable=False)
    file_type = Column(Enum('Image', 'Video'), default="Image")
    sort_order = Column(Integer)


class ProductAttributeModel(Base):
    __tablename__ = 'product_attribute'

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey(ProductModel.id), primary_key=True, nullable=False)
    attribute_id = Column(Integer, ForeignKey(AttributeModel.id), primary_key=True, nullable=False)


class ProductTagModel(Base):
    __tablename__ = 'product_tag'

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey(ProductModel.id), primary_key=True, nullable=False)
    seo_title = Column(String(255))
    seo_desc = Column(Text)
    seo_keywords = Column(String(255))
    h1_tag = Column(String(255))
    h2_tag = Column(String(255))
    h3_tag = Column(String(255))
    alt_img_tag = Column(String(255))
