# -*- coding: utf-8 -*-
from .thaipbs import *
from pythainlp import word_tokenize # ทำการเรียกตัวตัดคำ
#from pythainlp.word_vector import sentence_vectorizer # ทำการเรียก thai2vec
from sklearn.metrics.pairwise import cosine_similarity  # ใช้หาค่าความคล้ายคลึง
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(tokenizer=word_tokenize)
all_news=[]
dn="now"
#def sentence_similarity_old(s1,s2):
#    return cosine_similarity(sentence_vectorizer(str(s1)),sentence_vectorizer(str(s2)))[0][0]

def sentence_similarity(text1, text2):
    # Thank you - https://stackoverflow.com/a/24129170/11952699
    tfidf = vectorizer.fit_transform([text1, text2])
    return ((tfidf * tfidf.T).A)[0,1]

def get_all(day="now"):
    global all_news,breakingnews,politics,social,crime,region,environment,economy,foreign,sport
    n = [breakingnews(),politics(),social(),crime(),region(),environment(),economy(),foreign(),sport()]
    for i in n:
        _n=i.get_today()
        if day == "now" and len(_n)>0:
            all_news+=[j for j in _n]
        else:
            all_news+=[j for j in i.yesterday()]
get_all()
def s(text,day="now"):
    global all_news,dn
    if dn!=day:
        get_all(day)
        dn=day
    _t=[sentence_similarity(text,i) for i in all_news]#[0][0]
    #print(_t)
    p =max(_t)
    print("ค่าความน่าจะเป็นของข่าวที่เกี่ยวข้องมากที่สุด : "+str(p))
    if p<0.02:
        return "ไม่พบข่าวค่ะ"
    return all_news[_t.index(max(_t))]
"""
while True:
    t = input("ชื่อข่าว : ")
    print(s(t))
    print()
"""