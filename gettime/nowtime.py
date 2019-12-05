from datetime import datetime

def now():
    text = "ขณะนี้เวลา "+str(datetime.now().strftime('%H:%M:%S'))+" นาฬิกาค่ะ"
    return text