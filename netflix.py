#Recommends a netflix show/movie for the user based on their inputs

#init
import webbrowser
import pandas as pd
data = pd.read_csv('netflix.csv')

id = data['id'].tolist()
type = data['Type'].tolist()
title = data['Title'].tolist()
country = data['Country'].tolist()
data_added = data['Data Added'].tolist()
release_year = data['Release Year'].tolist()
rating = data['Rating'].tolist()
genre = data['Genre'].tolist()

#Functions
netflix_recs = []

netflix_ratings = ["PG", "PG-13", "R", "TV-14", "TV-MA", "TV-Y7-FV", "TV-Y7", "TV-Y", "TV-G", "G", "UR", "TV-PG"]

movie_genres = ["Documentaries", "Dramas", "Romantic Movies", "Independent Movies", "Thrillers", "Comedies", "Children & Family Movies", "Horror Movies", "Sports Movies",
                "Action & Adventure", "Sci-Fi & Fantasy", "International Movies", "Stand-Up Comedy","LGBTQ Movies", "Music & Musicals",
                "Cult Movies", "Classic Movies", "Faith & Spirituality", "Anime Features", "Anime Series"]

tv_genres = ["Crime TV Shows", "Kids' TV", "TV Action & Adventure", "International TV Shows", "Reality TV", "TV Dramas", "TV Comedies", "British TV Shows", "Docuseries", "TV Horror",
             "TV Sci-Fi & Fantasy", "TV Thrillers", "TV Mysteries", "Romantic TV Shows", "Stand-Up Comedy & Talk Shows","Classic & Cult TV", "Teen TV Shows", "Spanish-Language TV Shows",
             "Science & Nature TV"]
print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
print("Hello! Welcome to our netflix recommender program, we are going to find the right show for you!")

def rec(date):
    print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    pref = input("Are you looking for a movie or a TV Show?: ").upper()
    if pref == "movie".upper():
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("These are all of the movie genres:")
        print(movie_genres)
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    if pref == "tv show".upper():
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("These are all of the tv show genres:")
        print(tv_genres)
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    genre = input("What genre are you looking for?: ").upper()
    print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    netflix_recs.clear()
    country = input("What country do you live in?: ").upper()
    print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    year = input("Do you want to watch a new or old movie/show?: ")
    print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("These are all of the tv show ratings:")
    print(netflix_ratings)
    print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    rating = input("What rating would you like your show/movie to be?: ").upper()
    print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    for index, row in data.iterrows():
        if genre in row["Genre"].upper():
            if pref in row["Type"].upper():
                if year == "new" and int(row["Release Year"]) >= int(date) or year == "old" and int(row["Release Year"]) <= int(date):
                    if country in row["Country"].upper():
                        if rating in row["Rating"].upper():
                            netflix_recs.append(row["Title"])
    if len(netflix_recs) == 0:
        print("Sorry, no matches found. Try switching up your filters.")
        print(netflix_recs)
    else:
        print("Here are your recommendations!: ")
        print(netflix_recs)
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        netflix_recs.clear()

#Main
rec(2000)
