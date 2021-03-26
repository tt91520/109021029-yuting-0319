import requests
from bs4 import BeautifulSoup

req = requests.get("http://210.70.80.21/~bs109021029/publication.html")
req.encoding = "utf8"
if req.status_code == 200:
    #print(req.text)
    soup = BeautifulSoup(req.text,"lxml")
    print(soup)
    result1 = soup.find_all("li")
    print(result1)
else:
    print("沒有啦")
