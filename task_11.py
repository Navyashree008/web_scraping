import requests
from bs4 import BeautifulSoup
import json

with open("evry_movie_details.json","r")as f:
    info = json.load(f)

unique_gener = []
for i in range(len(info)):
    for j in range(len(info[i]["gener"])):
        if info[i]["gener"][j] not in unique_gener:
            unique_gener.append(info[i]["gener"][j])


all_gener_info = {}
for i in range(len(unique_gener)):
    all_gener_info[unique_gener[i]] = 0
    for j in range(len(info)):
        if unique_gener[i] in info[j]["gener"]:
            all_gener_info[unique_gener[i]]+= 1 
print(all_gener_info)



