from daos.product_dao import ProductDAO
from models.product import Product

class ProductController:
    def __init__(self):
        self.dao = ProductDAO()

    def list_products(self) -> list[Product]:
        return self.dao.select_all()

    def add_product(self, name: str, brand: str, price: float) -> int:
        return self.dao.insert(Product(None, name, brand, price))

    def delete_product(self, product_id: int) -> None:
        self.dao.delete(product_id)