from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    app_name: str = "MUSIC_BOX"
    env: str = "dev"
    api_prefix: str = "/api/v1"


settings = Settings()
