# pip install pyowm
import pyowm
import json
import pytemperature
from datetime import datetime

owm = pyowm.OWM('6f846f85e39da4936de30f30525db8b9',language='th')
def get_weather_now(place:str):
    global owm
    observation = owm.weather_at_place(place)
    w = observation.get_weather()
    return w

statusall={"Mist":"มีหมอก","Clouds":"มีเมฆมาก"}
def status(s):
    global statusall
    if s in list(statusall.keys()):
        return statusall[s]
    else:
        return s

def temp_now(j):
    now = datetime.now()
    t="""
    สภาพอากาศปัจจุบัน เวลา {time} นาฬิกา
    มีอุณหภูมิ {temp} องศาเซลเซียส
    สภาพอากาศ{status}
    """.format(time=now.strftime("%H:%M"),status=j["detailed_status"]
    ,temp=int(pytemperature.k2c(j["temperature"]["temp"])))
    return t
def temp_future(day,t):
    pass
def get_txt(place:str,d:str,t:str=None):
    """
    place : ชื่อสถานที่
    t : เวลา
    """
    if d=='now' and t==None:
        wm = json.loads(get_weather_now(place).to_JSON())
        print(temp_now(wm))
    elif d=='tomorrow':
        pass

get_txt("Nong Khai,TH","now")