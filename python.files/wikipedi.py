import requests
from bs4 import BeautifulSoup




url = "https://tr.wikipedia.org/wiki/T%C3%BCrkiye%27nin_en_zengin_100_ailesi_listesi"

html = requests.get(url).content

soup = BeautifulSoup(html, "html.parser")

list = soup.find("li", {"class":"my-content-text"}).find_all("tr")
               
                                                                     #limit = 1 demek sadece 1 tane tr al demektir.
print(list)
'''

count = 0

for tr in list:
    title = tr.find("td", {"class":"titleColumn"}).find("a").text
    year = tr.find("td", {"class":"titleColumn"}).find("span").text.strip("()")     # strip le parantezleri silebilirsin.
    rating = tr.find("td", {"class":"ratingColumn imdbRating"}).find("strong").text
    
    count += 1
    print(f"{count}. movie : {title.ljust(68)}  was produced in {year} and imdb is equal {rating} ")

'''


