import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree
from sklearn import preprocessing

class Decision_Tree:

    def __init__(self, training_data, test_data):
        self.training_data = training_data #pandas data frame
        self.test_data = test_data #pandas data frame
        self.accuracy = 0

        #Method
        self._classifier_()

    def _classifier_(self):
        training = self.training_data.values[:, 1:len(self.training_data.columns)]
        training_label = self.training_data.values[:, 0]
        test = self.test_data.values[:, 1:len(self.test_data.columns)]
        test_label = self.test_data.values[:,0]
        entropy = DecisionTreeClassifier(criterion= "entropy")
        entropy.fit(training, training_label)
        test_predict = entropy.predict(test)
        self.accuracy = accuracy_score(test_label, test_predict)


