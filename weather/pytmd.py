import requests
import datetime

class Place(object):
    def __init__(self,province=None, amphoe=None,tambon=None,region=None,lat=None,lon=None):
        self.region = region
        self.province = province
        self.amphoe = amphoe
        self.tambon = tambon
        self.lon = lon
        self.lat = lat
    def to_json(self):
        self.data={}
        if self.province is not None:
            self.data['province'] = self.province
        if self.amphoe is not None:
            self.data['amphoe'] = self.amphoe
        if self.tambon is not None:
            self.data['tambon'] = self.tambon
        return self.data
    def at_to_json(self):
        return {"lat":self.lat, "lon":self.lon}
    def region_to_json(self):
        return {"region":self.region}

def day(name):
    if name is "today":
        return datetime.date.today().strftime("%Y-%m-%d")
    elif name is "tomorrow":
        return (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")

def region2code(name):
  if name in ["ภาคกลาง"]:
    return "C"
  elif name in ["ภาคเหนือ"]:
    return "N"
  elif name in ["ภาคตะวันออกเฉียงเหนือ","ภาคอีสาน"]:
    return "NE"
  elif name in ["ภาคตะวันออก"]:
    return "E"
  elif name in ["ภาคใต้"]:
    return "S"
  elif name in ["ภาคตะวันตก"]:
    return "W"

th_cond={
    1 : "ท้องฟ้าแจ่มใส",
    2 : "มีเมฆบางส่วน",
    3 : "เมฆเป็นส่วนมาก",
    4 : "มีเมฆมาก",
    5 : "ฝนตกเล็กน้อย",
    6 : "ฝนปานกลาง",
    7 : "ฝนตกหนัก",
    8 : "ฝนฟ้าคะนอง",
    9 : "อากาศหนาวจัด",
    10 : "อากาศหนาว",
    11 : "อากาศเย็น",
    12 : "อากาศร้อนจัด"
}
en_cond={
    1:"Clear",
    2:"Partly cloudy",
    3:"Cloudy",
    4:"Overcast",
    5:"Light rain",
    6:"Moderate rain",
    7:"Heavy rain",
    8:"Thunderstorm",
    9:"Very cold",
    10:"Cold",
    11:"Cool",
    12:"Very hot"
}
def cond(t,lang="th"):
  global th_cond,en_cond
  if lang is "th":
    return th_cond[t]
  else:
    return en_cond[t]

class PyTMD(object):
    def __init__(self,key,plce):
        self.place=plce
        self.headers = {
            'accept': "application/json",
            'authorization': "Bearer "+key,
        }
    def forecast_daily(self,date,duration=1,fields="tc_max,tc_min,tc,rh,cond,rain",type_w="place"):
        self.data={
            "date":date,
            "duration":duration,
            "fields":fields
        }
        self.querystring = {}
        self.url = str()
        if type_w is "place":
          self.url = "https://data.tmd.go.th/nwpapi/v1/forecast/location/daily/place"
          self.querystring = {**self.place.to_json() , **self.data}
        elif type_w is "at":
          self.url = "https://data.tmd.go.th/nwpapi/v1/forecast/location/daily/at"
          self.querystring = {**self.place.at_to_json() , **self.data}
        elif type_w is "region":
          self.url = "https://data.tmd.go.th/nwpapi/v1/forecast/location/daily/region"
          self.querystring = {**self.place.region_to_json() , **self.data}
        self.response = requests.request("GET",
        self.url, 
        headers=self.headers,
        params=self.querystring
        )
        return self.response.json()['WeatherForecasts']
    def hourly_data(self):
        self.response=requests.request("GET", "https://data.tmd.go.th/nwpapi/v1/forecast/location/hourly", headers=self.headers)
        return self.response.json()
    def forecast_hour(self,hour,duration=1,fields="tc_max,tc_min,tc,rh,cond,rain",type_w="place"):
        self.data={
            "hour":hour,
            "duration":duration,
            "fields":fields
        }
        self.querystring = {}
        self.url = str()
        if type_w is "place":
          self.url = "https://data.tmd.go.th/nwpapi/v1/forecast/location/hourly/place"
          self.querystring = {**self.place.to_json() , **self.data}
        elif type_w is "at":
          self.url = "https://data.tmd.go.th/nwpapi/v1/forecast/location/hourly/at"
          self.querystring = {**self.place.at_to_json() , **self.data}
        elif type_w is "region":
          self.url = "https://data.tmd.go.th/nwpapi/v1/forecast/location/hourly/region"
          self.querystring = {**self.place.region_to_json() , **self.data}
        self.response = requests.request("GET",
        self.url, 
        headers=self.headers,
        params=self.querystring
        )
        return self.response.json()
    def change_place(self,place):
        self.place = place