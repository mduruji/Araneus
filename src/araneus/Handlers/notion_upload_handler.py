# import requests
# import os
# from dotenv import load_dotenv

# # Load secret token and parent page ID from .env file
# load_dotenv()
# NOTION_API_URL = "https://api.notion.com/v1/blocks/{parent_page_id}/children"
# TOKEN = os.getenv('NOTION_SECRET')
# NOTION_API_VERSION = "2022-06-28"
# PARENT_PAGE_ID = os.getenv('NOTION_PARENT_PAGE_ID')

# class NotionFacade:
#     def __init__(self) -> None:
#         pass

#     def create_child_page_in_notion():
#         url = NOTION_API_URL.replace("{parent_page_id}", PARENT_PAGE_ID)

#         headers = {
#             "Authorization": f"Bearer {TOKEN}",
#             "Content-Type": "application/json",
#             "Notion-Version": NOTION_API_VERSION
#         }

#         # JSON payload for the child page
#         payload = {
#             "children": [
#                 {
#                     "object": "block",
#                     "type": "child_page",
#                     "child_page": {
#                         "title": "Child Page from Python"
#                     }
#                 }
#             ]
#         }

#         # Send the POST request to create the child page
#         response = requests.post(url, headers=headers, json=payload)

#         # Print response
#         print(f"Response Status: {response.status_code}")
#         print(f"Response Body: {response.json()}")

#     # Example usage
#     create_child_page_in_notion()
