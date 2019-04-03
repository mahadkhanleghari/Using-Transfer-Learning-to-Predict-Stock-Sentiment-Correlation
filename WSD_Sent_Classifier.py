from pre_processing import Pre_Processing
from senti_classifier import senti_classifier


class WSD_Sent_Classifier:

    def __init__(self):
    
        self.pos_feature_list= []
        self.neg_feature_list = []
        self.featureAnalyzer = senti_classifier


    def get_feature(self, doc_list):
        for doc in doc_list:
            doc_sents = []
            for sent in doc.sents:
                doc_sents.append(sent.text)
            pos, neg = self.featureAnalyzer.polarity_scores(doc_sents)
            self.pos_feature_list.append(pos)
            self.neg_feature_list.append(neg)













    
            
#just like bag of words, sent_classifier classifies the overall sentiment of the text but it takes sentences 
#as inputs and hence sequence is preserved.
        
#features for the train_pos file

pos_pre = Pre_Processing("train_pos.txt")
pos_doc_list = pos_pre.doc_instance_list

pos_training_file_features= WSD_Sent_Classifier().get_feature(pos_doc_list)

#features for the train_neg file
#neg_pre=Pre_Processing("train_neg.txt")
#neg_doc_list = neg_pre.doc_instance_list

#neg_training_file_features=WSD_Sent_Classifier().get_feature(neg_doc_list)"""
