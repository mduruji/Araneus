import requests
from bs4 import BeautifulSoup
import logging
logging.basicConfig(level=logging.DEBUG)
import os
from dotenv import load_dotenv

load_dotenv()
URL = os.getenv('SEED_URL')

class Scraper:
    def __init__(self) -> None:
        pass
        
    def scrape_for_links(self):
        try:
            response = requests.get(URL)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, 'html.parser')

            h2_tags = soup.find_all('h2', {'class' : 'wp-block-post-title'})
            
            links = [h2.find('a') for h2 in h2_tags]

            link_list = [(link.get_text(), link['href']) for link in links]

            for text, href in link_list:
                logging.info(f"Link found: {text} ({href})")

            hrefs = [link['href'] for link in links]

            return hrefs
        except requests.exceptions.RequestException as e:
            logging.error(f"HTTP Request failed: {e}")

    def scrape_for_prompts(self, url):
        try:
            response = requests.get(url)
            response.raise_for_status()

            soup = BeautifulSoup(response.content, 'html.parser')
            
            list_items = soup.select('ol.wp-block-list > li')

            prompts = [f"{item.get_text()}" for item in list_items]

            page_name = url.split("/")[-2]
            
            if len(prompts) > 1:
                logging.info(f"Prompts in {page_name} scraped successfully")
            else:
                logging.info(f"No prompts found in {page_name}")

            return {page_name: prompts}
        except requests.exceptions.RequestException as e:
            logging.error(f"HTTP Request failed: {e}")
            return {}
