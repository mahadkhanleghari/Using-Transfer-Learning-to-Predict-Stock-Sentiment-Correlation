import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree
from sklearn import preprocessing
from collections import Counter

class Decision_Tree:

    def __init__(self, training_data, test_data):
        self.training_data = training_data #pandas data frame
        self.test_data = test_data #pandas data frame
        self.accuracy = 0

        #Method

    def classifier(self):
        training = self.training_data.values[:, 1:len(self.training_data.columns)]
        training_label = self.training_data.values[:, 0]
        test = self.test_data.values[:, 1:len(self.test_data.columns)]
        test_label = self.test_data.values[:,0]
        entropy = DecisionTreeClassifier(criterion= "entropy")
        entropy.fit(training, training_label)
        test_predict = entropy.predict(test)
        accuracy = accuracy_score(test_label, test_predict)
        return accuracy

    def article_classifier(self):
        training = self.training_data.values[:, 1:len(self.training_data.columns)]
        training_label = self.training_data.values[:, 0]
        test = self.test_data.values[:, 0:len(self.test_data.columns)]
        entropy = DecisionTreeClassifier(criterion="entropy")
        entropy.fit(training, training_label)
        test_predict = entropy.predict(test)
        total = len(test_predict)
        polarity_freq = Counter(test_predict)
        pos_val = polarity_freq[1]
        neg_val = polarity_freq[0]
        result = pos_val/total
        return result





