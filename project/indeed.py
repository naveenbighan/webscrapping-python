from selenium import webdriver
from bs4 import BeautifulSoup as BS
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException
import pymongo
import pandas as pd
from time import sleep
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
chrome_options.add_argument(f'user-agent={user_agent}')

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 10)

# MongoDB setup
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["job_data"]
job_data_collection = db["job_data_collection"]

jobs_data = []
index = 0
urls = [
    "https://in.indeed.com/jobs?q=software+engineer&l=India",
    "https://in.indeed.com/jobs?q=data+science&l=India",
    "https://in.indeed.com/jobs?q=electrical+engineer&l=India",
    "https://in.indeed.com/jobs?q=hr&l=India",
    "https://in.indeed.com/jobs?q=accountant&l=India",
    "https://in.indeed.com/jobs?q=data+entry&l=India",
    "https://in.indeed.com/jobs?q=office+assistant&l=India",
    "https://in.indeed.com/jobs?q=mechanical+engineer&l=India",
    "https://in.indeed.com/jobs?q=automation+engineer&l=India",
    "https://in.indeed.com/jobs?q=automation+test+engineer&l=India",
    "https://in.indeed.com/jobs?q=sales+executive&l=India",
    "https://in.indeed.com/jobs?q=civil+engineer&l=India",
    "https://in.indeed.com/jobs?q=teacher&l=India",
    "https://in.indeed.com/jobs?q=content+writer&l=India",
    "https://in.indeed.com/jobs?q=video+editor&l=India",
    "https://in.indeed.com/jobs?q=architect&l=India",
    "https://in.indeed.com/jobs?q=logistics&l=India",
    "https://in.indeed.com/jobs?q=business+development+executive&l=India",
    "https://in.indeed.com/jobs?q=associate+manager&l=India"
]

for url in urls:
    print(f"Scraping URL: {url}")

    for page in range(70):  # Adjust the range as needed
        start = page * 10
        page_url = f"{url}&start={start}"

        driver.get(page_url)
        sleep(5)

        html = driver.page_source
        soup = BS(html, 'html.parser')

        jobs = soup.find_all("div", class_="css-hyhnne e37uo190")
        for job in jobs:
            post_name = job.find("h2")
            company_name = job.find("div", class_="css-1qv0295 e37uo190")
            location = job.find("div", class_="css-1p0sjhy eu4oa1w0")
            time = job.find("div", class_="css-1cvvo1b eu4oa1w0")
            summary = job.find("div", class_="css-9446fg eu4oa1w0")

            if post_name:
                index += 1
                driver.execute_script("arguments[0].scrollIntoView(true);", post_name)
                wait.until(EC.presence_of_element_located((By.TAG_NAME, "h2")))

                try:
                    post_name.click()
                    
                    job_details_html = driver.page_source
                    job_soup = BS(job_details_html, 'html.parser')

                    time_text = time.text.strip() if time else "N/A"
                    terms = ["Part-time", "Full-time", "Monday to Friday", "Internship", "Permanent", "Temporary"]
                    print_time = time_text.strip('+23145') if any(term in time_text for term in terms) else "N/A"

                    salary = time_text.strip('abcdefghijklmnopqrstuvwxyz ') if any(term in time_text for term in ["₹", "a year", "a month"]) else "N/A"
                    
                    company_name_text = company_name.text.strip() if company_name else "N/A"
                    location_text = location.text.strip() if location else "N/A"
                    summary_text = summary.text.strip() if summary else "No summary"
                    
                    all_job_data = {
                        "title": post_name.text.strip(),
                        "company-name": company_name_text,
                        "location": location_text,
                        "type": print_time,
                        "salary_package": salary,
                        "company_requirements": summary_text
                    }

                    jobs_data.append(all_job_data)
                    df = pd.DataFrame(jobs_data)
                    df.to_csv("indeed2_jobs.csv", index=False)
                    
                    # Uncomment to insert into MongoDB
                    # job_data_collection.insert_one(all_job_data)

                    print(f"{index}. {post_name.text.strip()}  company name: {company_name_text}  location: {location_text} type: {print_time} salary: {salary} requirement: {summary_text}")
                    
                except StaleElementReferenceException:
                    print(f"Job posting {index} became stale. Skipping...")

sleep(30)

driver.quit()
