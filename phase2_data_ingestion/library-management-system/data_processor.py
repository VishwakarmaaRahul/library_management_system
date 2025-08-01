import argparse
import logging
import os

from sqlalchemy import create_engine
from schemas import load_and_validate_data, insert_data
from models import Base

def parse_arguments():
    parser = argparse.ArgumentParser(description="Load and insert library data into database")
    parser.add_argument('--directory', '-d', required=True, help='CSV file directory')
    parser.add_argument('--database-url', '--db', required=True, help='SQLAlchemy DB URL')
    parser.add_argument('--log-level', default='INFO', choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'], help='Log level')
    return parser.parse_args()

def setup_logging(level):
    logging.basicConfig(
        level=getattr(logging, level.upper(), logging.INFO),
        format='%(asctime)s - %(levelname)s - %(message)s',
        filename='validation_errors.log'
    )

def main():
    args = parse_arguments()
    setup_logging(args.log_level)

    try:
        members, books, authors, libraries = load_and_validate_data(
            os.path.join(args.directory, "Members.csv"),
            os.path.join(args.directory, "Books.csv"),
            os.path.join(args.directory, "Authors.csv"),
            os.path.join(args.directory, "Libraries.csv")
        )

        # logging.info(f"Validated {len(members)} members, {len(books)} books, {len(authors)} authors, {len(libraries)} libraries.")
        # logging.info(f"Total members processed: {len(members)}")
        # logging.info(f"Total books processed: {len(books)}")
        # logging.info(f"Total authors processed:{len(authors)}")
        # logging.info(f"Total libraries processed:{len(libraries)}")

        engine = create_engine(args.database_url)
        Base.metadata.create_all(engine)

        insert_data(members, books, authors, libraries, engine)

        for member in members:
            print(member)
        for book in books:
            print(book)
        for author in authors:
            print(author)
        for library in libraries:
            print(library)

    except Exception as e:
        logging.error(f"Error in processing: {e}", exc_info=True)

if __name__ == "__main__":
    main()

