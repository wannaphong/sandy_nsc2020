from sklearn.neural_network import MLPClassifier
from typing import List
from sklearn.pipeline import Pipeline
from pythainlp.ulmfit import process_thai
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer, TfidfTransformer
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
model = MLPClassifier(solver='adam', alpha=1e-5,hidden_layer_sizes=(24, 6), verbose=False, max_iter=2000)
nb = Pipeline([('vect', CountVectorizer(tokenizer=process_thai, ngram_range=(1,2))),
               ('tfidf', TfidfTransformer()),
               ('chi2', SelectKBest(chi2, k='all')),
               ('clf', model),
])