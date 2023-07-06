from req import *
from requests import get
def search_for_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = auth_headers(token)
    search_query = f"?q={artist_name}&type=artist&limit=1"

    query_url = url + search_query
    result = get(query_url, headers=headers)
    json_res = json.loads(result.content)["artists"]["items"]
    
    if len(json_res) == 0: 
        print(f"no artist with name of {artist_name} exists")
        return None
    
    return json_res[0]
    
token=token(client_id, client_secret)
res = search_for_artist(token, "gary moore")
print(res)

