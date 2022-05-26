from fastapi import FastAPI, HTTPException
import validators
from . import schemas

'''The app variable is the main point of interaction to create the API.'''
app = FastAPI()


def raise_bad_request(message):
    raise HTTPException(status_code=400, detail=message)


@app.get("/")       # A path operation decorator to associate your root path with read_root() by registering it in FastAPI.
def read_root():    # Now, FastAPI listens to the root path and delegates all incoming GET requests to your read_root() function.'''
    return "Welcome to the Url shortener API"


@app.post('/url')
def create_url(url: schemas.URL):
    if not validators.url(url.target_url):
        raise_bad_request(message="Provided URL is not valid")
    return f"TODO: Create database entry for: {url.target_url}"



