from fastapi import APIRouter, Depends
from services import product_service
router = APIRouter()
@router.get('/products')
def read_products(product_service: ProductService = Depends()):
    return product_service.read_products()