import pandas as pd

df = pd.read_csv("csv_data/BooksOLD.csv")

df.drop(columns=["book_id", "total_copies","available_copies","library_id"], inplace=True)

df.to_csv("Books.csv", index=False)
