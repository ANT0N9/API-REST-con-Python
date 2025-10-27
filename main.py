from fastapi import FastAPI

from config.db import Base, engine
from models.user import User
from routers import user

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}