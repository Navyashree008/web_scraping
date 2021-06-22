
import time
import random
import requests
from bs4 import BeautifulSoup
import json

def conver_to_int(a):
    store = ""
    i = 0
    while i < len(a):
        if a[i] == "(" or a[i] ==")" or a[i] == ".":
            i+=1
            continue
        store+=a[i]
        i+=1
    n = int(store)
    return n


def scrape_top_list():
    jaon_list = []
    url = "https://www.imdb.com/india/top-rated-indian-movies/"
    page = requests.get(url)
    soup = BeautifulSoup(page.text,'html.parser') #from this we will get whole webpage
    main_div = soup.find('div', class_ = 'lister')
    main_tbody = main_div.find('tbody', class_ = 'lister-list')
    trs = main_tbody.find_all("tr")
    for tr in trs:
        dict1 = {}
        posi_name_year = tr.find("td",class_ = "titleColumn").get_text() #this is foe name,year,rank
        movie_url = "https://www.imdb.com/"+tr.find("td",class_ = "titleColumn").a["href"]
        td_list = posi_name_year.split("\n")
        list1=[]
        i=0
        while i < len(td_list):
            a = td_list[i].strip()
            list1.append(a)
            i+=1
        r=tr.find("td",class_ = "ratingColumn imdbRating").get_text()
        rating =float(r) #converting rating to float
        position = conver_to_int(list1[1])
        year = conver_to_int(list1[3])
        dict1['name'] = list1[2]
        dict1['position'] = position
        dict1['year'] = year
        dict1['rating'] = rating
        dict1['url'] = movie_url
        jaon_list.append(dict1)
        r = random.randint(1, 3)
        time.sleep(r)
    return jaon_list
list = scrape_top_list()    

with open("top_movie_list.json","w") as f:
    json.dump(list,f,indent=4)    
    




