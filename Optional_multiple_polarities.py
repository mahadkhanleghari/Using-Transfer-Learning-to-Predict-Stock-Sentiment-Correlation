from senti_classifier import senti_classifier
from textblob import TextBlob

class WSD_Sent_Classifier:

    def __init__(self):
    
        self.pos_feature_list= []
        self.neg_feature_list = []
        self.featureAnalyzer = senti_classifier


    def get_polarity(self, sentence):
        pos, neg = self.featureAnalyzer.polarity_scores(sentence)
        return pos, neg

    def textblob(self, sentence):
        pol = TextBlob(sentence)
        score = pol.sentiment.polarity
        return score









