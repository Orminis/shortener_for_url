import secrets

import validators
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from . import schemas, models

'''The app variable is the main point of interaction to create the API.'''
app = FastAPI()
models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def raise_bad_request(message):
    raise HTTPException(status_code=400, detail=message)

# A path operation decorator to associate your root path with read_root() by registering it in FastAPI.
# Now, FastAPI listens to the root path and delegates all incoming GET requests to your read_root() function.'''
@app.get("/")
def read_root():
    return "Welcome to the Url shortener API"


@app.post('/url', response_model=schemas.URLInfo)
def create_url(url: schemas.URLBase, db: Session = Depends(get_db)):
    if not validators.url(url.target_url):
        raise_bad_request(message="Provided URL is not valid")

    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = "".join(secrets.choice(chars) for _ in range(5))
    secret_key = "".join(secrets.choice(chars) for _ in range(8))
    db_url = models.URL(
        target_url=url.target_url, key=key, secret_key=secret_key
    )
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    db_url.url = key
    db_url.admin_url = secret_key

    return db_url
