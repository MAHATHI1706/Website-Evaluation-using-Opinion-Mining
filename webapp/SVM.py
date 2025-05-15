import sys
import pandas as pd
from sklearn.pipeline import Pipeline
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import LinearSVC
from sklearn import svm
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report, f1_score, accuracy_score, confusion_matrix
import pickle



def svmclassfy(train_file='Training.csv'):
    train_news = pd.read_csv(train_file)
    tfidf = TfidfVectorizer(stop_words='english', use_idf=True, smooth_idf=True)  # TF-IDF

    svm_pipeline = Pipeline([('lrgTF_IDF', tfidf), ('lrg_mn', LinearSVC(random_state=0, tol=1e-5))])

    filename = 'svm_model.sav'
    pickle.dump(svm_pipeline.fit(train_news['review'], train_news['sentiment']), open(filename, 'wb'))

    print("Model Successfully Trained")



#svmclassfy()