import sys
import pandas as pd
from sklearn.pipeline import Pipeline
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import classification_report, f1_score, accuracy_score, confusion_matrix
import pickle

class Predict:

    def main(review):

        review=[review]

        filename = 'nn_model.sav'
        
        train = pickle.load(open(filename, 'rb'))
        predicted_class = train.predict(review)
        return predicted_class[0]



if __name__ == "__main__":
    pass

