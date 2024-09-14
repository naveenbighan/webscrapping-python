from bs4 import BeautifulSoup as BS
import requests
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time,pymongo
import pandas as pd

client=pymongo.MongoClient("mongodb://localhost:27017/")
db=client["imbd_data"]
imbd_data_collection=db["imbd_data_collection"]


driver=webdriver.Chrome()
driver.maximize_window()
wait = WebDriverWait(driver,10)

driver.get("https://www.imdb.com/chart/top/")
html= driver.page_source

Soup=BS(html,"html.parser")

movies= Soup.find("ul",class_="ipc-metadata-list ipc-metadata-list--dividers-between sc-a1e81754-0 dHaCOW compact-list-view ipc-metadata-list--base")


movie_data=[]
for movie in movies:
    name= movie.find("h3")
    movie_year=movie.find("div",class_="sc-b189961a-7 btCcOY cli-title-metadata")
    rating=movie.find("span",class_="sc-b189961a-1 kcRAsW")
    
    if movie_year:
        first_div= movie_year.find("span")
    
    if rating:
        ratings_f_div=rating.find("span")
    print(f"Movie: {name.get_text()} , Movie year : {first_div.text} , rating : {ratings_f_div.text}")

    movie_dict={"Movie": name.get_text(),
        "Year": first_div.text,
        "Rating": ratings_f_div.text}
    # movie_data.append(movie_dict)

if movie_data:   
   imbd_data_collection.insert_many(movie_dict)

df =pd.DataFrame(movie_data)
df.to_csv("topratingmovies.csv", index=False)
    

        

           


time.sleep(10)
driver.quit()
    
    
        
