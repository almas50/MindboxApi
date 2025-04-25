from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, schemas, services
from .database import engine, Base, SessionLocal
from .seed import seed_db

Base.metadata.create_all(bind=engine)
seed_db(SessionLocal())
app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/products", response_model=list[schemas.ProductOut])
def products(db: Session = Depends(get_db)):
    return services.get_all_products(db)


@app.get("/categories", response_model=list[schemas.CategoryWithProducts])
def categories(db: Session = Depends(get_db)):
    return services.get_all_categories(db)


@app.get("/pairs", response_model=list[schemas.ProductCategoryPair])
def pairs(db: Session = Depends(get_db)):
    return services.get_all_pairs(db)
