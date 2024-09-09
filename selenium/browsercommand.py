from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

url="https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
driver.get(url)

time.sleep(5)
driver.find_element(By.CSS_SELECTOR,(".oxd-text.oxd-text--p.orangehrm-login-forgot-header")).click()
time.sleep(4)

driver.back()
time.sleep(4)

driver.forward()
time.sleep(4)

driver.refresh()





time.sleep(30)