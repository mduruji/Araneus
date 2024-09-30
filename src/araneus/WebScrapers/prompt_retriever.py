# import requests
# from bs4 import BeautifulSoup

# def scrape_page(url):
#     try:
#         # Send an HTTP GET request
#         response = requests.get(url)
#         response.raise_for_status()  # Check for request errors

#         # Parse the HTML content with BeautifulSoup
#         soup = BeautifulSoup(response.content, 'html.parser')

#         # Extract the ordered list (ol) and list items (li)
#         list_items = soup.select('ol > li')

#         # Extract the text from each list item
#         prompts = [item.get_text() for item in list_items]

#         # Return a map with the page name and its prompts
#         page_name = url.split("/")[-1]
#         return {page_name: prompts}

#     except requests.exceptions.RequestException as e:
#         print(f"HTTP Request failed: {e}")
#         return {}

# # Example usage
# url = "https://example.com/page1"
# scraped_data = scrape_page(url)
# print(scraped_data)
