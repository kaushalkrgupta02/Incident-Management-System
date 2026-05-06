from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    POSTGRES_URL: str = "postgresql+asyncpg://user123:pass123@postgres:5432/ims_db_pg"
    MONGODB_URL: str = "mongodb://user123:pass123@mongodb:27017/ims_db_mongo?authSource=admin"
    REDIS_URL: str = "redis://redis:6379"
    APP_NAME: str = "IMS - Incident Management System"
    VERSION: str = "1.0.0"

    class Config:
        env_file = ".env"

settings = Settings()
