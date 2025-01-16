"""module providing a function for printing python version."""

import sys
import requests

# print(sys.version)
print(sys.executable)


r = requests.get('https://www.python.org', timeout=10)
print(r.status_code)
# def greet(who_to_greet):
#     greeting = f'Hello, {who_to_greet}'
#     return greeting
name = input('what is your name')
print('Hello', name)
# print(greet('World'))
# print(greet('Caleb'))


# import requests
# from bs4 import BeautifulSoup

# # URL of the site to scrape
# url = "http://books.toscrape.com/"

# # Send a GET request to the site
# response = requests.get(url)

# # Check if the request was successful
# if response.status_code == 200:
#     # Parse the HTML content
#     soup = BeautifulSoup(response.content, "html.parser")
 
#     #Find all book prices (replace 'price_color' with the actual class for prices)
#     prices = soup.find_all(class_="price_color")
    
#     # Print the extracted prices
#     for price in prices:
#         print(price.get_text(strip=True))
# else:
#     print(f"Failed to retrieve the webpage. Status code: {response.status_code}")