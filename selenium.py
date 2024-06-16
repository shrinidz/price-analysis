import time
import json
import csv
import re
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Function to extract the numeric part of the price
def extract_price(price_str):
    match = re.search(r'\d+', price_str.replace(',', ''))
    return match.group() if match else 'N/A'

# Initialize the Chrome driver
try:
    service = Service("D:/chromedriver/chromedriver-win64/chromedriver.exe")
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Uncomment to run in headless mode
    driver = webdriver.Chrome(service=service, options=chrome_options)
except Exception as e:
    print(f"Error initializing the Chrome driver: {e}")
    exit()

# Open Flipkart
try:
    driver.get("https://www.flipkart.com/")
    time.sleep(5)
except Exception as e:
    print(f"Error opening Flipkart: {e}")
    driver.quit()
    exit()

# Close the login popup if it appears
try:
    close_login_popup = driver.find_element(By.XPATH, "//button[contains(text(), '✕')]")
    close_login_popup.click()
except Exception as e:
    print("Login popup not found or already closed.")

# Find the search bar and search for "Hindi Books"
try:
    search_bar = driver.find_element(By.NAME, "q")
    search_bar.send_keys("Hindi Books")
    search_bar.send_keys(Keys.RETURN)
except Exception as e:
    print(f"Error finding search bar or searching: {e}")
    driver.quit()
    exit()

try:
    driver.maximize_window()
    time.sleep(5)  # Wait for the results to load
except Exception as e:
    print(f"Error maximizing window or waiting: {e}")
    driver.quit()
    exit()

# Scrape book details
books = []



# Find all elements matching the given XPaths
try:
    name_elements = driver.find_elements(By.XPATH, "//*[contains(@class,'wjcEIp')]")
    price_elements = driver.find_elements(By.XPATH, "//*[contains(@class,'Nx9bqj')]")
    rating_elements = driver.find_elements(By.XPATH, "//*[contains(@class,'Y1HWO0')]")
except Exception as e:
    print(f"Error finding elements: {e}")
    driver.quit()
    exit()



# Iterate over the elements and store the data in a dictionary
for i in range(name_elements):
    try:
        name = name_elements[i].text
        price = extract_price(price_elements[i].text)
        rating = rating_elements[i].text

        books.append({
            "name": name,
            "price": price,
            "rating": rating
        })
    except Exception as e:
        print(f"Error getting data from elements: {e}")

# Close the driver
try:
    driver.quit()
except Exception as e:
    print(f"Error closing the driver: {e}")

# Save the scraped data to a JSON file
try:
    with open('hindi_books.json', 'w', encoding='utf-8') as json_file:
        json.dump(books, json_file, ensure_ascii=False, indent=4)
except Exception as e:
    print(f"Error saving to JSON file: {e}")

# Save the scraped data to a CSV file
try:
    keys = books[0].keys()
    with open('hindi_books.csv', 'w', newline='', encoding='utf-8') as csv_file:
        dict_writer = csv.DictWriter(csv_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(books)
except Exception as e:
    print(f"Error saving to CSV file: {e}")

print("Data scraped and saved successfully!")
