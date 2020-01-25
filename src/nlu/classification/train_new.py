file = "../dataset/data-nottag.set"
import pandas as pd
colnames=['text', 'tag']
def filtered_words(x:tuple):
    #w = .lower()#word_tokenize(x[0],custom_dict=o)
    #ww = [word for word in w if word not in list(thai_stopwords())]
    return (x[0].lower().strip() ,x[1])#(''.join(ww),x[1])
user1 = pd.read_csv(file, names=colnames, header=None,sep="|")
data= [filtered_words(tuple(x)) for x in user1.to_records(index=False)]

# model
from typing import List
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from pythainlp.ulmfit import process_thai
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer, TfidfTransformer
from sklearn.feature_selection import SelectKBest, chi2

nb = Pipeline([('vect', CountVectorizer(tokenizer=process_thai, ngram_range=(1,2))),
               ('tfidf', TfidfTransformer()),
               ('chi2', SelectKBest(chi2, k='all')),
               ('clf', MultinomialNB()),
])