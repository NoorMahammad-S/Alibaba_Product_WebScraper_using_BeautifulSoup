import requests
from bs4 import BeautifulSoup
import csv

# URL of the Alibaba product listings you want to scrape
url = "https://www.alibaba.com/products/F0/products.html"

# Send a GET request to the Alibaba URL
response = requests.get(url)

# Parse the HTML content of the page
soup = BeautifulSoup(response.text, 'html.parser')

# Find the section containing product information
products_section = soup.find('div', {'class': 'm-gallery-product-item'})

# Check if products_section is not None
if products_section is not None:
    # Create a CSV file to store the scraped data
    csv_filename = "alibaba_products.csv"

    # Open the CSV file for writing with UTF-8 encoding
    with open(csv_filename, mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.writer(csv_file)

        # Write the header row
        writer.writerow(["Product Name", "Price", "Description"])

        # Find and write data rows
        product_elements = products_section.find_all('div', {'class': 'item-main'})
        for product_element in product_elements:
            product_name = product_element.find('a', {'class': 'item-info-title'}).text.strip()
            price = product_element.find('div', {'class': 'item-price'}).text.strip()
            description = product_element.find('div', {'class': 'item-detail'}).text.strip()

            writer.writerow([product_name, price, description])

    print(f"Scraped Alibaba product data and saved to {csv_filename}")
else:
    print("Products section not found on the page. Check the page structure.")
