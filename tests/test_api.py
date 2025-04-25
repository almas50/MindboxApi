from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_get_products():
    response = client.get("/products")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    for product in data:
        assert "name" in product
        assert "categories" in product

def test_get_categories():
    response = client.get("/categories")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    for category in data:
        assert "name" in category
        assert "products" in category

def test_get_product_category_pairs():
    response = client.get("/pairs")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    for pair in data:
        assert "product_name" in pair
        assert "category_name" in pair