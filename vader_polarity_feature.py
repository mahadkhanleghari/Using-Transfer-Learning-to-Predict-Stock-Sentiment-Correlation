from pre_processing import Pre_Processing
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer





class Vader_polarity:
     def __init__(self):
    
        self.feature_list=[]            #list of features that will be returned
        self.featureAnalyzer=SentimentIntensityAnalyzer()


     def get_feature(self,doc_list):
        
            for doc in doc_list:
                 
                 self.polarity_score=self.featureAnalyzer.polarity_scores(doc.text)["compound"] #compound indicates the overall polarity, whether it is positive or negative, similar to TextBlob

                 if self.polarity_score >0.1:       
                    self.feature_list.append(1)
                 else:
                    self.feature_list.append(0)
               

            
            return self.feature_list
    
            
#if the polarity of the document is >0.1, then the feature is positive (1) , else it is negative (0)            
        

   
#getting the features for the train_pos file
pos_pre=Pre_Processing("train_pos.txt")
pos_doc_list = pos_pre.doc_instance_list

pos_training_file_features=Vader_polarity().get_feature(pos_doc_list)


#getting the features for the train_neg file
neg_pre=Pre_Processing("train_neg.txt")
neg_doc_list =neg_pre.doc_instance_list


neg_training_file_features=Vader_polarity().get_feature(neg_doc_list)




















 