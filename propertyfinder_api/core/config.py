from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MONGODB_URI: str
    JWT_SECRET: str
    JWT_ALGORITHM: str
    JWT_ACCESS_EXPIRE_MINUTES: int

    class Config:
        env_file = ".env.local"

settings = Settings()
