from pydantic import BaseModel
from typing import List, Optional


class CategoryOut(BaseModel):
    id: int
    name: str

    class ConfigDict:
        from_attributes = True


class ProductOut(BaseModel):
    id: int
    name: str
    categories: List[CategoryOut] = []

    class ConfigDict:
        from_attributes = True


class CategoryWithProducts(BaseModel):
    id: int
    name: str
    products: List[ProductOut] = []

    class ConfigDict:
        from_attributes = True


class ProductCategoryPair(BaseModel):
    product_name: Optional[str] = None
    category_name: Optional[str] = None
