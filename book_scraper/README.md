# Book Scraper

A Python script that scrapes book data from [books.toscrape.com](https://books.toscrape.com) and saves it to a sorted CSV file.

## Features
- Scrapes book titles and prices from all pages
- Filters out unavailable books
- Sorts books by price (ascending)
- Creates "book_scraper" folder automatically
- Saves results in CSV with GBP formatting

## Requirements
```bash
Python 3.x
requests
beautifulsoup4
```

Install dependencies:
```bash
pip install requests beautifulsoup4
```

## Usage
1. Save script as `book_scraper.py`
2. Run:
```bash
python book_scraper.py
```
3. Find results in:
```
<current_dir>/book_scraper/book_data.csv
```

## Sample Output
| Book Name                  | Price  |
|----------------------------|--------|
| A Light in the Attic       | £51.77 |
| Tipping the Velvet         | £53.74 |

## Notes
- Only includes in-stock books
- Website structure changes may break scraper, based on the specific strucutre of the webpage from my snooping around
- Consider adding delays for production use
- Respects robots.txt (Doesn't even have one and its a scraping website ():)

## License
[MIT](https://choosealicense.com/licenses/mit/)
