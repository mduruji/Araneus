# import requests
# from bs4 import BeautifulSoup

# def scrape_for_links(url):
#     try:
#         # Send an HTTP GET request to fetch the webpage
#         response = requests.get(url)
#         response.raise_for_status()  # Check for HTTP request errors

#         # Parse the HTML content using BeautifulSoup
#         soup = BeautifulSoup(response.content, 'html.parser')

#         # Extract all anchor tags with href attributes
#         links = soup.find_all('a', href=True)

#         # Collect the links in an array
#         link_list = [(link.get_text(), link['href']) for link in links]

#         # Print all found links
#         for text, href in link_list:
#             print(f"Link found: {text} ({href})")

#         return link_list

#     except requests.exceptions.RequestException as e:
#         print(f"HTTP Request failed: {e}")

# # Example usage
# url = "https://example.com"
# scraped_links = scrape_for_links(url)
