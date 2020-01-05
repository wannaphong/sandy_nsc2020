# -*- coding: utf-8 -*-
from datetime import datetime
from pythainlp.util import thai_time

def now(text):
    if "วัน" and "เวลา":
        pass
    elif 'เวลา' in text or 'เพลา' in text or 'โมง' in text:
        text = "ขณะนี้เวลา "+thai_time(str(datetime.now().strftime('%H:%M')),"6h")+"ค่ะ"#นาฬิกา
    else:
        text = "ระบบบอกเวลา ยังไม่รองรับคำสั่งนี้ค่ะ"
    return text