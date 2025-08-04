from sqlalchemy import Column, Integer, String, Date, TIMESTAMP,text
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class LibraryORM(Base):
    __tablename__ = 'libraries'
    library_id = Column(Integer, primary_key=True)
    library_name = Column(String(100),nullable=False)
    campus_location = Column(String(100))
    contact_email = Column(String(100),unique=True)
    phone_number = Column(String(20),unique=True)
    created_at = Column(TIMESTAMP,nullable=False,server_default=text('CURRENT_TIMESTAMP'))
    last_update = Column(TIMESTAMP, nullable=False, server_default=text(
        'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))

class Books(Base):
    __tablename__ = 'books'
    # book_id = Column(Integer, primary_key=True)
    title = Column(String(200),primary_key=True)

    # total_copies = Column(Integer)
    # available_copies = Column(Integer)
    isbn = Column(String(20), unique=True, nullable=True)
    published_date = Column(Date)
    created_at = Column(TIMESTAMP,nullable=False,server_default=text('CURRENT_TIMESTAMP'))
    last_update = Column(TIMESTAMP, nullable=False, server_default=text(
        'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))

class MemberORM(Base):
    __tablename__ = 'members'
    member_id = Column(Integer, primary_key=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    email = Column(String(100),unique=True)
    phone_number = Column(String(20),unique=True)
    member_type = Column(String(50))
    registration_date = Column(Date)
    created_at = Column(TIMESTAMP,nullable=False,server_default=text('CURRENT_TIMESTAMP'))
    last_update = Column(TIMESTAMP, nullable=False, server_default=text(
        'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))

class AuthorORM(Base):
    __tablename__ = 'authors'
    author_id = Column(Integer, primary_key=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    birth_date = Column(Date)
    nationality = Column(String(100))
    biography = Column(String(1000))
    created_at = Column(TIMESTAMP,nullable=False,server_default=text('CURRENT_TIMESTAMP'))
    last_update = Column(TIMESTAMP, nullable=False, server_default=text(
        'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))

