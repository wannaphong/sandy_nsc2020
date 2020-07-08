# -*- coding: utf-8 -*-
from .pytmd import *
from pythainlp.tag.named_entity import ThaiNameTagger
from pythainlp.corpus import provinces
from nltk.tokenize import RegexpTokenizer
from difflib import get_close_matches
from pysandy import getprovince,getdistrict
key="" # ใส่  Access Tokens ที่นี่ โดยเอามาจาก https://data.tmd.go.th/nwpapi/home

p=Place(province="หนองคาย",amphoe="เมืองหนองคาย")
def update():
    global p
    if getprovince()!='' and getdistrict()!='':
        p=Place(province=getprovince(),amphoe=getdistrict())
    elif getprovince()!='':
        p=Place(province=getprovince())
    else:
        p=Place(province="หนองคาย",amphoe="เมืองหนองคาย")
d=PyTMD(key,p)
pattern = r'\<LOCATION\>(.*?)\<\/LOCATION\>'
tokenizer = RegexpTokenizer(pattern)
ner = ThaiNameTagger()
province_list = provinces()

def now():
    global d,p
    data=d.forecast_daily(day("today"))[0]['forecasts'][0]['data']
    text = """
    สภาพอากาศที่{place}ตอนนี้ มีสภาพอากาศ{cond}
    มีอุณหภูมิ {temp} องศาเซลเซียส
    อุณหภูมิสูงสุด {temp_max} องศาเซลเซียส
    และมีอุณหภูมิต่ำสุด {temp_min} องศาเซลเซียสค่ะ
    """.format(place=p.province,cond=cond2txt(data['cond']),temp=int(data['tc']),temp_max=int(data['tc_max']),temp_min=int(data['tc_min'])).replace("    ","")
    return text

def tomorrow():
    global d,p
    data=d.forecast_daily(day("tomorrow"))[0]['forecasts'][0]['data']
    text = """
    สภาพอากาศที่{place} วันพรุ่งนี้ มีสภาพอากาศ{cond}
    มีอุณหภูมิเฉลี่ย {temp} องศาเซลเซียส
    อุณหภูมิสูงสุด {temp_max} องศาเซลเซียส
    และอุณหภูมิต่ำสุด {temp_min} องศาเซลเซียสค่ะ
    """.format(place=p.province,cond=cond2txt(data['cond']),temp=int(data['tc']),temp_max=int(data['tc_max']),temp_min=int(data['tc_min'])).replace("    ","")
    return text

#print(now())

def text2com(text):
    global now,tomorrow,tokenizer,ner,d,Place,PyTMD,province_list,p
    tag_ner = ner.get_ner(text,pos=False,tag=True)
    tt = tokenizer.tokenize(tag_ner)
    print("จังหวัดที่ตรวจพบ : "+str(tt))
    if "สภาพอากาศ" in text or "อากาศ" in text or "อุณหภูมิ" in text:
        pass
    else:
        return "ขออภัยค่ะ ระบบพยากรณ์อากาศยังไม่รองรับการใช้งานปัจจุบันค่ะ"
    if len(tt)>0:
        if tt[0] ==[] or tt[0] == '':
            temp = "หนองคาย"
        elif tt[0]=="โคราช":
            temp = "นครราชสีมา"
        else:
            temp = get_close_matches(tt[0], province_list,cutoff=0.6)[0]
        print(temp)
        if temp in province_list:
            p=Place(province=temp)
            d=PyTMD(key,p)
        else:
            if "โคราช" in text:
                p=Place(province="นครราชสีมา")
            else:
                update()
            d=PyTMD(key,p)
    else:
        update()
        d=PyTMD(key,p)
    if "วันนี้" in text or "ตอนนี้" in text:
        return now()
    elif "พรุ่งนี้" in text:
        return tomorrow()
    else:
        return now()
    #else:
    #    return "ขออภัยค่ะ ระบบพยากรณ์อากาศยังไม่รองรับการใช้งานปัจจุบันคะ"
