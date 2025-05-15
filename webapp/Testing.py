import sys
import pandas as pd
from sklearn.pipeline import Pipeline
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report, f1_score, accuracy_score, confusion_matrix
import pickle

class Testing:

    def detecting(test_file,model='nn_model.sav'):

        #train_news = pd.read_csv(train_file)
        test_ = pd.read_csv(test_file)
        
        testdata=test_['sentiment']
        #tfidf = TfidfVectorizer(stop_words='english',use_idf=True,smooth_idf=True) #TF-IDF
        print("Start Classification")

        #knn_pipeline = Pipeline([('lrgTF_IDF', tfidf), ('lrg_mn', KNeighborsClassifier())])

        #pickle.dump(knn_pipeline.fit(train_news['review'], train_news['sentiment']), open(model, 'wb'))
        train = pickle.load(open(model, 'rb'))
        predicted_class = train.predict(test_["review"])
        
        r=Testing.model_assessment(testdata,predicted_class)
        print((r))

        return r


    def model_assessment(y_test, predicted_class):
        print('accuracy')
        # Accuracy = (TP + TN) / ALL
        accuracy = accuracy_score(y_test, predicted_class)
        return accuracy


if __name__ == "__main__":
    Testing.detecting('testset.csv')

