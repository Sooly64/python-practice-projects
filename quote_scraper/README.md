# Quote Scraper

This is a simple Python script that scrapes quotes from [Quotes to Scrape](https://quotes.toscrape.com/) based on a specific tag. You can input a tag (such as "love", "inspirational", or "life"), and the script will fetch all quotes associated with that tag from the website.

The script uses **requests** to fetch the HTML page and **BeautifulSoup** to parse the HTML and extract the relevant quote data.

## Features

- Fetches quotes by a specified tag.
- Automatically handles pagination to fetch quotes from multiple pages.
- Filters quotes to only show those under 200 characters.

## Installation

1. Clone or download this repository.
2. Install the required dependencies:

   ```bash
   pip install requests beautifulsoup4
   ```

## Usage

### Command Line Usage

To run the script and fetch quotes for a specific tag, simply execute the script and provide the tag as an input when prompted:

```bash
python quotes_scraper.py
Enter a tag to look for! love/inspirational/life/humor/books/reading/friendship/friends/truth/simile:
```

The script will then display all short quotes related to that tag.

### Example

1. Running the script with the tag "life":

   ```bash
   python quotes_scraper.py
   Enter a tag to look for! love/inspirational/life/humor/books/reading/friendship/friends/truth/simile: life
   ```

2. Output:

   ```
   These are all the short life quotes!

   "The purpose of life is not to be happy. It is to be useful, to be honorable, to be compassionate, to have it make some difference that you have lived and lived well." - Ralph Waldo Emerson

   "In three words I can sum up everything I've learned about life: it goes on." - Robert Frost

   ...
   ```

## How It Works

1. **Fetch Quotes by Tag**: The script takes a tag as input (e.g., "life", "humor") and forms the URL for that tag.
2. **Pagination Handling**: If there are multiple pages of quotes for the tag, the script will follow the "next" links and fetch quotes from subsequent pages.
3. **Quote Extraction**: For each quote, it extracts the text of the quote and the author's name.
4. **Filtering**: It only displays quotes that are under 200 characters long.

## Contributing
2. **Pagination Handling**: If there are multiple pages of quotes for the tag, the script will follow the "next" links and fetch quotes from subsequent pages.
3. **Quote Extraction**: For each quote, it extracts the text of the quote and the author's name.
4. **Filtering**: It only displays quotes that are under 200 characters long.

## Contributing
