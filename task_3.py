import json
with open("top_movie_list.json","r") as f:
    list_of_movies = json.load(f)
def years():
    unique_year = []
    i = 0
    while i < len(list_of_movies):
        if list_of_movies[i]['year'] not in unique_year:
            unique_year.append(list_of_movies[i]['year'])
        i+=1
    return unique_year
unique_years = years()
def decades():
    decades_list = []
    i = 0
    while i < len(unique_years):
        a = unique_years[i] % 10
        m = unique_years[i] - a
        if m not in decades_list:
            decades_list.append(m)
        i+=1
    return decades_list
list_of_decades = decades()
list_of_decades.sort()
def group_by_decades():
    decades_dict = {}
    for i in range(len(list_of_decades)):
        movies = []
        for j in range(len(list_of_movies)):
            if list_of_movies[j]['year'] <= list_of_decades[i]+10:
                movies.append(list_of_movies[j])
        decades_dict[list_of_decades[i]] = movies
    return decades_dict 
decades_dictionary = group_by_decades()
with open("decade_wise_list.json","w") as f:
    json.dump(decades_dictionary,f,indent=4)

