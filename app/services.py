from sqlalchemy.orm import Session
from . import models, schemas


def get_all_products(db: Session):
    return db.query(models.Product).all()


def get_all_categories(db: Session):
    return db.query(models.Category).all()


def get_all_pairs(db: Session):
    pairs = []
    products = db.query(models.Product).all()
    for product in products:
        for cat in product.categories:
            pairs.append({"product_name": product.name, "category_name": cat.name})
        if not product.categories:
            pairs.append({"product_name": product.name, "category_name": None})
    categories = db.query(models.Category).all()
    for cat in categories:
        if not cat.products:
            pairs.append({"product_name": None, "category_name": cat.name})
    return pairs
