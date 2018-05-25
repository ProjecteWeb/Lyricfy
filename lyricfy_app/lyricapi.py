import json

import requests

api_key = "PmvrVrL3R09mqFbpdsiRDzXikhoiJh14aXBMMiK4CFSz9GPlmOH6nyRNPaxqv0kd"


def get_json(name, artist):
    url = "https://orion.apiseeds.com/api/music/lyric/"
    url += artist
    url += "/" + name
    url += "?apikey=" + api_key
    json = requests.get(url).content
    return json


def get_lyrics(name, artist):
    lyric_json = json.loads(get_json(name, artist))
    return lyric_json["result"]["track"]["text"]
