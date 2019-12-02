from bs4 import BeautifulSoup
import lxml
import requests
url="https://www.imdb.com/chart/top/"
data=requests.get(url)
soup=BeautifulSoup(data.text,"lxml") 


titulo=[]
score=[]
year=[]
top250=soup.tbody.find_all("tr")
print(len(top250))
for movies in top250:
    #fetches the name of the movie
    nomes=movies.find("td",class_="titleColumn")
    nomes2=nomes.find("a",title_="").text
    titulo.append(nomes2)
#fetches the score of the movie
    rating=movies.find("strong").text
    score.append(rating)
#fetches the year of the movie
    movie_year=movies.find("span",class_="secondaryInfo").text
    year.append(movie_year)


print(titulo)
print(score)
print(year)