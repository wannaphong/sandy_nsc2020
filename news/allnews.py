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
        if day == "now":
            all_news+=[j for j in i.get_today()]
        else:
            all_news+=[j for j in i.yesterday()]
get_all()
def s(text,day="now"):
    global all_news,dn
    if dn!=day:
        get_all(day)
        dn=day
    t=[sentence_similarity(text,i) for i in all_news]#[0][0]
    p =max(t)
    print("ค่าความน่าจะเป็นของข่าวที่เกี่ยวข้องมากที่สุด : "+p)
    if p<0.02:
        return "ไม่พบข่าวค่ะ"
    return all_news[t.index(max(t))]
"""
while True:
    t = input("ชื่อข่าว : ")
    print(s(t))
    print()
"""