from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver=webdriver.Chrome()
driver.get("https://www.selenium.dev/")
driver.switch_to.new_window()
driver.get("https://playwright.dev/")

driver.find_element(By.CLASS_NAME,("getStarted_Sjon")).click()
time.sleep(4)
first_tab=driver.window_handles[0]
driver.switch_to.window(first_tab)
driver.find_element(By.XPATH,("/html/body/header/nav/div/ul/li[2]/a/span")).click()
time.sleep(20)