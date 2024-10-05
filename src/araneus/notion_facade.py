import requests
import os
from dotenv import load_dotenv
import logging
logging.basicConfig(level=logging.DEBUG)
from datetime import datetime

# Get the current date
current_date = datetime.now().date()

load_dotenv()
NOTION_API_URL = "https://api.notion.com/v1/pages"
TOKEN = os.getenv('NOTION_SECRET')
NOTION_API_VERSION = "2022-06-28"
PARENT_PAGE_ID = os.getenv('NOTION_PARENT_PAGE_ID')

class NotionFacade:
    def __init__(self) -> None:
        pass

    def create_child_page_in_notion(self, prompt):
        url = NOTION_API_URL

        headers = {
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json",
            "Notion-Version": NOTION_API_VERSION
        }

        payload = {
            "parent": {
                "type": "page_id",
                "page_id": PARENT_PAGE_ID
            },
            "properties": {
                "title": [
                    {
                        "type": "text",
                        "text": {
                            "content": f"{current_date}"
                        }
                    }
                ]
            },
            "children": [
                {
                    "object": "block",
                    "type": "heading_3",
                    "heading_3": {
                        "rich_text": [
                            {
                                "type": "text",
                                "text": {
                                    "content": prompt
                                }
                            }
                        ]
                    }
                }
            ]
        }

        response = requests.post(url, headers=headers, json=payload)

        logging.info(f"Response Status: {response.status_code}")
        logging.info(f"Response Body: {response.json()}")
