from pydantic import BaseModel, EmailStr, field_validator,ValidationError
import phonenumbers
import logging
import re
import csv
from datetime import date , datetime

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

    return members, books, authors, libraries

def main():
    members, books, authors,libraries \
        = load_and_validate_data('csv_data/Members.csv',
                                 'csv_data/Books.csv',
                                 'csv_data/Authors.csv',
                                 'csv_data/Libraries.csv')


    print(f"Loaded {len(members)} valid members.")
    print(f"Loaded {len(books)} valid books.")
    print(f"Loaded {len(authors)} valid authors.")
    print(f"Loaded {len(libraries)} valid libraries.")

    for member in members:
        print(member)
    for book in books:
        print(book)
    for author in authors:
        print(author)
    for library in libraries:
        print(library)

if __name__ == '__main__':
    main()


