# -*- coding: utf-8 -*-
import time
import requests, urllib.parse
import io
#from PIL import Image
from pysandy import getlinenotify


class LINE:
    def __init__(self, token):
        self.url = 'https://notify-api.line.me/api/notify'
        self.LINE_HEADERS = {'Authorization': 'Bearer ' + token}
        self.session = requests.Session()

    """def sendimage(self, image, msg='image'):
        f = io.BytesIO()
        Image.fromarray(image).save(f, 'png')
        data = f.getvalue()
        response = self.session.post(self.url,
                                     headers=self.LINE_HEADERS,
                                     params={"message": msg},
                                     files={"imageFile": data})
        return response.text"""

    def sendtext(self, msg):
        response = self.session.post(self.url,
                                     headers=self.LINE_HEADERS,
                                     params={"message": msg})
        return response.text

    def sendsticker(self, stickerPackageId=2, stickerId=34, msg ='sticker'):
        response = self.session.post(self.url,
                                     headers=self.LINE_HEADERS,
                                     params={"message": msg,
                                             "stickerPackageId": stickerPackageId,
                                             "stickerId": stickerId})
        return response.text

def sent():
    if getlinenotify()=='':
        return "ระบบขอความช่วยเหลือผ่านนไลน์ยังไม่เปิดใช้งาน กรุณาตั้งค่าก่อนตามคู่มือการใช้งานค่ะ"
    line = LINE(getlinenotify())
    line.sendtext("มีคนในบ้านต้องการความช่วยเหลือด่วนครับ")
    line.sendtext("ช่วยมาที่บ้านด้วยครับ")
    line.sendsticker(1,4)
    return "กำลังขอความช่วยเหลือผ่านไลน์ค่ะ"