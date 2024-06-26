import requests
from bs4 import BeautifulSoup

def fetch_random_quote():
    url = "http://quotes.toscrape.com/random"
    response = requests.get(url)
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        quote_element = soup.find('span', class_='text')
        if quote_element:
            return quote_element.text.strip()
    return "Unable to fetch a quote from the web at the moment."

def main():
    quote = fetch_random_quote()
    print(quote)

if __name__ == "__main__":
    main()
