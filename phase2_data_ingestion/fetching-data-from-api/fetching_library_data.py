from http.client import responses

import requests
from bs4 import BeautifulSoup


# def fetch_data_from_library_api():
#     r = requests.get('https://openlibrary.org')
#     print(r)
#     # print(dir(r))
#     # print(r.headers['content-type'])
#     # print(r.text)
#
#     # data = r.json()
#     # print(data)
#
#
# soup = BeautifulSoup(r.text, 'html.parser')
# # print(soup.prettify())
# all_divs = soup.find_all('div')
#
# for div in all_divs[:10]:
#     print(div)
#     print('-' * 40)


# def search_author(author_name):
#     url = f"https://openlibrary.org/search/authors.json?q={author_name}"
#     response = requests.get(url)
#     data = response.json()
#     if data['numFound'] > 0:
#         return data['docs'][0]['key']  # get a first author key like "/authors/OL26320A"
#     else:
#         return None
#
# def main():
#     # fetch_data_from_library_api()
#     print(search_author("Tennessee Williams"))
#
# if __name__ == "__main__":
#     main()


#
# url = "https://openlibrary.org/search.json?q=Gitanjali"
# url = "https://openlibrary.org/search/authors.json?q=Rabindranath Tagore"
# r = requests.get(url)
# data = r.json()
# # print(data)
#
# for index, author in enumerate(data.get("docs", [])[:3], 1):
#     print(index, author)
#     # Loop through each field in the author object
#     for key, value in author.items():
#         print(f"{key}: {value}")
#         url = f"https://openlibrary.org/works/value.json"
#         response = requests.get(url)
#         author_data = response.json()
#         soup = BeautifulSoup(response.text, 'html.parser')
#         print(soup.prettify())


import requests
from bs4 import BeautifulSoup

url = "https://openlibrary.org/search/authors.json?q=Rabindranath Tagore"
r = requests.get(url)
data = r.json()

for index, author in enumerate(data.get("docs", [])[:3], 1):
    print(f"\nAuthor #{index}")

    for key, value in author.items():
        print(f"{key}: {value}")

    # Get author key and fetch author details
    author_key = author.get("key")  # e.g., "OL1770A"

    if author_key:
        detail_url = f"https://openlibrary.org/authors/{author_key}.json"
        response = requests.get(detail_url)

        if response.status_code == 200:
            author_data = response.json()
            print("\nAuthor JSON data from detailed endpoint:")
            print(author_data)
        else:
            print(f"Failed to fetch details for {author_key}")

#
# print(author_data["key"])
# print(author_data["name"])
# print(author_data["birth_date"])
# print(author_data["bio"])




# url = f"https://openlibrary.org/authors/OL1770A/works.json"
# response = requests.get(url)
# book_data = response.json()
#
# title_data = book_data["entries"]
# count = 0
# for entry in title_data:
#     count = count+1
#     print(entry["title"])
#
# print(count)



#
# #Search for authors named "Tolkien"
#
# author_name = "Tolkien"
# url = f"https://openlibrary.org/search/authors.json?q={author_name}"
# response = requests.get(url)
# data = response.json()
#
# for author in data.get('docs', [])[:3]:
#     print(f"Name: {author.get('name')}, Key: {author.get('key')}")
#
# #Search for books with "Hobbit
#
# search_term = "Hobbit"
# url = f"https://openlibrary.org/search.json?q={search_term}"
# response = requests.get(url)
# data = response.json()
#
# for book in data.get('docs', [])[:3]:
#     print(f"Title: {book.get('title')}, Author: {book.get('author_name')}")
#


#Get works by author with key /authors/OL26320A (Tolkien)

# author_key = "OL26320A"
# url = f"https://openlibrary.org/authors/{author_key}/works.json"
# response = requests.get(url)
# data = response.json()
#
# for work in data.get('entries', [])[:3]:
#     print(f"Title: {work.get('title')}, Key: {work.get('key')}")


#Get details of work /works/OL82563W

# work_key = "OL82563W"
# url = f"https://openlibrary.org/works/{work_key}.json"
# response = requests.get(url)
# data = response.json()
#
# print(f"Title: {data.get('title')}")
# print(f"Description: {data.get('description')}")
# print(f"First publish date: {data.get('first_publish_date')}")



import requests
import json

url = "https://openlibrary.org/books/OL27187262M.json"
headers = {
    "User-Agent": "MyApp/1.0 (rahulvishwakarmnados@gmail.com)"
}
response = requests.get(url, headers=headers)
data = response.json()

# print(data)
print(f"Book Key: {data.get('key')}")
print(f"Title: {data.get('title')}")
print(f"Author: {data.get('authors')}")
print(f"Publish Date: {data.get('publish_date', 'Unknown')}")
print(f"ISBN_10: {data.get('isbn_10')}")
print(f"ISBN_13: {data.get('isbn_13')}")
print(f"Description: {data.get('description', {}).get('value', 'No description available')}")
# print(json.dumps(data, indent=2))

