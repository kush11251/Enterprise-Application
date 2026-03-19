from models import User
from config import DB_HOST, DB_PORT, DB_USERNAME, DB_PASSWORD
import psycopg2
class UserRepository:
    def __init__(self, db_host: str, db_port: int, db_username: str, db_password: str):
        self.db_host = db_host
        self.db_port = db_port
        self.db_username = db_username
        self.db_password = db_password
    def read_users(self):
        # Connect to database and read users