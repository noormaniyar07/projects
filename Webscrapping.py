

import requests
from bs4 import BeautifulSoup

url = input("Enter the URL of the website to scrape: ")

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

print("Available tags in the HTML:\n")
for tag in soup.find_all(True):  
    print(tag.name, tag.attrs)

    
    quotes = soup.find_all('span', class_='text')
    authors = soup.find_all('small', class_='author')

    print("\nQuotes and Authors:\n")
    for quote, author in zip(quotes, authors):
        print(f"Quote: {quote.get_text()}")
        print(f"Author: {author.get_text()}\n")


