from models import Product
from repositories import product_repository
class ProductService:
    def __init__(self, product_repository: ProductRepository):
        self.product_repository = product_repository
    def read_products(self):
        return self.product_repository.read_products()