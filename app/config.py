from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str

    model_config = {  # Use model_config for configuration settings in Pydantic v2
        "env_file": ".env"
    }

settings = Settings()
print(settings.DATABASE_URL)