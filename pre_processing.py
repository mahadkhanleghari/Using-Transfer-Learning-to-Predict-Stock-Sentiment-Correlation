import spacy
from textblob import TextBlob                         #You have to download textblob
nlp = spacy.load("en_core_web_sm")


class Pre_Processing:

    def __init__(self, file_name,positive_words_filename,negative_words_filename):
        self.file_name = file_name
        self.positive_words_filename=positive_words_filename#name of the file that contains the bag of positive words
        self.negative_words_filename=negative_words_filename#name of the file that contains the bag of negative words
        self.undoced_instance_list = [] #List of all paragraphs in base form. (Not in Spacy Doc form)
        self.doc_instance_list = [] #list of every instance in Spacy doc form
        self.positive_words_list=[] #list of positive words 
        self.negative_words_list=[] #list of negative words
        

        """Method Calls Description
        
        1. extract_training calls ___clean_text__.
        2. __clean_text__ returns a refined list undoced_instance_list.
        3. __spacy_tokenizer__ makes the doc_instance_list.
        4. _get_positive_words places the bag of words in the positive_words.txt file in a list
        5. _get_negative_words places the bag of words in the negative_words.txt file in a list    """

        #Method Calls
        self._extract_training_()
        self._spacy_docizer_()
        self._get_positive_words_()
        self._get_negative_words_()
        


    def _extract_training_(self):
        with open(self.file_name, "r") as training_file:
            raw_text_list = training_file.read().split("PARA:ID")
        self.undoced_instance_list = self.__clean_text__(raw_text_list)

    def __clean_text__(self, raw_text_list):
        refined = [] #removes the special characters. Not to be confused with String Special Characters.
        for paragraph in raw_text_list:
            b_removed = paragraph.replace("<br /><br />", "")
            n_removed = b_removed.replace("\n", "")
            refined.append(n_removed)
        refined_new = [] #removes the empty paragraph or any empty object in list
        for para in refined:
            if para != "":
                refined_new.append(para)
        return refined_new

    def _spacy_docizer_(self): #Converts every paragraph into a doc object and appends it to the doc list
        for instance in self.undoced_instance_list:
            new = nlp(instance)
            self.doc_instance_list.append(new)
            
            
    def _get_positive_words_(self):         #gets a list of positive words from the positive_words.txt file
        
        with open(self.positive_words_filename,"r") as pos_words:
           self.positive_words_list=pos_words.read().split()

         
    def _get_negative_words_(self):         #gets a list of negative words from the negative_words.txt file
        
        with open(self.negative_words_filename,"r") as neg_words:
            self.negative_words_list=neg_words.read().split()
        
   
        




        
        
            
#main
file = "test_neg.txt"
positive_words_file="positive_words.txt"
negative_words_file="negative_words.txt"
pre = Pre_Processing(file,positive_words_file,negative_words_file)

doc_list = pre.doc_instance_list #Important: This is a list of doc type object.




feature1=[]                     #these two lists will contain the features for each doc object
feature2=[]

negative_words_count=[]         #these two lists are used to calculate the second feature
positive_words_count=[]


for doc in doc_list:
    doc_blob=TextBlob(doc.text)

    if doc_blob.sentiment.polarity >0.1:       #the textblob object has a function that calculate the positivity or negativity(polarity) of a piece of text
        feature1.append(1)
    else:
        feature1.append(0)
        
        
  #for the second feature, we check each word if it exists in either the positive words list or negative words list
  #if it exists in the positive words list, we increment the positive_words_count list by 1
  #if it exists in the positive words list, we increment the negative_words_count list by 1
   
    for word in doc:                
        if word.text in pre.negative_words_list:
            negative_words_count.append(1)
        if word.text in pre.positive_words_list:
            positive_words_count.append(1)
            
    #after getting the counts for each word, we calculate the sum of each count. if count of positive >count of negative, then it is positive
    if sum(positive_words_count)>sum(negative_words_count):
        feature2.append(1)
    else:
        feature2.append(0)
    positive_words_count.clear()
    negative_words_count.clear()
    


#note that both features are binary, where 1 indicates that it is positive, and 0 indicates that it is negative


            
            
     
        

    

   





