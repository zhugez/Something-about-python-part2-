from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    email = Column(String(50))
    picture = Column(String(50))

    def __init__(self, name, email, picture):
        self.name = name
        self.email = email
        self.picture = picture


engine = create_engine("sqlite:///users.db", echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
user = Person(name='Ly Ngoc VU', email='john@example.com',
              picture='http://www.example.com/')
session.add(user)
session.commit()
session.delete(user)
users = session.query(Person).all()
for user in users:
    print(user.name)
session.close()
