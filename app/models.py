from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

product_category = Table(
    'product_category', Base.metadata,
    Column('product_id', ForeignKey('products.id')),
    Column('category_id', ForeignKey('categories.id'))
)


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, index=True)
    categories = relationship("Category", secondary=product_category, back_populates="products")


class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, index=True)
    products = relationship("Product", secondary=product_category, back_populates="categories")
