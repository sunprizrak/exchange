from pathlib import Path
from os import getenv
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).parent.parent


class Settings(BaseSettings):
    db_driver: str
    db_user: str
    db_password: str
    db_host: str
    db_port: int
    db_name: str
    db_echo: bool = False

    @property
    def db_url(self) -> str:
        return f"{self.db_driver}://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"


settings = Settings()