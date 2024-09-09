import requests
from bs4 import BeautifulSoup

headers=({"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"})
url="https://www.amazon.in/s?k=iphone&crid=1MX3WYDF5K1OC&sprefix=iphone%2Caps%2C237&ref=nb_sb_noss_1"
r= requests.get(url,headers=headers)
Soup= BeautifulSoup(r.text,"html.parser")
print(Soup.prettify())

with open("demo.html","w") as f:
    f.write(r.text)