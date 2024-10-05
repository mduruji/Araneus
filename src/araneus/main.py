from notion_facade import NotionFacade
from dynamo_db_facade import DynamoDBFacade
import logging

logging.basicConfig(level=logging.DEBUG)

TABLE_NAME = "Journal"
FILE_PATH = "src/araneus/cache.txt"

notion = NotionFacade()
dynamo = DynamoDBFacade()

categories = [
    "25-lenten-journal-prompts",
    "30-bible-study-journal-prompts",
    "12-habits-of-happy-couples",
    "25-christmas-journal-prompts",
    "christian-journal-prompts",
]

def read_cache_file():
    """Reads the cache file and returns a dictionary with key-value pairs."""
    values = {}
    try:
        with open(FILE_PATH, 'r') as file:
            for line in file:
                key, value = line.strip().split('=')
                values[key] = value
    except FileNotFoundError:
        logging.error(f"Cache file not found: {FILE_PATH}")
    except Exception as e:
        logging.error(f"Error reading cache file: {e}")
    return values

def write_cache_file(data):
    """Writes a dictionary to the cache file."""
    try:
        with open(FILE_PATH, 'w') as file:
            for key, value in data.items():
                file.write(f"{key}={value}\n")
    except Exception as e:
        logging.error(f"Error writing to the file: {e}")

def update_cache_file(key, new_value):
    """Updates a specific key-value pair in the cache file."""
    data = read_cache_file()
    if key in data:
        data[key] = str(new_value)
        write_cache_file(data)
    else:
        logging.error(f"Key '{key}' not found in the cache.")

values = read_cache_file()

if values:
    category_id_key, prompt_id_key = tuple(values.keys())
    category_index, prompt_id = [int(num) for num in list(values.values())]

    if category_index < len(categories):
        category = categories[category_index]
        print(category)

        if __name__ == "__main__":
            try:
                prompt = dynamo.get_prompt(TABLE_NAME, category, prompt_id)

                notion.create_child_page_in_notion(prompt)

                prompt_id += 1
    
                update_cache_file(prompt_id_key, prompt_id)

            except Exception as e:
                logging.error(f"Error retrieving or processing the prompt: {e}")
    else:
        logging.error("Category index out of range.")
else:
    logging.error("Cache values could not be loaded.")
