from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import csv
import time


driver = webdriver.Chrome()


url = "http://books.toscrape.com/catalogue/page-1.html"
driver.get(url)

with open('books.csv', 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(['Title', 'Price', 'Availability'])  # Header row

    while True:
        time.sleep(2)
        
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        
        books = soup.find_all('article', class_='product_pod')
        
        for book in books:
            title = book.h3.a['title']
            
            price = book.find('p', class_='price_color').text
            
            availability = book.find('p', class_='instock availability').text.strip()
            
            csv_writer.writerow([title, price, availability])
        
        next_button = soup.find('li', class_='next')
        
        if next_button:
            next_page_url = next_button.a['href']
            next_page_url = url.rsplit('/', 1)[0] + '/' + next_page_url
            driver.get(next_page_url)
        else:
            break



driver.quit()
