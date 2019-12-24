from pythainlu.intent_classification import naive_bayes,MultinomialNB
from pythainlp.tokenize import word_tokenize
from sklearn.model_selection import train_test_split
with open("../dataset/data-nottag.set",'r',encoding='utf-8') as f:
    data=[tuple(i.strip().split('|')) for i in f.readlines()]
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
while True:
    text = input("text : ")
    if text=="exit":
        break
    p([text])