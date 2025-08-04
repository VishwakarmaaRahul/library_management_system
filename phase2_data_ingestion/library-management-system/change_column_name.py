import pandas as pd

df = pd.read_csv("csv_data/BooksOLD.csv")

# Rename columns using a dictionary: {"old_name": "new_name"}
df.rename(columns={"publication_date": "published_date"}, inplace=True)

# Save the updated CSV
df.to_csv("csv_data/BooksOLD.csv", index=False)