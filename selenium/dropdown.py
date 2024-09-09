from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select

browser=webdriver.Chrome()
browser.maximize_window()
url="https://the-internet.herokuapp.com/dropdown"
browser.get(url)

dropdown_element=browser.find_element(By.ID,("dropdown"))
select=Select(dropdown_element)
# select.select_by_visible_text("Option 2")
# select.select_by_index(1)
# select.select_by_value("2")
option_count=len(select.options)
print(option_count)



time.sleep(15)