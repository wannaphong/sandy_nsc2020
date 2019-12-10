from .thaipbs import *
from pythainlp.util import num_to_thaiword
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