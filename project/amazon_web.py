from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import time

driver = webdriver.Chrome()

driver.get("https://www.amazon.com/s?k=laptops")

time.sleep(3)

html = driver.page_source
driver.quit()

soup = BeautifulSoup(html, 'html.parser')

product_names = soup.find_all('span', class_='a-size-medium a-color-base a-text-normal')
product_prices = soup.find_all('span', class_='a-offscreen')
product_ratings = soup.find_all('span', class_='a-icon-alt')

products_data = []

for name, price, rating in zip(product_names, product_prices, product_ratings):
    products_data.append({
        "Name": name.get_text(strip=True),
        "Price": price.get_text(strip=True),
        "Rating": rating.get_text(strip=True)
    })

csv_file = "amazon_products.csv"
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=["Name", "Price", "Rating"])
    writer.writeheader()  
    writer.writerows(products_data)

print(f"Data has been successfully saved to {csv_file}")
