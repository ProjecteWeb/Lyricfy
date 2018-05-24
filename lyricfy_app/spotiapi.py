import base64
import json

import requests

client_id = "081b299e957a4608b9567f7d6987962c"
client_secret = "82a91d1c0b224db2be316d3e5311cc4e"

def encoded_clientid(clientid, clientsecret):
    return base64.b64encode(clientid + ":" + clientsecret)


def get_apikey():
    url = "https://accounts.spotify.com/api/token"
    headers = {"Authorization": "Basic " + encoded_clientid(client_id, client_secret)}
    data = [('grant_type', 'client_credentials'), ]
    r = requests.post(url, headers=headers, data=data)
    rdict = json.loads(r.text)
    return rdict['access_token']


class SpotifyAPI(object):
    limit = 10

    def __init__(self):
        self.api_key = get_apikey()

    def get_json(self, element, tipus):
        url = "https://api.spotify.com/v1/search?"
        url += "type=" + tipus + "&"
        url += "q=" + element + "&"
        url += "access_token=" + self.api_key
        # f = urllib2.urlopen(url)
        json = requests.get(url).content
        # f.close()
        return json

    def get_song_list(self, name):
        song_list = []
        songjson = json.loads(self.get_json(name, "track"))
        total_tracks = songjson["tracks"]["total"]
        for x in range(0, self.limit):
            song = []
            if x < total_tracks:
                song.append(songjson["tracks"]["items"][x]["album"]["name"])
                song.append(songjson["tracks"]["items"][x]["artists"][0]["name"])
                song.append(songjson["tracks"]["items"][x]["name"])
                song_list.append(song)
        return song_list
