from fastapi import FastAPI
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .routers import user, auth, admin
from .database import engine
from .config import settings
from . import models, util

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

while True: 
        try:
                conn = psycopg2.connect(host = f'{settings.db_host}',
                                database = f'{settings.db_name}', 
                                user=f'{settings.db_user}', 
                                password=f'{settings.db_pass}',
                                cursor_factory=RealDictCursor
                                )
                cursor = conn.cursor()
                print("Database connection was successful!")
                break
        except Exception as error:
                print("Connecting to database failed.")
                print(f"Error was {error}")
                time.sleep(2)

app.include_router(user.router)
app.include_router(auth.router)
app.include_router(admin.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}

