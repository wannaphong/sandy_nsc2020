from datetime import datetime
from pythainlp.util import thai_time

def now():
    text = "ขณะนี้เวลา "+thai_time(str(datetime.now().strftime('%H:%M')), "m6h")+"ค่ะ"#นาฬิกา
    return text