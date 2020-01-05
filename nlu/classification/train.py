from pythainlu.intent_classification import naive_bayes,MultinomialNB
from pythainlp.tokenize import word_tokenize
from sklearn.model_selection import train_test_split
file = "../dataset/data-nottag.set"
import pandas as pd
colnames=['text', 'tag']


from pythainlp.tokenize import word_tokenize,Trie
from pythainlp.corpus import thai_stopwords
# ...
#filtered_words = [word for word in word_list if word not in list(thai_stopwords())]
o= Trie(list(thai_stopwords()))
def filtered_words(x:tuple):
    #w = .lower()#word_tokenize(x[0],custom_dict=o)
    #ww = [word for word in w if word not in list(thai_stopwords())]
    return (x[0].lower().strip() ,x[1])#(''.join(ww),x[1])

user1 = pd.read_csv(file, names=colnames, header=None,sep="|")
data= [filtered_words(tuple(x)) for x in user1.to_records(index=False)]
def features(text):
    wordlist = word_tokenize(text)
    f={}
    if "แจ้งเตือน" in text or 'เตือน' in text:
        f['a'] =True
    if "เวลา" in wordlist:
        f['time'] =True
    else:
        f['time'] = False
    if 'เปิด' in text or 'ปิด' in text:
        f['iot'] = True
    else:
        f['iot'] = False
    if 'พยากรณ์' in text or 'อากาศ' in text or 'สภาพอากาศ' in text:
        f['w'] = True
    else:
        f['w'] = False
    if 'เพลง' in text:
        f['m'] = True
    elif 'ธรรมะ' in text:
        f['b'] = True
    return f
train_data,test_data=train_test_split(data, test_size=0.1, random_state=42,shuffle=True)
model=MultinomialNB.train('sandy',train_data,test_data)
print(model[1])
def p(text):
    global model
    print(MultinomialNB.predict(model[0],text))

modelfull=MultinomialNB.train('sandy',data)
import dill
with open('../../modelclass2.model', 'wb') as out_strm: 
    dill.dump(modelfull, out_strm)


'''
while True:
    text = input("text : ")
    if text=="exit":
        break
    p([text])
'''