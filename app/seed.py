from .models import Product, Category
from sqlalchemy.orm import Session


def seed_db(db: Session):
    if db.query(Product).count() > 0:
        return
    p1 = Product(name="Laptop")
    p2 = Product(name="Phone")
    p3 = Product(name="Keyboard")
    c1 = Category(name="Electronics")
    c2 = Category(name="Gadgets")
    c3 = Category(name="Fridges")
    p1.categories.append(c1)
    p2.categories.append(c1)
    p2.categories.append(c2)
    db.add_all([p1, p2, p3, c1, c2, c3])
    db.commit()
