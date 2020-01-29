# -*- coding: utf-8 -*-
from .pytmd import *
from pythainlp.tag.named_entity import ThaiNameTagger
from pythainlp.corpus import provinces
from nltk.tokenize import RegexpTokenizer
from difflib import get_close_matches
from pysandy import getprovince,getdistrict
key="eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjNlNjRhYjY2ZGQxYzhkMGQ5NzJiNWFjYWUzODVkODkxNGU2MjRiMjNmMjA2NjllMDAwMjg2YmU4ZmVlYmM0NWY2MmQzNzU3YzI1N2U2ODczIn0.eyJhdWQiOiIyIiwianRpIjoiM2U2NGFiNjZkZDFjOGQwZDk3MmI1YWNhZTM4NWQ4OTE0ZTYyNGIyM2YyMDY2OWUwMDAyODZiZThmZWViYzQ1ZjYyZDM3NTdjMjU3ZTY4NzMiLCJpYXQiOjE1NzU4MDc0MjEsIm5iZiI6MTU3NTgwNzQyMSwiZXhwIjoxNjA3NDI5ODIxLCJzdWIiOiI2NzEiLCJzY29wZXMiOltdfQ.dbAs1ZiSmi75OUwD0E5--_XYYN1Izzuf1j1LRAbzLGipOcorDl1YmHolxxWFI7DnZ6jGiXoYVuBdZ5zUrrYWoifq_FkWbPC_i0DlLtnrm1tBD8ZuxI7rQTVf9hR-HOiatS81od52t-r2Z-Htbssza297SS2-9PK1NLPC3ysaP5sM4ENSUjKU65PrQHP_Joj4DE-HGm-dMk49UFhzZVZhMHrAu64wdFviQdLLLG7OExa6t5hHRE8QUWdIPwt7-_AWgDY9wy9W-Za9ivPBy6pebsMPF_jsL2nsw0rjiTm2QazfbHTfwAP-VvPOGuhHEBwNYsdwKS-8BdCj5-QOLa13tv7zoSOSIr1FR6y0Oku6gtQmN1aAMpfl_Y9nHNOA0LJg9Eh3WjDwIS1Tg-VEx2hoX4KPrqVNo1BjyNiuJ5upDARDsXC3VMBVJ7jt5ewpn769FGYoBDLawX-ngj6sT-CJ2FO63CEfjpx4wFkJSgsrB4ABxvtFKUAeVBEB_pIQAytUKy3k0lPVUUjCr1mC0yCj-q0cGX4X57jCTrjKA9-U2nElk-35nc3LhkNl3i37lXCQceLDxasrhFK_kXAJdRe6rzQZ7VIRU7m1cpfv17GdF_9p3rg3bRDnjLIOksD_423UzApKkku7AXCGRmGsC8Wzb4TEUsjIc-IMRFQzGr1nFHM"

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