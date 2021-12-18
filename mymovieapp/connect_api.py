import requests
import pandas as pd
# import requests

API_KEY = 'a1a16aff683f4bbbe45ce2192602ce09'

data = pd.DataFrame()
for i in range(1,473):
    response = requests.get(f"https://api.themoviedb.org/3/movie/top_rated?api_key={API_KEY}&language=en-US&page={i}")
    temp_df = pd.DataFrame(response.json()["results"])[[   
        'id',
        'title',
        'overview', 
        'backdrop_path', 
        'poster_path', 
        'release_date', 
        'vote_average'
    ]]
    data = data.append(temp_df, ignore_index=True)

data.to_csv("movie_data.csv", index=False)
