import argparse
import logging
import os
from schemas import load_and_validate_data

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Load and validate CSV data into a database"
    )

    parser.add_argument(
        '--directory', '-d',
        required=True,
        help='Path to the directory containing CSV files'
    )
    parser.add_argument(
        '--database-url', '--db',
        required=True,
        help='SQLAlchemy-compatible database URL'
    )
    parser.add_argument(
        '--log-level',
        default='INFO',
        choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'],
        help='Logging level (default: INFO)'
    )

    return parser.parse_args()

def setup_logging(level):
    logging.basicConfig(
        level=getattr(logging, level.upper(), logging.INFO),
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def main():
    args = parse_arguments()
    setup_logging(args.log_level)

    logging.info("Starting data processing...")
    try:
        dir = args.directory
        load_and_validate_data(
            os.path.join(dir, "members.csv"),
            os.path.join(dir, "books.csv"),
            os.path.join(dir, "authors.csv"),
            os.path.join(dir, "libraries.csv")
        )
        logging.info("Data successfully loaded into the database.")
    except Exception as e:
        logging.error(f"Failed to load data: {e}", exc_info=True)

if __name__ == '__main__':
    main()




