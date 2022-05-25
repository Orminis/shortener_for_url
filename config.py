# pydantic is a library that uses type annotation to validate data and manage settings.
from pydantic import BaseSettings


"""The BaseSettings class comes in handy to define environment variables in your application. 
You only have to define the variables that you want to use, and pydantic takes care of the rest. 
In other words, pydantic will automatically assume those default values if it doesn't find the corresponding 
environment variables."""
class Settings(BaseSettings):
    env_name: str = "Local"                     # Name of your current environment
    base_url: str = "http://localhost:8000"     # Domain of your app
    db_url: str = "sqlite:///./shortener.db"    # Address of your database


def get_settings():
    settings = Settings()
    print(f"Loading settings for: {settings.env_name}")
    return settings

