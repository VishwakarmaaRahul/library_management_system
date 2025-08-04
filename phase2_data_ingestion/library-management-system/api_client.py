import requests
import json

class OpenLibraryAPIClient:
    BASE_URL = "https://openlibrary.org"

    def search_author(self, author_name: str):
        url = f"{self.BASE_URL}/search/authors.json"
        params = {"q": author_name}
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        if not data['docs']:
            raise ValueError(f"Author '{author_name}' not found.")
        return data['docs'][0]

    def get_author_works(self, author_key: str, limit: int):
        url = f"{self.BASE_URL}/authors/{author_key}/works.json"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data.get("entries", [])[:limit]

    def get_work_details(self, work_key: str):
        url = f"{self.BASE_URL}/works/{work_key}.json"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data

    def get_editions_for_work(self, work_key: str, limit: int = 1):
        url = f"{self.BASE_URL}/works/{work_key}/editions.json"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        editions = data.get("entries", [])
        if editions:
            return editions[:limit]
        return []

    def get_book_details(self, edition_key: str):
        url = f"{self.BASE_URL}/books/{edition_key}.json"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        # print(f"Full Book Details for {edition_key}:")
        # print(json.dumps(data, indent=2))

        return data