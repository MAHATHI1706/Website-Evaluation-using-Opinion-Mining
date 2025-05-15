import sys
import pandas as pd
from sklearn.pipeline import Pipeline
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import svm
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report, f1_score, accuracy_score, confusion_matrix
import pickle



def rfclassfy(train_file='Training.csv'):
    train_news = pd.read_csv(train_file)
    tfidf = TfidfVectorizer(stop_words='english', use_idf=True, smooth_idf=True)  # TF-IDF

    svm_pipeline = Pipeline([('lrgTF_IDF', tfidf), ('lrg_mn', RandomForestClassifier(n_estimators=100, max_depth=2))])

    filename = 'rf_model.sav'
    pickle.dump(svm_pipeline.fit(train_news['review'], train_news['sentiment']), open(filename, 'wb'))

    print("Model Successfully Trained")



#rfclassfy()