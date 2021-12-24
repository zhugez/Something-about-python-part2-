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
userList = []

user = Person(name='Nguyễn Văn A ', email='DASAS@gmail.com',picture='https://localhost:5000/static/images/avatar.png')

user2 = Person(name='Nguyễn Văn B ', email='DASAS@gmail.com',picture='https://localhost:5000/static/images/avatar.png')

user3 = Person(name='Nguyễn Văn C ', email='DASAS@gmail.com',picture='https://localhost:5000/static/images/avatar.png')

user4 = Person(name='Lý Ngọc Vũ ', email='DASAS@gmail.com',picture='https://localhost:5000/static/images/avatar.png')
userList.append(user)
userList.append(user2)
userList.append(user3)
userList.append(user4)
with session:
    for user in userList:
        session.add(user)
    data= session.query(Person).all()
    session.delete(data)
    users = session.query(Person).all()
for user in users:
    print(f"USER ID: {user.id}, Name: {user.name}" if user.name != null else "NULL")
# session.commit()
# session.close()
