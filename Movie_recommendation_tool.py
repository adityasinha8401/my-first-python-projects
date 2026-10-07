data1=[{"title": "Inception", "genre": "Sci-Fi", "year": 2010, "rating": 8.8},
    {"title": "Interstellar", "genre": "Sci-Fi", "year": 2014, "rating": 8.6},
    {"title": "The Dark Knight", "genre": "Action", "year": 2008, "rating": 9.0},
    {"title": "Mad Max: Fury Road", "genre": "Action", "year": 2015, "rating": 8.1},
    {"title": "Parasite", "genre": "Thriller", "year": 2019, "rating": 8.5},
    {"title": "Get Out", "genre": "Thriller", "year": 2017, "rating": 7.8},
    {"title": "Superbad", "genre": "Comedy", "year": 2007, "rating": 7.6},
    {"title": "The Grand Budapest Hotel", "genre": "Comedy", "year": 2014, "rating": 8.1}
]

print("=====WELCOME TO THE MOVIE RECOMMENDER SYSTEM======")
print("Available Genres: Action, Comedy, Drama, Horror, Romance, Sci-Fi, Thriller")
user_genre=input("Enter your preffered genre from the above list:").lower()
print("\nEra Options:")
print("1. Classic (Before 2015)")
print("2. Modern (2015 and After)")
user_era=input("Enter your Preferred Era (1 or 2):").strip()
recommended_movies=[]
for movie in data1:
    if movie["genre"].lower() == user_genre:
        if user_era=="1" and movie["year"]<2015:
            recommended_movies.append(movie)
        elif user_era=="2" and movie["year"]>=2015:
            recommended_movies.append(movie)
num_movies=len(recommended_movies)
for i in range(num_movies):
    for j in range(0,num_movies-i-1):
        if recommended_movies[j]["rating"]<recommended_movies[j+1]["rating"]:
            recommended_movies[j],recommended_movies[j+1]=recommended_movies[j+1],recommended_movies[j]
print('='*40)
print("       RECOMMENDED MOVIES       ")
print('='*40)
if len(recommended_movies)==0:
    print("No Movies Found Matching Your Preferences.")
else:
    print(f"Found {len(recommended_movies)} Movies Matching Your Preferences")
    for idx, movie in enumerate(recommended_movies, 1):
            print(f"{idx}. {movie['title']} ({movie['year']})")
            print(f"   Rating: {movie['rating']}/10")
            print(f"   Genre: {movie['genre']}\n")
print("="*40)