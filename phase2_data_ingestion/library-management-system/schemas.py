from pydantic import BaseModel, EmailStr, field_validator,ValidationError
import phonenumbers
import logging
import re
import csv
from datetime import date , datetime
from sqlalchemy.exc import IntegrityError, OperationalError, ProgrammingError


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, MemberORM, BookORM, AuthorORM, LibraryORM

class Library(BaseModel):
    library_id : int
    library_name : str
    campus_location : str
    contact_email : EmailStr
    phone_number : str

    @field_validator('phone_number')
    def validate_phone_number(cls,v):
        try:
            parsed = phonenumbers.parse(v,"IN")
            if not phonenumbers.is_valid_number(parsed):
                raise ValueError ("Phone Number is not vallid")
            return phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.E164)
        except phonenumbers.NumberParseException:
            raise ValueError("Could not parse phone number")

class Book(BaseModel):
    """This is the book class and validating ISBN """
    book_id : int
    title : str
    publication_date : date
    total_copies : int
    available_copies : int
    isbn : str

    @field_validator('isbn')
    def isbn_validator(cls, v):
        isbn = v.replace('-', '').upper()
        if len(isbn) == 13 and isbn.isdigit():
            total = sum((int(x) * (1 if i % 2 == 0 else 3)) for i, x in enumerate(isbn))
            if total % 10 != 0:
                raise ValueError('Invalid ISBN-13 checksum')
            return isbn
        elif len(isbn) == 10 and re.match(r'^\d{9}[\dXx]$', isbn):
            total = sum((10 - i) * (10 if x.upper() == 'X' else int(x)) for i, x in enumerate(isbn))
            if total % 11 != 0:
                raise ValueError('Invalid ISBN-10 checksum')
            return isbn
        else:
            raise ValueError('ISBN must be 10 digits long')

class Members(BaseModel):
    member_id : int
    first_name : str
    last_name : str
    email : EmailStr
    phone_number : str
    member_type : str
    registration_date : date


    @field_validator('phone_number')
    def validate_phone_number(cls,v):
        try:
            parsed = phonenumbers.parse(v,"IN")
            if not phonenumbers.is_valid_number(parsed):
                raise ValueError ("Phone Number is not vallid")
            return phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.E164)
        except phonenumbers.NumberParseException:
            raise ValueError("Could not parse phone number")

    @field_validator('first_name','last_name')
    def normalize_name(cls,v):
        clean = ' '.join(v.strip().split())
        return clean.title()



class Authors(BaseModel):
    author_id : int
    first_name : str
    last_name : str
    birth_date : date
    nationality : str
    biography : str


    @field_validator('first_name', 'last_name')
    def normalize_authors_name(cls, v):
        clean = ' '.join(v.strip().split())
        return clean.title()

    @field_validator('birth_date')
    def validate_birth_date(cls, v):
        if v.year < 1800 or v > datetime.now().date():
            raise ValueError("Invalid birth date: must be between 1800 and today")
        return v

