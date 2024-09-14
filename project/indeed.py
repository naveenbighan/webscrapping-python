from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as BS
from selenium.webdriver.support.wait import WebDriverWait 
from selenium.common.exceptions import StaleElementReferenceException
import pymongo
import ssl
import pandas as pd
from time import sleep
from selenium.webdriver.support import expected_conditions as EC




driver = webdriver.Chrome()
wait=WebDriverWait(driver,500)


client=pymongo.MongoClient("mongodb://localhost:27017/")
db=client["job_data"]
job_data_collection=db["job_data_collection"]

jobs_data=[]
index=0
web_pages=int("eneter number of pages : ")
for page in range(web_pages):
    start=web_pages*10
 
    driver.get(f"https://in.indeed.com/jobs?q=&l=India&start={start}&vjk=4fc71573088824d8")
    sleep(5)
    
    html= driver.page_source
    soup=BS(html,'html.parser')

    jobs=soup.find("div",class_="css-hyhnne e37uo190")
    if jobs:
        
        post_names = driver.find_elements(By.TAG_NAME,"h2")
        
        
        company_names=jobs.find_all("div",class_="css-1qv0295 e37uo190")
        locations=jobs.find_all("div",class_="css-1p0sjhy eu4oa1w0")
        timings=jobs.find_all("div",class_="css-1cvvo1b eu4oa1w0")
        summaries=jobs.find_all("div",class_="css-9446fg eu4oa1w0")


        
        for post_name,company_name,location,time,summary in zip(post_names,company_names,locations,timings,summaries):
            
            index+=1
            
            
            driver.execute_script("arguments[0].scrollIntoView(true);", post_name)
        
            wait.until(EC.presence_of_element_located((By.TAG_NAME, "h2")))
            try:
                post_name.click()
                
        
                job_details_html = driver.page_source
                job_soup = BS(job_details_html, 'html.parser')
                
                
                
                
                
                time=time.text.strip()
                
                terms = ["Part-time", "Full-time", "Monday to Friday", "Internship", "Permanent", "Temporary"]
                
                if any(term in time for term in terms):
                    print_time=time.strip('+23145')
                else:
                    print_time="N/A"
                    
                    
                if f"{range(1000,5000000)}" in time or "₹" in time or "a year" in time or "a month" in time :
                    salary=time.strip('abcdefghijklmnopqrstuvwxyz ')
                else:
                    salary="N/A" 
                if company_name:
                    company_name=company_name.text.strip()
                if location:
                    location=location.text.strip()
                
                
                if summary:
                    summary=summary.text.strip()
                else:
                    summary="No summary"
                
                
                all_job_data={
                    "title":post_name.text.strip(),
                    "company-name":company_name,
                     "location":location,
                     "type":print_time,
                     "salary_package":salary,
                     "company_requirements":summary
                    
                }    
                
                #want add all data in csv
                jobs_data.append(all_job_data)
                df =pd.DataFrame(jobs_data)
                df.to_csv("indeed1_jobs.csv", index=False)
                
                # want to add all data in database in mongodb
                
                # if jobs_data:
                #     job_data_collection.insert_one(all_job_data)
                    
                

                print(f"{index}. {post_name.text.strip()}  company name : {company_name}  location : {location} type : {print_time} salary : {salary} requirement : {summary}")
                
            except StaleElementReferenceException:
                            print(f"Job posting {index} became stale. Skipping...")

    

sleep(30)


 