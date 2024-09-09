from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver= webdriver.Chrome()
url="https://google.com/"
driver.get(url)
driver.maximize_window()

# 

viewport=[(430,932),(1024,1366),(912,1368),(1068,577)]

try:
    for width,height in viewport:
        driver.set_window_size(width,height)
        time.sleep(4)
finally:
    driver.close()

time.sleep(30)

