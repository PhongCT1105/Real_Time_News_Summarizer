from pydantic_settings import BaseSettings  # correct in v2

class Settings(BaseSettings):
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_DB: str = "news"
    POSTGRES_USER: str = "news"
    POSTGRES_PASSWORD: str = "news"
    
    class Config:
        env_file = ".env"

settings = Settings()