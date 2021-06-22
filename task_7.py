import requests
from bs4 import BeautifulSoup
import json

with open("evry_movie_details.json","r")as f:
    details = json.load(f)



def analyse_movies_directors():
    unique_director = []
    for i in range(len(details)):
        for j in range(len(details[i]['director'])):
            if details[i]['director'][j] not in unique_director:
                unique_director.append(details[i]['director'][j])
    
    director_details = {}
    for i in range(len(unique_director)):
        count = 0
        for j in range(len(details)):
            if unique_director[i] in details[j]['director']:
                count+=1
        director_details[unique_director[i]] = count
    return director_details
analyse_movies_directors()
with open("director_wise_movie.json","w")as f:
    json.dump(analyse_movies_directors(),f,indent=4)