import requests
from bs4 import BeautifulSoup

def fetch_quotes_by_tag(tag):
    base_url = "https://quotes.toscrape.com"
    url = f"{base_url}/tag/{tag}/"
    quotes = []

    while url:
        response = requests.get(url)
        WebData = BeautifulSoup(response.text, "html.parser")

        quote_boxes = WebData.find_all("div", class_="quote")
        for quote_box in quote_boxes:
            quote = quote_box.find("span", class_="text").text.strip()
            author = quote_box.find("small", class_="author").text.strip()
            if len(quote) < 200:
                quotes.append((f"{quote} - {author}"))

        next_btn = WebData.find("li", class_="next")
        if next_btn:
            next_page = next_btn.find("a")["href"]
            url = base_url + next_page
        else:
            url = None

    return quotes

def main():
    tag = input("Enter a tag to look for! love/inspirational/life/humor/books/reading/friendship/friends/truth/simile: ")

    print(f"These are all the short {tag} quotes!", end="\n\n")

    quotes = fetch_quotes_by_tag(tag)
    for quote in quotes:
        print(quote, end="\n\n")

    print("All done!")

main()