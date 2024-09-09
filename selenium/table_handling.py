from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://cosmocode.io/automation-practice-webtable/")
driver.maximize_window()
driver.execute_script("window.scrollTo(0,700)")

table= driver.find_element(By.ID,("countries"))
rows=driver.find_elements(By.TAG_NAME,("tr"))
rows_count=len(rows)
print(rows_count)

target_value="Bangladesh"
found=False

for row in rows:
    columns=row.find_elements(By.TAG_NAME,("td"))
    for  column in columns:
        if target_value in column.text:
            print(f"found value:{target_value}")
            found=True
            break
        if found:
            break
        else :f"target value{target_value} not found"


time.sleep(10)