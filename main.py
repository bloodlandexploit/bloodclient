import RestAPI
import BASE_URL
import json
import getcode
import time

main_server = "https://api.blood.land/mining/servers/9"
user_id = "" #miningpool_ID
user_pw = "" #miningpool_PW
secret_key_1 = BASE_URL.secret_key_1
token = RestAPI.getToken(user_id, user_pw)
print(token)
print(BASE_URL.miningurl)
while True:
    getInfo = RestAPI.getInfo(token)
    reportInterval = json.loads(getInfo)['reportInterval']
    timestamp = json.loads(getInfo)['timestamp']
    secret_key_2 = json.loads(getInfo)['secret']
    mo = json.loads(getInfo)['mo']
    mx = json.loads(getInfo)['mx']
    mainwallet = json.loads(getInfo)['user']['mainWalletAddress']
    point = json.loads(getInfo)['user']['point']
    print("unix time", timestamp, "secret_key_2", secret_key_2)
    #code_not_working
    print(code)
    report = RestAPI.report(token, code)
    print(report)
    reportsec = int(reportInterval / 1000)
    time.sleep(reportsec)