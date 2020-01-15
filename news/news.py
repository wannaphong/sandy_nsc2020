# -*- coding: utf-8 -*-
from .thaipbs import *
from .allnews import s
from pythainlp.util import num_to_thaiword




def get_news(ty="breakingnews",text=""):
    if ty == "breakingnews":
        temp=breakingnews()
        n= "เด่น"
    elif ty == "politics":
        temp = politics()
        n = "การเมือง"
    elif ty == "social":
        temp = social()
        n = "สังคม"
    elif ty == "crime":
        temp = crime()
        n = "อาชญากรรม"
    elif ty == "region":
        temp = region()
        n = "ภูมิภาค"
    elif ty == "environment":
        temp = environment()
        n = "สิ่งแวดล้อม"
    elif ty == "economy":
        temp = economy()
        n = "เศรษฐกิจ"
    elif ty == "foreign":
        temp = foreign()
        n= "ต่างประเทศ"
    elif ty == "sport":
        temp = sport()
        n="กีฬา"
    else:
        temp=breakingnews()
        n= "เด่น"
    t="ข่าว"+n+"ประจำวันนี้"
    l= temp.get_today()
    
    if len(l)==0 or "เมื่อวาน" in text:
        l=temp.yesterday()
        t="ข่าว"+n+"เมื่อวานนี้ "
    
    j=1
    for i in l:
        if j-1!=len(l):
            t+="ข่าวที่ "+num_to_thaiword(j)
        else:
            t+="ข่าวสุดท้าย "
        t+=" "+i#.replace('',')
        t+="   "
        j+=1
    t+="\n"+"สำหรับ"+"ข่าว"+n+"จบแล้วค่ะ"
    #sent = sent_tokenize(t)
    #t = '\n'.join(sent)
    return t

def gethotnews():
    temp=breakingnews()
    l= temp.get_today()
    t="ข่าวเด่นประจำวันนี้ "
    if len(l)==0:
        l=temp.yesterday()
        t="ข่าวเด่นเมื่อวานนี้ "
    
    j=1
    for i in l:
        if j-1!=len(l):
            t+="ข่าวที่ "+num_to_thaiword(j)
        else:
            t+="ข่าวสุดท้าย "
        t+=" "+i#.replace('',')
        t+="   "
        j+=1
    t+="สำหรับข่าวเด่นประจำวันจบแล้วค่ะ"
    return t
def get():
    n=gethotnews()
#print(gethotnews())
def text2com(text):
    global politics,get_news
    if "ข่าว" in text:
        pass
    else:
        return "ขออภัยค่ะ ระบบอ่านข่าวยังไม่รองรับการใช้งานปัจจุบันค่ะ"
    if "การเมือง" in text:
        return get_news("politics",text)
    elif "สังคม" in text:
        return get_news("social",text)
    elif "อาชญากรรม" in text:
        return get_news("crime",text)
    elif "ภูมิภาค" in text:
        return get_news("region",text)
    elif "สิ่งแวดล้อม" in text:
        return get_news("environment",text)
    elif "เศรษฐกิจ" in text:
        return get_news("economy",text)
    elif "ต่างประเทศ" in text or "ต่างชาติ" in text:
        return get_news("foreign",text)
    elif "กีฬา" in text:
        return get_news("sport",text)
    elif "วันนี้" in text or "ตอนนี้" in text or "สรุป" in text or 'เด่น' in text:
        return gethotnews()
    elif "ข่าว" in text and (text.split("ข่าว")[-1] !=[] and text.split("ข่าว")[-1] !=['']):
        return s(text.split("ข่าว")[-1])
    else:
        return "ขออภัยค่ะ ระบบอ่านข่าวยังไม่รองรับการใช้งานปัจจุบันค่ะ"