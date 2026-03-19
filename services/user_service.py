from models import User
from repositories import user_repository
class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
    def read_users(self):
        return self.user_repository.read_users()