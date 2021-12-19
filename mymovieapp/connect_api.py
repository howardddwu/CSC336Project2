import requests
import json

API_KEY = 'a1a16aff683f4bbbe45ce2192602ce09'

def get_movie_list(list_name):
    url = f"https://api.themoviedb.org/3/movie/{list_name}?api_key={API_KEY}&language=en-US&page=1"
    r = requests.get(url)
    results = json.loads(r.text)["results"]

    movies = []
    for m in results:
        movie_id = m["id"]
        title = m["title"]
        overview = m["overview"]
        poster = m["poster_path"]
        image = f"https://image.tmdb.org/t/p/w342{poster}"
        movie = {
            "movie_id": movie_id,
            "title": title,
            "overview": overview,
            "image": image
        }
        movies.append(movie)
    
    return movies
