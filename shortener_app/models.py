"""While database.py contains information about your database connection,
the models.py file will describe the content of your database. To continue, create models.py:"""

from sqlalchemy import Boolean, Column, Integer, String

from .database import Base


class URL(Base):
    __tablename__ = 'urls'

    id = Column(Integer, primary_key=True)
    key = Column(String, unique=True, index=True)
    secret_key = Column(String, unique=True, index=True)
    target_url = Column(String, index=True)
    is_active = Column(Boolean, default=True)
    clicks = Column(Integer, default=0)


"""The code that you add to models.py looks similar to the code that you wrote in schemas.py. 
In schemas.py, you defined what data your API expected from the client and the server. 
In models.py, you declare how your data should be stored in the database.

You’re creating a database model named URL. The URL model is a subclass of Base, which you import.

It’s common to give your model a singular name and your database tables plural names. 
That’s why you name your model URL and provide the special variable __tablename__."""