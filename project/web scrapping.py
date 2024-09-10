from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from bs4 import BeautifulSoup
import re
import csv


driver = Chrome()


driver.get('http://www.olympedia.org/statistics/medal/country')


year_dd = driver.find_element(By.ID, 'edition_select')
gender_dd = driver.find_element(By.ID, 'athlete_gender')


year_options = year_dd.find_elements(By.TAG_NAME, 'option')
gender_options = gender_dd.find_elements(By.TAG_NAME, 'option')

usa_lst = []


for gender in gender_options[1:]:  
    gender.click()
    gender_val = gender.text
    
    for year in year_options[2:]: 
        year.click()
        year_val = year.text
        
        try:
            
            the_soup = BeautifulSoup(driver.page_source, 'html.parser')
            
            
            head = the_soup.find(href=re.compile('USA'))
            
            
            medal_values = head.find_all_next('td', limit=5)
            val_lst = [x.string for x in medal_values[1:]]
            
        except:
            
            val_lst = ['0' for x in range(4)]
        
        
        val_lst.append(gender_val)
        val_lst.append(year_val)
        
        usa_lst.append(val_lst)


with open('output.csv', 'w', newline='') as output_f:
    output_writer = csv.writer(output_f)
    for row in usa_lst:
        output_writer.writerow(row)



