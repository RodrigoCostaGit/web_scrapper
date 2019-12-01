from bs4 import BeautifulSoup
import lxml
import requests
url="https://www.imdb.com/chart/top/"
data=requests.get(url)
soup=BeautifulSoup(data.text,"lxml") 
# print(soup.prettify())
# top250=soup.find_all("tbody",class_="lister-list")
# top250=soup.find_all("tr")

titulo=[]
score=[]
top250=soup.tbody.find_all("tr")
print(len(top250))
for movies in top250:
    vari=movies.find("td",class_="titleColumn")
    vari2=vari.find("a",title_="").text
    # vari=movies.find("a",href_="img alt")
    titulo.append(vari2)
print(titulo)

