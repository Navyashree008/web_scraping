import requests
from bs4 import BeautifulSoup
import json
import os.path
from os import path



def scrape_movie_cast(movie_url):
    allActor_info_list = []
    file_path = "/home/lenovo/Documents/web_scraping/all_files/"+str(movie_url[-10:-1])+".txt"
    print(file_path)
    if os.path.exists(file_path):
        f = open(file_path,"r")
        soup = BeautifulSoup(f,'html.parser')
        # print(soup)
        div = soup.find('div',class_ = 'ipc-sub-grid ipc-sub-grid--page-span-2 ipc-sub-grid--wraps-at-above-l title-cast__grid')
        allActors=soup.select("a[data-testid='title-cast-item__actor']")
        for i in range(len(allActors)):
            dict = {}
            name = allActors[i].text
            name_id = allActors[i]['href'][6:15]
            dict['name'] = name
            dict['name_id'] = name_id
            allActor_info_list.append(dict)
    return allActor_info_list
# print(scrape_movie_cast("https://www.imdb.com//title/tt0048473/"))
  
