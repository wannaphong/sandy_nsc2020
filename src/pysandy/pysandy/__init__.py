# -*- coding: utf-8 -*-
import requests
key="cedf380e-e540-42c3-b21b-ba8a2e7f7011"
host="https://sandy.numfa.com"

def getid():
    r = requests.get(host+"/api/getid/"+key)
    if r.status_code==200:
        return r.text
    return ''

def getprovince():
    """
    รับจังหวัด
    """
    r = requests.get(host+"/api/getprovince/"+key)
    if r.status_code==200:
        return r.text
    return ''

def getlinenotify():
    """
    รับ key line notify
    """
    r = requests.get(host+"/api/getlinenotify/"+key)
    if r.status_code==200:
        return r.text
    return ''

def getdistrict():
    """
    รับอำเภอ
    """
    r = requests.get(host+"/api/getdistrict/"+key)
    if r.status_code==200:
        return r.text
    return ''