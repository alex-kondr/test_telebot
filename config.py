from pydantic import BaseSettings


class Settings(BaseSettings):
    api_id_telegram: int = 123
    api_hash_telegram: str = "a1b2c3"
    token_telegram: str = "a1b2c3"
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        

settings = Settings()
