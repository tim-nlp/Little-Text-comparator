import requests
from random import randint
import json

class TextReaderAPI:
    """Reads text from API request"""
    def __init__(self):
        pass


    def get_id(self):
        """Gets two different ids for Gutendex"""
        self.id = randint(1, 3000)

        print(f"ID: {self.id}")

        self.url = f"https://gutendex.com/books?ids={self.id}&languages=en"
        self.r = requests.get(self.url)
        print(f"Status code: {self.r.status_code}")


    def get_text(self):
        """Gets title, author's name and .txt"""

        self.response_dict = self.r.json()
        self.readable_dict = json.dumps(self.response_dict, indent=4)

        try:
            self.url_text = self.response_dict["results"][0]["formats"]["text/plain; charset=utf-8"]
        except ValueError, IndexError:
            print(f"\nThe text could not be accessed.")
        else:
            self.get_text = requests.get(self.url_text)

            self.contents = self.get_text.text
        return self.contents


    def get_book_title(self):
        """Gets title and author"""
        try:
            self.title = self.response_dict["results"][0]["title"]
        except ValueError, IndexError:
            print("\nThe title wasn't found.")
        else:
            print(f"\n{self.title}")
        return self.title


    def get_book_author(self):
        """Gets title and author"""
        try:
            self.author = self.response_dict["results"][0]["authors"][0]["name"]
        except ValueError, IndexError:
            print("\nThe author wasn't found.")
        else:
            print(f"by {self.author}")
        return self.author
