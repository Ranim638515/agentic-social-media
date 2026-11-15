from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_url: str = "postgresql+psycopg://postgres:postgres@localhost:5432/social_ai"
    llm_provider: str = "openai"
    llm_api_key: str = ""
    secret_key: str = "change_me"

    model_config = SettingsConfigDict(env_file="../.env", extra="ignore")


settings = Settings()
