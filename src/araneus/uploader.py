from concurrent.futures import ThreadPoolExecutor
from dynamo_db_facade import DynamoDBFacade
from prompt_scraper import Scraper

scraper = Scraper()
dynamo = DynamoDBFacade()

TABLE_NAME = "Journal"
dynamo.create_category_table(TABLE_NAME)
links = scraper.scrape_for_links()

def upload(prompt_category, prompts):
    prompt_id = 1
    for prompt in prompts:
        dynamo.add_prompt(TABLE_NAME, prompt_category, prompt_id, prompt)
        prompt_id += 1

def process_link(link):
    prompt_collection = scraper.scrape_for_prompts(link)
    
    if prompt_collection:
        prompt_category = list(prompt_collection.keys())[0]
        prompts = prompt_collection[prompt_category]
        upload(prompt_category, prompts)

def main():
    max_workers = len(links)
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        executor.map(process_link, links)

if __name__ == '__main__':
    main()
