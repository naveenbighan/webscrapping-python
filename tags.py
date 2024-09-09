import requests
from bs4 import BeautifulSoup

with open("sample.html","r") as f:
    Html_doc=f.read()
    

Soup= BeautifulSoup(Html_doc, "html.parser")
print(Soup.prettify())

ultag= Soup.new_tag("ul")

litag= Soup.new_tag("li")
litag.string= "Home"
ultag.append(litag)




litag2= Soup.new_tag("li")
litag2.string="About"
ultag.append(litag2)

Soup.html.body.insert(0,ultag)
with open("modified.html", "w") as file:
    file.write(str(Soup))