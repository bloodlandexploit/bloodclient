import urllib.request
import json
import random
import requests


def ConnectEntry(main_server):
    json_data = requests.get(main_server).json()
    get_secret_key_1 = json_data['secret']
    get_name = len(json_data['names'])
    get_random = random.randint(0, get_name-1)
    get_apiUrl = json_data['apiUrls'][get_random]
    get_miningUrl = json_data['minerUrls'][get_random]
    get_code = json_data['code']
    return get_secret_key_1, get_apiUrl, get_miningUrl, get_code
