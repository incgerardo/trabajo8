from bs4 import BeautifulSoup
import requests

url="https://proxy.scrapeops.io/v1/?api_key=443ee665-27e9-4dcd-bf97-34c3c5dd9b2f&url=https://www.thecrag.com/en/climbing/germany/"	#nombre de la pagina

r=requests.get(url)
print(r.status_code)

soup = BeautifulSoup(r.content,"html.parser")		#transforma el html en un árbol de objetos

lis = soup.find_all('li', class_='dropdown-submenu.href')

for li in lis:
    print(li)