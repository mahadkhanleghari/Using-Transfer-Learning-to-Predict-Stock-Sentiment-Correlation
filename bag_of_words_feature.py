from pre_processing import Pre_Processing
import collections

class Bag_of_words_feature:
     def __init__(self):
        
         
        #variable initialization
        
        self.positive_words_filename="positive_words.txt"    #name of the file that contains the bag of positive words
        self.negative_words_filename="negative_words.txt"    #name of the file that contains the bag of negative words
        
        self.positive_words_list=[] #contains positive words that are retrieved from positive_words.txt 
        self.negative_words_list=[] #contains  negative words that are retrieved from negative_words.txt 
       
        self.feature_list=[]


        self.negative_words_count=[]     #these two lists contain the counts used to detect whether the doc object is positive or negative
        self.positive_words_count=[]
        
        
        #method calls
        self._get_positive_words_()
        self._get_negative_words_()
        
       
     
     def _get_positive_words_(self):         #gets a list of positive words from the positive_words.txt file
        
            with open(self.positive_words_filename,"r") as pos_words:
                self.positive_words_list=pos_words.read().split()

         
     def _get_negative_words_(self):         #gets a list of negative words from the negative_words.txt file
        
           with open(self.negative_words_filename,"r") as neg_words:
            self.negative_words_list=neg_words.read().split()
            
     
     def get_feature(self,doc_list):
        
     # we check each word if it exists in either the positive words list or negative words list
     #if it exists in the positive words list, we increment the positive_words_count list by 1
     #if it exists in the negative words list, we increment the negative_words_count list by 1
         
            for doc in doc_list:   
               for word in doc:                
                 if word.text in self.negative_words_list:
                    self.negative_words_count.append(1)
                 if word.text in self.positive_words_list:
                    self.positive_words_count.append(1)
            
     #after getting the counts for each word, we calculate the sum of each count. if count of positive >count of negative, then it is positive
               if sum(self.positive_words_count)>sum(self.negative_words_count):
                self.feature_list.append(1)
               else:
                self.feature_list.append(0)
                
                self.positive_words_count.clear()
                self.negative_words_count.clear()
            
            return self.feature_list
    











    















 
