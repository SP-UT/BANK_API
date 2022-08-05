from pydantic import BaseSettings

class Settings(BaseSettings):
    db_user: str
    db_pass: str
    db_host: str
    db_name: str
    secret_key: str
    algorithm: str
    access_token_expire_minutes: str


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
            },
            "secret_key": {
                "env": "SECRET_KEY"
            },
            "algorithm": {
                "env": "ALGORITHM"
            },
            "access_token_expire_minutes": {
                "env": "ACCESS_TOKEN_EXPIRE_MINUTES"
            }
        }

settings = Settings()