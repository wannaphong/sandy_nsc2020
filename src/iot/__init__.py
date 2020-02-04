# -*- coding: utf-8 -*-
import requests

def event(n):
    url = "https://maker.ifttt.com/trigger/{e}/with/key/dtdTlG_QqZNeap3ird6gWE".format(e=n)
    #print(url)
    return requests.get(url)

def light(e):
    if e=="on":
        event("nsc-light-on")
    else:
        event("nsc-light-off")

def fan(e):
    if e=="on":
        event("nsc-fan-on")
    else:
        event("nsc-fan-off")

def text2com(text,t):
    if t not in ['light','fan']:
        return "ระบบไอโอทีไม่รองรับการทำงานนี้ค่ะ"
    temp=""
    if "เปิด" in text and t=="light":
        light("on")
        temp="เปิดไฟแล้วค่ะ"
    elif "ปิด" in text and t=="light":
        light("off")
        temp="ปิดไฟแล้วค่ะ"
    elif "เปิด" in text and t=="fan":
        fan("on")
        temp="เปิดพัดลมแล้วค่ะ"
    elif "ปิด" in text and t=="fan":
        fan("off")
        temp="ปิดพัดลมแล้วค่ะ"
    else:
        temp="ระบบยังไม่รองรับฟังก์ชันนี้ค่ะ"
    return temp