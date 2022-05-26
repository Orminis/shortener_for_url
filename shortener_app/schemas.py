from pydantic import BaseModel


class URLBase(BaseModel):
    """target_url to store the URL that your shortened URL forwards to."""
    target_url: str


class URL(URLBase):
    is_active: bool
    clicks: int

    class Config:
        """you tell pydantic with orm_mode = True to work with a database model.
        ORM stands for Object-Relational Mapping, and it provides the convenience
        of interacting with your database using an object-oriented approach."""
        orm_mode = True


class URLInfo(URL):
    """ This enhances URL by requiring two additional strings, url and admin_url.
    You could also add the two strings url and admin_url to URL.
    But by adding url and admin_url to the URLInfo subclass,
    you can use the data in your API without storing it in your database."""
    url: str
    admin_url: str
