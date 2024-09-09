import requests


def fetch_And_Save_Data(url,path):
    r = requests.get(url)
    with open(path,"w")as file:
        file.write(r.text)
        
url="https://timesofindia.indiatimes.com/city/delhi"
fetch_And_Save_Data(url, "data/times.html")


