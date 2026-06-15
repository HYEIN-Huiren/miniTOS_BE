import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    # DB
    DB_USER: str = os.getenv("DB_USER")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD")
    DB_HOST: str = os.getenv("DB_HOST")
    DB_PORT: str = os.getenv("DB_PORT")
    DB_NAME: str = os.getenv("DB_NAME")
    
    FE_HOST: str = os.getenv("FE_HOST")
    FE_PORT: str = os.getenv("FE_PORT")
    
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM: str = os.getenv("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES: str = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
    

    @property
    def DATABASE_URL(self) -> str:
        return (
            f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )
    
    @property
    def FE_URL(self) -> str:
        return (
            f"http://{self.FE_HOST}:{self.FE_PORT}"
        )


settings = Settings()