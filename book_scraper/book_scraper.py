import requests
from bs4 import BeautifulSoup
import csv
import os

# Enter a folder to save the csv data (default current working directory)
FOLDER_PATH = os.path.join(os.getcwd(), "book_scraper")

# Helper method for string-float conversion
def string_to_float(s):
    cleaned_string = ''.join([char for char in s if char.isdigit() or char == '.'])
    return float(cleaned_string)

# Gets unsorted raw book data as dictionary
def fetch_books_with_price():

    books = { }

    # URL Instantiation
    base_url = "https://books.toscrape.com/catalogue/"
    url = f"{base_url}page-1.html"

    # Loops for each book page and adds data to dictionary
    while True:

        # Gets Webdata
        request = requests.get(url)
        WebData = BeautifulSoup(request.text, "html.parser")

        # Gets data for each book
        book_blocks = WebData.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
        for book_block in book_blocks:
            # Gets book name
            name_line = book_block.find("h3")
            book_name_element = name_line.find("a")
            book_name = book_name_element['title']

            # Gets book price
            price_line = book_block.find("div", class_="product_price")
            price = price_line.find("p", class_="price_color").text.strip()

            # Avalibility check
            avalibility = "in" in price_line.find("p", class_="instock availability").text.strip().lower()
            if avalibility:
                # Instantiates raw data into dictionary
                books[book_name] = string_to_float(price)

        # Find next page if avalible, else break
        next_line = WebData.find("li", class_="next")
        if next_line:
            next_element = next_line.find("a")
            next_link = next_element["href"]
            url = base_url + next_link
        else:
            break
    
    # Returns the raw book data
    return books

# Store data into CSV cleanly with header row and price unit
def save_books_to_csv(books, folder,filename):

    os.makedirs(folder, exist_ok=True)
    file_path = os.path.join(folder, filename)

    with open(file_path, mode = 'w', newline = '', encoding = 'utf-8') as file:

        writer = csv.writer(file)

        writer.writerow(["Book Name","Price"])

        for book_name, price in books.items():
            writer.writerow([book_name, f"£{price}"])

# Main Control Flow
def main():
    # Gets books and sorts them based on values/prices
    books = fetch_books_with_price()
    sorted_books = dict(sorted(books.items(), key = lambda item: item[1]))

    # Saves books to csv and prints completion message
    save_books_to_csv(sorted_books, FOLDER_PATH, "book_data.csv")
    print(f"Data saved to {FOLDER_PATH}/book_data.csv")

# Execution!
main()