import urllib.request
import json
import requests
import schedule
import time
 
def scd():
    with urllib.request.urlopen("https://www.bitmex.com/api/v1/trade?symbol=XBTUSD&count=1&reverse=true") as url:
        data = url.read()
    j = json.loads(data)
    teleurl = "https://api.telegram.org/bot776990016:AAE-x3YRB3Slvh9NiJCa5INpuCBoQHAW9DM/sendMessage"
    print(j[0]["symbol"] + " : " + str(j[0]["price"]))
    params = {'chat_id': '-1001353940838', 'text': j[0]["symbol"]  + " : " + str(j[0]["price"])}   
    res = requests.get(teleurl, params=params)
schedule.every().minute.do(scd)

while 1:
    schedule.run_pending()
    time.sleep(120)