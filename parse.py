import json
import requests
from pprint import pprint
url = 'https://api.themoviedb.org/3/movie/popular?api_key=131783423dfc5d2cb752bba2d8da456e&language=ko-KR&page='

# response1 = requests.get(url+'1')
# response2 = requests.get(url+'2')
# response = response1.json().get('results') + response2.json().get('results')
# pprint(response)

datas = []
for i in range(1, 251):
    response = requests.get(url+f'{i}').json().get("results")
    for res in response:
        del res["original_language"]
        del res["backdrop_path"]
        del res["original_title"]
        del res["adult"]
        del res["video"]
        if not res.get("release_date"):
            print(res["title"])
            continue
        if not res.get("poster_path"):
            continue

        data = {}
        data["model"] = "movies.movie"
        data["fields"] = res
        datas.append(data)


with open('datas.json', 'w', encoding='utf8') as f:
    json.dump(datas, f, indent=2, ensure_ascii = False)

