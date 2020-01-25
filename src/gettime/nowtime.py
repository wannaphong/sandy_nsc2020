# -*- coding: utf-8 -*-
from datetime import datetime
from pythainlp.util import thai_time,thai_strftime

def now(text):
    _n=datetime.now()
    print("t :",text)
    if "วัน" in text and "เวลา" in text:
        text = "วันนี้"+thai_strftime(_n, "%A %d %B %Y ")+"เวลา "+thai_time(str(_n.strftime('%H:%M')),"6h")+"ค่ะ"
    elif "วัน" in text:
        text = "วันนี้"+thai_strftime(_n, "%A %d %B %Y ")+"ค่ะ"
    elif 'เวลา' in text or 'เพลา' in text or 'โมง' in text:
        text = "ขณะนี้เวลา "+thai_time(str(_n.strftime('%H:%M')),"6h")+"ค่ะ"#นาฬิกา
    else:
        text = "ระบบบอกเวลา ยังไม่รองรับคำสั่งนี้ค่ะ"
    return text