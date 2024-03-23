import os
from dotenv import load_dotenv
from attr import define, frozen, field

load_dotenv()

class DatabaseHelper():
    @staticmethod
    def get_host():
        return os.getenv("POSTGRES_HOST")
    @staticmethod
    def get_port():
        return os.getenv("POSTGRES_PORT")
    @staticmethod
    def get_username():
        return os.getenv("POSTGRES_USER")
    @staticmethod
    def get_password():
        return os.getenv("POSTGRES_PASSWORD")
    @staticmethod
    def get_database():
        return os.getenv("POSTGRES_DB")

@frozen
class Database:
    dialect: str = "postgresql"
    engine: str = "psycopg2"
    host: str = field(default=DatabaseHelper.get_host())
    port: int = field(default=DatabaseHelper.get_port())
    username: str = field(default=DatabaseHelper.get_username())
    password : str = field(default=DatabaseHelper.get_password())
    database: str = field(default=DatabaseHelper.get_database())
    echo: bool = True

@define
class Config:
    database: Database = Database()