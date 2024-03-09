from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    BOT_TOKEN: str
    CHATS: list
    HOURS_TIMEOUT: int
    MINUTES_TIMEOUT: int
    SECONDS_TIMEOUT: int
    SPAM_TEXT: str

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()

