import requests
from bs4 import BeautifulSoup
import json

with open("evry_movie_details.json","r")as f:
    details = json.load(f)

all_dict = {}
def analyse_language_and_directors():
    unique_director = []
    for i in range(len(details)):
        for j in range(len(details[i]['director'])):
            if details[i]['director'][j] not in unique_director:
                unique_director.append(details[i]['director'][j])

    
    for i in range(len(unique_director)):
        
        unique_dict = {}
        for j in range(len(details)):
            if unique_director[i] in details[j]["director"]:
                for lg in range(len(details[j]["language"])):
                    if details[j]["language"][lg] not in unique_dict:
                        unique_dict[details[j]["language"][lg]] = 1
                    else:
                        unique_dict[details[j]["language"][lg]] += 1
                        
        all_dict[unique_director[i] ] = unique_dict
    return all_dict
analyse_language_and_directors()

with open("director_lang_info.json","w")as f:
    json.dump(all_dict,f,indent=4)