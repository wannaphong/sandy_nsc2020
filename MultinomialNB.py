# -*- coding: utf-8 -*-
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

def train(name,train_data:List[tuple],test_data=None)->tuple:
    """
    Train Naive Bayes Classifier for Multinomial Models

    :param list train_data: list train data of tuple (text,tag)
    :param object get_features: function of features
    :param list test_data: list test data of tuple (text,tag)

    :return: tuple(model,accuracy)
    """
    X_data=[]
    y_data=[]
    for sent in train_data:
        X_data.append(sent[0])
        y_data.append(sent[1])
    nb.fit(X_data, y_data)
    if test_data!=None:
        X_test=[]
        y_test=[]
        for sent in test_data:
            X_test.append(sent[0])
            y_test.append(sent[1])
        y_pred = nb.predict(X_test)
        return (nb, accuracy_score(y_pred, y_test))
    return (nb,)

def predict(model,text):
    return (model.predict(text),model.predict_proba(text))