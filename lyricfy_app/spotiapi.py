import base64
import json
import urllib2

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

    def __init__(self, apikey):
        self.api_key = apikey

    def get_json(self, tipus, element):
        url = "https://api.spotify.com/v1/search?"
        url += "type=" + tipus + "&"
        url += "q=" + element + "&"
        url += "access_token=" + self.api_key
        f = urllib2.urlopen(url)
        json = f.read()
        f.close()
        return json
