import requests
from bs4 import BeautifulSoup
import json

with open("evry_movie_details.json","r")as f:
    details = json.load(f)



def analyse_movie_lang():
    unique_lang = []
    for i in range(len(details)):
        for j in range(len(details[i]['language'])):
            if details[i]['language'][j] not in unique_lang:
                unique_lang.append(details[i]['language'][j])
    
    languages_details = {}
    for i in range(len(unique_lang)):
        count = 0
        for j in range(len(details)):
            if unique_lang[i] in details[j]['language']:
                count+=1
        languages_details[unique_lang[i]] = count
    return languages_details
analyse_movie_lang()
with open("lang_wise_movie.json","w")as f:
    json.dump(analyse_movie_lang(),f,indent=4)