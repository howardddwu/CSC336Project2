import requests
import pandas as pd
import json
from .models import Movies

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
        backdrop = m["backdrop_path"]
        image = f"https://image.tmdb.org/t/p/w342{backdrop}"
        movie = {
            "movie_id": movie_id,
            "title": title,
            "overview": overview,
            "image": image
        }
        movies.append(movie)
    
    return movies



# for i in range(1, 472):
#     response = requests.get("https://api.themoviedb.org/3/movie/top_rated?api_key=<api_key>&language=en-US&page={}".format(i))
#     temp_df = pd.DataFrame(response.json()["results"])[['id','title','overview','popularity','release_date','vote_average','vote_count']]
#     data.append(temp_df, ignore_index=False)


# movies = models.Movies.objects.all()
# data = pd.DataFrame()
# for m in movies:
#     m.movie_id
#     r = requests.get(f"https://api.themoviedb.org/3/movie/{m.movie_id}/credits?api_key={API_KEY}&language=en-US")
#     temp_df = pd.DataFrame(r.json()["cast"])[['id', 'name', 'profile_path', 'character']]
#     data = data.append(temp_df, ignore_index=True)
# print(data)