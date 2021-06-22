import requests
from bs4 import BeautifulSoup
import json
from task_4 import one_movie_detail
import random
import time

with open("top_movie_list.json","r") as f:
    list_of_movies = json.load(f)

all_movie_detail = []
def every_movie_detail():
    for i in range(len(list_of_movies)):
        url = list_of_movies[i]['url']
        movie = list_of_movies[i]['name']
        movie_detail = one_movie_detail(url,movie)
        all_movie_detail.append(movie_detail)
        r = random.randint(1, 3)
        time.sleep(r)
        help(random.randint)
    return all_movie_detail
every_movie_detail()

with open("evry_movie_details.json","w") as f:
    json.dump(all_movie_detail,f,indent=4)
    
    