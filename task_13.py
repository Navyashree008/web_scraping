from ast import fix_missing_locations
import json
from bs4 import BeautifulSoup
import requests
from task_12 import scrape_movie_cast
# import os
import os.path
from os import path
with open("top_movie_list.json","r") as f:
    movies_list = json.load(f)




def one_movie_detail():
    all = []
    folder_to_work = "all_files"
    list_of_files = os.listdir(folder_to_work)
    for i in range(len(list_of_files)):
        print(i)
        url = movies_list[i]['url']
        movie_details = {}
        page = requests.get(url)
        soup = BeautifulSoup(page.text,'html.parser')
        main_div = soup.find('div',class_ = 'ipc-metadata-list-item__content-container') #director name
        ul = main_div.find('ul',class_='ipc-inline-list ipc-inline-list--show-dividers ipc-inline-list--inline ipc-metadata-list-item__list-content baseAlt')
        li = main_div.find('li',class_='ipc-inline-list__item')
        find_a=li.find_all("a") 
        director = [d.get_text() for d in find_a]
        countries = soup.select('li[data-testid="title-details-origin"]')
        for c in countries:
            countries_ul = c.find_all('li',class_="ipc-inline-list__item")
            country_list = []
            for li in countries_ul:
                c_n=li.a.text
                country_list.append(c_n)
        
        languages = soup.select('li[data-testid="title-details-languages"]')
        for l in languages:
            lnguages_ul = l.find_all('li',class_="ipc-inline-list__item")
            language_list = []
            for li in lnguages_ul:
                l_n=li.a.text
                language_list.append(l_n)
        
        poster_div = soup.select('div[data-testid="hero-media__poster"]')
        for k in poster_div:
            poster = k.find('a',class_='ipc-lockup-overlay ipc-focusable')['href']
        poster_url = "https://www.imdb.com"+poster
        bio = soup.find('span',class_ = 'GenresAndPlot__TextContainerBreakpointXL-cum89p-4 liTOue').text
        runtime_ul = soup.find('ul',class_='ipc-inline-list ipc-inline-list--show-dividers TitleBlockMetaData__MetaDataList-sc-12ein40-0 dxizHm baseAlt')
        runtime_lis = runtime_ul.find_all('li',class_ = 'ipc-inline-list__item')
        z=0
        # print(len(runtime_lis))
        for m in runtime_lis:
            if z == len(runtime_lis) - 1:
                runtime =  m.text 
            z+=1
        t_list = []
        t = runtime.split()
        for k in range(len(t)):
            if "h" in t[k]:
                a = t[k].replace("h","")
                t_list.append(a)
            elif "min" in t[k]:
                a = t[k].replace("min","")
                t_list.append(a)
        con = []
        for j in range(len(t_list)):
            h = int(t_list[j])
            con.append(h)
        if len(con) == 2:
            time_add = con[0]*60 +con[1]
            time = str(time_add)+"min"
        else:
            time_add = con[0]*60 
            time = str(time_add)+"min"

        gener_lis = soup.select('li[data-testid="storyline-genres"]')
        for z in gener_lis:
            gener = z.find_all('a',class_ = 'ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link')
        list_of_gener = [g.get_text() for g in gener]

        cast_info = scrape_movie_cast(url)

        movie_details['name'] = movies_list[i]['name']
        movie_details['director'] = director
        movie_details['country'] = country_list
        movie_details['language'] = language_list
        movie_details['poster_url'] = poster_url
        movie_details['Bio'] = bio
        movie_details['runtime'] = time 
        movie_details['gener'] = list_of_gener
        movie_details['cast'] = cast_info
        all.append(movie_details)
    return all
    # break
a = one_movie_detail()
with open("all_details.json","w")as f:
    json.dump(a,f,indent=4)


