import requests
from bs4 import BeautifulSoup

req = requests.get("http://210.70.80.21/~bs109021029/publication.html")
req.encoding = "utf8"
if req.status_code == 200:
    #print(req.text)
    soup = BeautifulSoup(req.text,"lxml")
    #print(soup)
    result1 = soup.find_all("li")
    fp = open("out2.text", "w", encoding="utf8")
    #print(result1)
    #i = 1
    for val in result1:
        text2 = val.text.replace("\n", "")
        text3 = text2.replace(" ","")
        #print(i, val.text)
        #i += 1
        print(text3)
        fp.write(text3 + "\n")
    fp.close()
else:
    print("沒有啦")
