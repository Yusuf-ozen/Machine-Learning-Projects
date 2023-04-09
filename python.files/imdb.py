import requests
from bs4 import BeautifulSoup




url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

html = requests.get(url).content

soup = BeautifulSoup(html, "html.parser")

list = soup.find("tbody", {"class" : "lister-list"}).find_all("tr", limit=40)   # class ı lister-list olan tbody i getir demektir. 
                                                                                #limit = 1 demek sadece 1 tane tr al demektir.
'''
count = 0

for tr in list:
    title = tr.find("td", {"class":"titleColumn"}).find("a").text
    year = tr.find("td", {"class":"titleColumn"}).find("span").text.strip("()")     # strip le parantezleri silebilirsin.
    rating = tr.find("td", {"class":"ratingColumn imdbRating"}).find("strong").text
    
    count += 1
    print(f"{count}. movie : {title.ljust(68)}  was produced in {year} and imdb is equal {rating} ")  # baslık için 50 karakterlik bir alan kaplar.


'''
print(list)

