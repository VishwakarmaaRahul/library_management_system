from sqlalchemy import Column, Integer, String, Date, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class LibraryORM(Base):
    __tablename__ = 'libraries'
    library_id = Column(Integer, primary_key=True)
    library_name = Column(String(100))
    campus_location = Column(String(100))
    contact_email = Column(String(100))
    phone_number = Column(String(20))

class BookORM(Base):
    __tablename__ = 'books'
    book_id = Column(Integer, primary_key=True)
    title = Column(String(200))
    publication_date = Column(Date)
    total_copies = Column(Integer)
    available_copies = Column(Integer)
    isbn = Column(String(20))

class MemberORM(Base):
    __tablename__ = 'members'
    member_id = Column(Integer, primary_key=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    email = Column(String(100))
    phone_number = Column(String(20))
    member_type = Column(String(50))
    registration_date = Column(Date)

class AuthorORM(Base):
    __tablename__ = 'authors'
    author_id = Column(Integer, primary_key=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    birth_date = Column(Date)
    nationality = Column(String(100))
    biography = Column(String(1000))
