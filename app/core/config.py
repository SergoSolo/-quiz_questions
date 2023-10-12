import logging

import aiohttp
from pydantic import BaseSettings


class Settings(BaseSettings):
    """Настройки проекта."""

    APP_TITLE: str
    APP_DESCRIPTION: str
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: str

    @property
    def database_url(self):
        return (
            f"postgresql+asyncpg://"
            f"{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )

    class Config:
        env_file = ".env"


settings = Settings()
logger = logging.getLogger(__name__)


def configure_logging():
    logging.basicConfig(
        datefmt="%d.%m.%Y %H:%M:%S",
        format="%(asctime)s, %(levelname)s, %(message)s",
        level=logging.INFO,
    )


async def get_http_client_session():
    async with aiohttp.ClientSession() as session:
        yield session
