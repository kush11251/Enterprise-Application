from fastapi import APIRouter, Depends
from services import user_service
router = APIRouter()
@router.get('/users')
def read_users(user_service: UserService = Depends()):
    return user_service.read_users()