import requests
from bs4 import BeautifulSoup
import random

def skini_citat_sa_weba():
    url = "http://quotes.toscrape.com/random"
    response = requests.get(url)
    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        citat_element = soup.find('span', class_='text')
        if citat_element:
            return citat_element.text.strip()
    return "Nije moguće skidati citat sa weba trenutno."

def main():
    citat = skini_citat_sa_weba()
    print(citat)

if __name__ == "__main__":
    main()
