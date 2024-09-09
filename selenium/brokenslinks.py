from selenium import webdriver
from selenium.webdriver.common.by import By 
import time
import requests



browser=webdriver.Chrome()

url="https://jqueryui.com/ "
browser.get(url)

links=browser.find_elements(By.TAG_NAME,("a"))
print(len(links))

for link in links:
    href= link.get_attribute("href")
    response=requests.get(href)
    if response.status_code >=400:
        print(f"broken links{href}and status code: {response.status_code}")

time.sleep(100)