import json
import requests
from pprint import pprint

from requests import api

url = 'https://api.themoviedb.org/3/movie/popular?api_key=131783423dfc5d2cb752bba2d8da456e&language=ko-KR&page='

url2 = 'https://api.themoviedb.org/3/movie/'
url3 = 'https://api.themoviedb.org/3/person/'
api_key = '?api_key=131783423dfc5d2cb752bba2d8da456e&language=ko-KR'


datas = []
for i in range(1, 51):
    response = requests.get(url+f'{i}').json().get("results")
    for res in response:
        if not res.get("release_date"):
            # print(res["title"])
            continue
        if not res.get("poster_path"):
            continue
        del res["original_language"]
        del res["backdrop_path"]
        del res["original_title"]
        del res["adult"]
        del res["video"]
        # print(res.get("id"))
        response_credit = requests.get(url2+f'{res.get("id")}/'+'credits'+api_key).json().get("cast")
        response_credit1 = requests.get(url2+f'{res.get("id")}/'+'credits'+api_key).json().get("crew")

        if response_credit:
            if len(response_credit) > 1:
                if response_credit[0] and response_credit[1]:
                    res["actors"] = [{
                                        "id": response_credit[0].get("id"),
                                        "name": response_credit[0].get("name"),
                                    },
                                    {
                                        "id": response_credit[1].get("id") , 
                                        "name": response_credit[1].get("name")
                                    }]
                response_film1 = requests.get(url3+f'{response_credit[0].get("id")}/'+'movie_credits'+api_key).json().get("cast")
                response_film2 = requests.get(url3+f'{response_credit[1].get("id")}/'+'movie_credits'+api_key).json().get("cast")

                if response_film1:
                    rr1 = sorted(response_film1, key=(lambda x: x['vote_average']))
                    if len(rr1) > 1:
                        res.get("actors")[0]["filmography"] = [{
                                                                "id": rr1[-1].get("id"),
                                                                "title": rr1[-1].get("title"),
                                                                "vote_average": rr1[-1].get("vote_average"),
                                                                "release_date": rr1[-1].get("release_date"),
                                                                "poster_path": rr1[-1].get("poster_path")
                                                                },
                                                                {
                                                                "id": rr1[-2].get("id"),
                                                                "title": rr1[-2].get("title"),
                                                                "vote_average": rr1[-2].get("vote_average"),
                                                                "release_date": rr1[-2].get("release_date"),
                                                                "poster_path": rr1[-2].get("poster_path")
                                                                }]
                if response_film2:
                    rr2 = sorted(response_film2, key=(lambda x: x['vote_average']))
                    if len(rr2) > 1:
                        res.get("actors")[1]["filmography"] = [{
                                                                "id": rr2[-1].get("id"),
                                                                "title": rr2[-1].get("title"),
                                                                "vote_average": rr2[-1].get("vote_average"),
                                                                "release_date": rr2[-1].get("release_date"),
                                                                "poster_path": rr2[-1].get("poster_path")
                                                                },
                                                                {
                                                                "id": rr2[-2].get("id"),
                                                                "title": rr2[-2].get("title"),
                                                                "vote_average": rr2[-2].get("vote_average"),
                                                                "release_date": rr2[-2].get("release_date"),
                                                                "poster_path": rr2[-2].get("poster_path")
                                                                }]
        if response_credit1:
            for i in response_credit1:
                # print(i.get("job"))
                if i.get("job") == "Director":
                    # pprint(i.get("name"))
                    res["Director"] = {
                        "id": i.get("id"),
                        "name": i.get("name")
                    }
            if res.get("Director"):
                response_film = requests.get(url3+f'{res.get("Director").get("id")}/'+'movie_credits'+api_key).json().get("cast")
                if response_film:
                        rr = sorted(response_film, key=(lambda x: x['vote_average']))
                        if len(rr) > 1:
                            res.get("Director")["filmography"] = [{
                                                                    "id": rr[-1].get("id"),
                                                                    "title": rr[-1].get("title"),
                                                                    "vote_average": rr[-1].get("vote_average"),
                                                                    "release_date": rr[-1].get("release_date"),
                                                                    "poster_path": rr[-1].get("poster_path")
                                                                    },
                                                                    {
                                                                    "id": rr[-2].get("id"),
                                                                    "title": rr[-2].get("title"),
                                                                    "vote_average": rr[-2].get("vote_average"),
                                                                    "release_date": rr[-2].get("release_date"),
                                                                    "poster_path": rr[-2].get("poster_path")
                                                                    }]



        data = {}
        data["model"] = "movies.movie"
        data["fields"] = res
        datas.append(data)


with open('datas.json', 'w', encoding='utf8') as f:
    json.dump(datas, f, indent=2, ensure_ascii = False)