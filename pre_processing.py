import spacy
<<<<<<< HEAD
import numpy as np
import pandas as pd
=======
from textblob import TextBlob                         #You have to download textblob
>>>>>>> 814b659e77e82d4be4858a862f1369bbad573d69
nlp = spacy.load("en_core_web_sm")


class Pre_Processing:

    def __init__(self, file_name):
        self.file_name = file_name
        self.undoced_instance_list = [] #List of all paragraphs in base form. (Not in Spacy Doc form)
        self.doc_instance_list = [] #list of every instance in Spacy doc form
        self.instance_labels = [] #1 for pos 0 for neg

        

        """Method Calls Description
        
        1. extract_training calls ___clean_text__.
        2. __clean_text__ returns a refined list undoced_instance_list.
        3. __spacy_tokenizer__ makes the doc_instance_list. """

        #Method Calls
        self._extract_training_()
        self._spacy_docizer_()
        self._label_lister_()

        


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
            
            

    def _label_lister_(self): #creates the label for the instances
        label_count = len(self.doc_instance_list)
        if self.file_name.endswith("neg.txt"):
            value = 0
        elif self.file_name.endswith("pos.txt"):
            value = 1
        label_list = []
        for i in range(label_count):
            label_list.append(value)
        self.instance_labels = label_list

    def data_merger(self, pos_labels, neg_labels, feature_1_neg, feature_1_pos, feature_2_neg, feature_2_pos):
        labels_list = pos_labels + neg_labels
        feature_1 = feature_1_pos + feature_1_neg
        feature_2 = feature_2_pos + feature_2_neg
        pandas_dataframe = pd.DataFrame(labels_list, feature_1, feature_2)
        return pandas_dataframe

    
        
   
        
        
            
#main
file = "train_pos.txt"
pre = Pre_Processing(file)
doc_list = pre.doc_instance_list #Important: This is a list of doc type object.
label_list = pre.instance_labels #Label list for the current file


<<<<<<< HEAD
=======











            
            
     
        

    

   
>>>>>>> 814b659e77e82d4be4858a862f1369bbad573d69





