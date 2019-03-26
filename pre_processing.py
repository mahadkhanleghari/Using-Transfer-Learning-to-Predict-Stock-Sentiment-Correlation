import spacy
nlp = spacy.load("en_core_web_sm")

class Pre_Processing:

    def __init__(self, file_name):
        self.file_name = file_name
        self.undoced_instance_list = [] #List of all paragraphs in base form. (Not in Spacy Doc form)
        self.doc_instance_list = [] #list of every instance in Spacy doc form

        """Method Calls Description
        
        1. extract_training calls ___clean_text__.
        2. __clean_text__ returns a refined list undoced_instance_list.
        3. __spacy_tokenizer__ makes the doc_instance_list."""

        #Method Calls
        self._extract_training_()
        self._spacy_docizer_()


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




#main
file = "train_neg.txt"
pre = Pre_Processing(file)
doc_list = pre.doc_instance_list #Important: This is a list of doc type object.

print(doc_list)





