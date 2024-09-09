from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

username="standard_user"
password="secret_sauce"

login_url="https://www.saucedemo.com/"
driver.get(login_url)

user_field=driver.find_element(By.ID,"user-name")
pass_field=driver.find_element(By.ID, "password")

user_field.send_keys(username)
pass_field.send_keys(password)

login_field=driver.find_element(By.ID,"login-button")
assert not login_field.get_attribute("disabled")
login_field.click()

success_message=driver.find_element(By.CSS_SELECTOR,".title")
assert success_message.text=="Products"

time.sleep(20)
driver.quit()