def load_and_validate_data(members_csv, books_csv, authors_csv, library_csv ):
    logging.basicConfig(
        filename='validation_errors.log',
        level=logging.ERROR,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    members, books, authors, libraries = [], [], [], []

    def load_csv(path):
        with open(path, newline='', encoding='utf-8') as f:
            return list(csv.DictReader(f))

    members_data = load_csv(members_csv)
    books_data = load_csv(books_csv)
    authors_data = load_csv(authors_csv)
    libraries_data = load_csv(library_csv)

    logging.info(f"Read {len(members_data)} rows from Members.csv")
    logging.info(f"Read {len(books_data)} rows from Books.csv")
    logging.info(f"Read {len(authors_data)} rows from Authors.csv")
    logging.info(f"Read {len(libraries_data)} rows from Libraries.csv")


    for row in load_csv(members_csv):
        try:
            row['member_id'] = int(row['member_id'])
            row['registration_date'] = date.fromisoformat(row['registration_date'])
            member = Members(**row)
            members.append(member)
        except ValidationError as e:
            logging.error(f"Member Validation Error: {row}\n{e}")

    for row in load_csv(books_csv):
        try:
            row['book_id'] = int(row['book_id'])
            row['total_copies'] = int(row['total_copies'])
            row['available_copies'] = int(row['available_copies'])
            row['publication_date'] = date.fromisoformat(row['publication_date'])
            book = Book(**row)
            books.append(book)
        except ValidationError as e:
            logging.error(f"Book Validation Error: {row}\n{e}")

    for row in load_csv(authors_csv):
        try:
            row['author_id'] = int(row['author_id'])
            row['birth_date'] = date.fromisoformat(row['birth_date'])
            author = Authors(**row)
            authors.append(author)
        except ValidationError as e:
            logging.error(f"Author Validation Error: {row}\n{e}")

    for row in load_csv(library_csv):
        try:
            row['library_id'] = int(row['library_id'].strip())
            library = Library(**row)
            libraries.append(library)
        except ValidationError as e:
            logging.error(f"Library Validation Error: {row}\n{e}")

    logging.info(f"Validated members: {len(members)} / {len(members_data)}")
    logging.info(f"Validated books: {len(books)} / {len(books_data)}")
    logging.info(f"Validated authors: {len(authors)} / {len(authors_data)}")
    logging.info(f"Validated libraries: {len(libraries)} / {len(libraries_data)}")

    return members, books, authors, libraries



DATABASE_URL = "mysql+pymysql://root:Rvsql%40123@localhost:3306/library_data_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

Base.metadata.create_all(engine)


def insert_data(members, books, authors, libraries, engine):
    SessionLocal = sessionmaker(bind=engine)
    session = SessionLocal()

    inserted = {"members": 0, "books": 0, "authors": 0, "libraries": 0}
    duplicates = {"members": 0, "books": 0, "authors": 0, "libraries": 0}
    errors = {"members": 0, "books": 0, "authors": 0, "libraries": 0}

    try:
        for m in members:
            try:
                session.add(MemberORM(**m.model_dump()))
                inserted["members"] += 1
            except IntegrityError:
                session.rollback()
                duplicates["members"] += 1
                logging.warning(f"Duplicate Member skipped: {m.member_id}")
            except Exception as e:
                session.rollback()
                errors["members"] += 1
                logging.error(f"Error inserting member {m.member_id}: {e}")

        for b in books:
            try:
                session.add(BookORM(**b.model_dump()))
                inserted["books"] += 1
            except IntegrityError:
                session.rollback()
                duplicates["books"] += 1
                logging.warning(f"Duplicate Book skipped: {b.book_id}")
            except Exception as e:
                session.rollback()
                errors["books"] += 1
                logging.error(f"Error inserting book {b.book_id}: {e}")

        for a in authors:
            try:
                session.add(AuthorORM(**a.model_dump()))
                inserted["authors"] += 1
            except IntegrityError:
                session.rollback()
                duplicates["authors"] += 1
                logging.warning(f"Duplicate Author skipped: {a.author_id}")
            except Exception as e:
                session.rollback()
                errors["authors"] += 1
                logging.error(f"Error inserting author {a.author_id}: {e}")

        for l in libraries:
            try:
                session.add(LibraryORM(**l.model_dump()))
                inserted["libraries"] += 1
            except IntegrityError:
                session.rollback()
                duplicates["libraries"] += 1
                logging.warning(f"Duplicate Library skipped: {l.library_id}")
            except Exception as e:
                session.rollback()
                errors["libraries"] += 1
                logging.error(f"Error inserting library {l.library_id}: {e}")

        session.commit()
        logging.info("Data successfully committed to the database.")

    except (OperationalError, ProgrammingError) as db_error:
        session.rollback()
        logging.critical(f"Critical database error: {db_error}")
    except Exception as e:
        session.rollback()
        logging.error(f"Unexpected error during DB insert: {e}")
    finally:
        session.close()

    # Summary Report that shows all about insertion, duplication and errors
    logging.info("========== Summary Report ==========")
    for category in inserted:
        logging.info(f"{category.capitalize()} inserted: {inserted[category]}")
        logging.info(f"{category.capitalize()} duplicates skipped: {duplicates[category]}")
        logging.info(f"{category.capitalize()} errors: {errors[category]}")
    logging.info("====================================")




# def main():
    # print("Hello from main")
    # members, books, authors,libraries \
    #     = load_and_validate_data('csv_data/Members.csv',
    #                              'csv_data/Books.csv',
    #                              'csv_data/Authors.csv',
    #                              'csv_data/Libraries.csv')


    # print(f"Loaded {len(members)} valid members.")
    # print(f"Loaded {len(books)} valid books.")
    # print(f"Loaded {len(authors)} valid authors.")
    # print(f"Loaded {len(libraries)} valid libraries.")
    #
    # for member in members:
    #     print(member)
    # for book in books:
    #     print(book)
    # for author in authors:
    #     print(author)
    # for library in libraries:
    #     print(library)

    # insert_data(members, books, authors, libraries)

# if __name__ == '__main__':
#     main()


