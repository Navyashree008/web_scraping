import requests
from bs4 import BeautifulSoup
import json

with open("all_details.json","r")as f:
    details = json.load(f)

def analyse_co_actors():
    