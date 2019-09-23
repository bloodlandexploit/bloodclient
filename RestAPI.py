import requests
import json
import BASE_URL

s = requests.sessions.Session()
headers = {'Accept': 'application/json', 'Content-Type': 'application/json; charset=utf-8', 'Expect':'100-continue'}

def getToken(user_id, user_pw):
    data = json.dumps({"id":user_id,"password":user_pw,"secret":BASE_URL.secret_key_1})
    req = requests.models.Request('POST', BASE_URL.tokenurl, data=data, headers=headers)
    prepped = req.prepare()
    resp = s.send(prepped)
    token = json.loads(resp.text)['token']
    return token

def getInfo(token):
    data = json.dumps({"token":token,"secret":BASE_URL.secret_key_1,"lang":"kr"})
    req = requests.models.Request('POST', BASE_URL.infourl, data=data, headers=headers)
    prepped = req.prepare()
    resp = s.send(prepped)
    return resp.text

def report(token, code):
    data = json.dumps({"hashrate":0.0,"token":token,"secret":BASE_URL.secret_key_1,"code":code})
    req = requests.models.Request('POST', BASE_URL.reporturl, data=data, headers=headers)
    prepped = req.prepare()
    resp = s.send(prepped)
    return resp.text