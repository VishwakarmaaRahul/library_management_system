from api_client import OpenLibraryAPIClient
from schemas import get_session, insert_book_if_not_exists
from schemas import Book
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--author', required=True)
    parser.add_argument('--limit', type=int, default=5)
    parser.add_argument('--db', required=True)
    args = parser.parse_args()

    client = OpenLibraryAPIClient()
    session = get_session(args.db)

    author = client.search_author(args.author)
    works = client.get_author_works(author["key"], args.limit)

    for work in works:
        editions = client.get_editions_for_work(work["key"].split("/")[-1])
        if not editions:
            continue

        edition_key = editions[0]["key"].split("/")[-1]
        book_data = client.get_book_details(edition_key)

        try:
            book = Book.from_api(book_data)
            insert_book_if_not_exists(session, book)
            print(f"Inserted: {book.title}")
        except Exception as e:
            print(f"Skipping '{work['title']}': {e}")

if __name__ == "__main__":
    main()
