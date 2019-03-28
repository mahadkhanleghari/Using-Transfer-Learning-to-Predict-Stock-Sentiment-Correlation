from pre_processing import Pre_Processing
from textblob import TextBlob                         #You have to download textblob
import collections





class Polarity_feature:
     def __init__(self):
    
        self.feature_list=[]            #list of features that will be returned

     def get_feature(self,doc_list):
        
            for doc in doc_list:
                 doc_blob=TextBlob(doc.text)

                 if doc_blob.sentiment.polarity >0.1:       #the textblob object has a function that calculate the positivity or negativity(polarity) of a piece of text
                    self.feature_list.append(1)
                 else:
                    self.feature_list.append(0)
               

            
            return self.feature_list
    
            
#if the polarity of the document is >0.1, then the feature is positive (1) , else it is negative (0)            
        

   
#getting the features for the train_pos file
pos_pre=Pre_Processing("train_pos.txt")
pos_doc_list = pos_pre.doc_instance_list

pos_training_file_features=Polarity_feature().get_feature(pos_doc_list)


#getting the features for the train_neg file
neg_pre=Pre_Processing("train_neg.txt")
neg_doc_list =neg_pre.doc_instance_list


neg_training_file_features=Polarity_feature().get_feature(neg_doc_list)



print(collections.Counter(pos_training_file_features))        #displaying the negative training file features
print(collections.Counter(neg_training_file_features))        #displaying the negative training file features


















 