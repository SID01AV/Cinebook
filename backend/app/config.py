from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "CineBook API"
    environment: str = "local"
    debug: bool = False

    database_url: str = (
        "postgresql+asyncpg://cinemabook:"
        "cinemabook@postgres:5432/cinemabook"
    )

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:  #Could have been like settings = Settings()-> assigning it to a variable, but through function calling we can use it easily for testing, Caching using lru_cache and use in dependency injection
    return Settings()