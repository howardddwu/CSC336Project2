import requests
import pandas as pd
import json
# import requests

# API_KEY = 'a1a16aff683f4bbbe45ce2192602ce09'

def get_now_playing():
    url = f"https://api.themoviedb.org/3/movie/now_playing?api_key=a1a16aff683f4bbbe45ce2192602ce09&language=en-US&page=1"
    r = requests.get(url)
    return json.loads(r.text)

