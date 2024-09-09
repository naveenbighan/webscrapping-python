from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
import time

driver= webdriver.Chrome()
url="https://the-internet.herokuapp.com/broken_images"
driver.get(url)
driver.maximize_window()

images=driver.find_elements(By.TAG_NAME,("img"))
broken_images=[]
for image in images:
    src=image.get_attribute("src")
    response= requests.get(src)
    if response.status_code!= 200:
        broken_images.append(src)
        print("broken images found")
print(broken_images)
    