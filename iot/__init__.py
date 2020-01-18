# -*- coding: utf-8 -*-
import requests

def event(n):
    requests.get("https://maker.ifttt.com/trigger/{e}/with/key/dHXY-7BWw4HBYNiCa6kaJQ".format(e=n))

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
    if t=="fan":
        temp="ระบบยังไม่รองรับพัดลมค่ะ"
    return temp