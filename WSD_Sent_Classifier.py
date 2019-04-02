from pre_processing import Pre_Processing
from senti_classifier import senti_classifier

class WSD_Sent_Classifier:
    def __init__(self):
    
        self.feature_list=[]            
        self.featureAnalyzer=senti_classifier()

    def get_feature(self,doc_list):
        
            for doc in doc_list:
                self.pos_score, self.neg_score =self.featureAnalyzer.polarity_scores(doc.text)
                 if self.pos_score > self.neg_score: 
                    self.feature_list.append(1)
                else:
                    self.feature_list.append(0)
            
            return self.feature_list
    
            
#just like bag of words, sent_classifier classifies the overall sentiment of the text but it takes sentences 
#as inputs and hence sequence is preserved.
        
#features for the train_pos file

pos_pre=Pre_Processing("train_pos.txt")
pos_doc_list = pos_pre.doc_instance_list

pos_training_file_features=WSD_Sent_Classifier().get_feature(pos_doc_list)

#features for the train_neg file
neg_pre=Pre_Processing("train_neg.txt")
neg_doc_list =neg_pre.doc_instance_list

neg_training_file_features=WSD_Sent_Classifier().get_feature(neg_doc_list)
