"""module providing a function for printing python version."""

# import sys
# import requests

# # print(sys.version)
# print(sys.executable)


# r = requests.get('https://www.python.org', timeout=10)
# print(r.status_code)
# # def greet(who_to_greet):
# #     greeting = f'Hello, {who_to_greet}'
# #     return greeting
# name = input('what is your name')
# print('Hello', name)
# # print(greet('World'))
# # print(greet('Caleb'))


# import requests
# from bs4 import BeautifulSoup

# # URL of the site to scrape
# # url = "http://books.toscrape.com/"
# url = "https://books.toscrape.com/catalogue/category/books/travel_2/index.html"

# # Send a GET request to the site
# response = requests.get(url, timeout=10)

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

# import requests

# api_url = "https://api.weather.gov"

# params = {
#     "api_key": "i8uJfSCrb66QUZDqTAmIXh1UyA4f6PTTN2INpmbJ",  # Some APIs require a key, often free upon registration
#     "city": "New York",
# }

# response = requests.get(api_url, params=params, timeout=10)

# # Check if the request was successful
# if response.status_code == 200:
#     data = response.json()  # Parse JSON response
#     print(data)
# else:
#     print(f"Failed to retrieve data. Status code: {response.status_code}")



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Set up the Selenium WebDriver
driver = webdriver.Chrome()  # Ensure you have ChromeDriver installed and added to your PATH

# Navigate to the website
url = "https://library.nou.edu.ng/e-courseware/"
driver.get(url)

try:
    # Wait for the Faculty dropdown to load and select "Faculty of Agric"
    faculty_dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "Faculty"))
    )
    faculty_dropdown.click()
    faculty_option = driver.find_element(By.XPATH, "//option[text()='Agricultural Sciences']")
    faculty_option.click()
    time.sleep(2)  # Allow content to load

    # Look for the Course Title "Cultural Tourism"
    course_table = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "course_table"))
    )
    rows = course_table.find_elements(By.TAG_NAME, "tr")

    # Loop through rows to find "Cultural Tourism"
    for row in rows:
        if "Cultural Tourism" in row.text:
            # Find the download link
            download_link = row.find_element(By.LINK_TEXT, "Download")
            pdf_url = download_link.get_attribute("href")

            # Download the PDF
            pdf_response = requests.get(pdf_url)
            pdf_filename = os.path.join(os.getcwd(), "Cultural_Tourism.pdf")
            with open(pdf_filename, "wb") as pdf_file:
                pdf_file.write(pdf_response.content)

            print(f"PDF downloaded successfully: {pdf_filename}")
            break
    else:
        print("Course Title 'Cultural Tourism' not found.")

finally:
    # Close the browser
    driver.quit()