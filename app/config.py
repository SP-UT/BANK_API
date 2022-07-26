from pydantic import BaseSettings

class Settings(BaseSettings):
    db_user: str
    db_pass: str
    db_host: str
    db_name: str

    class Config:
        env_file = ".env"
        case_sensitive = True
        fields = {
            "db_user": {
                "env": "DB_USER"
            },
            "db_pass": {
                "env": "DB_PASS"
            },
            "db_host": {
                "env": "DB_HOST"
            },
            "db_name": {
                "env": "DB_NAME"
            }
        }

settings = Settings()