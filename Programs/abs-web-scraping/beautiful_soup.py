import bs4
import requests
res = requests.get("https://www.amazon.com/Automate-Boring-Stuff-Python-2nd/dp/1593279922/ref=sr_1_3?crid=2XNOZPN2PCY51&dchild=1&keywords=automate+the+boring+stuff+with+python&qid=1632855401&sprefix=automate+the+bor%2Caps%2C212&sr=8-3")

print(res.status_code)

soup = bs4.BeautifulSoup(res.text, "html.parser")
soup.select("//*[@id="newBuyBoxPrice"]")