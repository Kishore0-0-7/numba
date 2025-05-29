import requests
from bs4 import BeautifulSoup

def fetch_books_data():
    #replace https://www.examplebookswebsite.com with some website of your choice
    url = "https://www.examplebookswebsite.com"

    # Try block runs if no error occurs
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')    #parses raw HTML content to BeautifulSoup object named soup
        book_list = soup.find_all('div', class_='book-item')

        for book in book_list:
            title = book.find('h2', class_='book-title').text
            author = book.find('p', class_='book-author').text
            price = book.find('span', class_='book-price').text

            print(f"Title: {title}")
            print(f"Author: {author}")
            print(f"Price: {price}\n")
            
    except Exception as e:
        print(f"An error occurred: {e}")
# To run this file as a script
if __name__ == "__main__":
    fetch_books_data()
