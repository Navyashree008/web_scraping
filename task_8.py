import json
from os import write
from bs4 import BeautifulSoup
import requests

with open("top_movie_list.json","r") as f:
    movies_list = json.load(f)

import os


def creat_json_files():
    # directory = "all_files"
    # parent_dir = "/home/lenovo/Documents/web_scraping"
    # os.chdir(parent_dir)
    # os.makedirs(directory)
    for i in range(len(movies_list)):
        my_url = movies_list[i]['url']
        page = requests.get(my_url)
        soup = BeautifulSoup(page.text,'html.parser')
        
        id = my_url.split("/")
        file_name = id[-2]+".txt"
        path="/home/lenovo/Documents/web_scraping/all_files/"+file_name
        f = open(path,"w")
        f1 = f.write(page.text)
        
        
creat_json_files()   