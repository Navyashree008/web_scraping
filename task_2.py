import json

with open("top_movie_list.json","r") as f:
    list_of_movies = json.load(f)



json_object = {}
# def group_by_year(movies):
# work_list = list_of_movies.copy()

def years():
    unique_year = []
    i = 0
    while i < len(list_of_movies):
        if list_of_movies[i]['year'] not in unique_year:
            unique_year.append(list_of_movies[i]['year'])
        i+=1
    return unique_year

def group_by_year(movies):
    unique_years=years()
    i = 0
    while i < len(unique_years):
        movies_list = []
        j = 0
        while j < len(list_of_movies):
            if unique_years[i] == list_of_movies[j]['year']:
                movies_list.append(list_of_movies[j])
            j+=1
        json_object[unique_years[i]] = movies_list
        i+=1
    return json_object
dictionary = group_by_year(list_of_movies)

with open("year_wise_list.json","w") as f:
    json.dump(dictionary,f,indent= 4)

