import spacy
import numpy as np
import pandas as pd
nlp = spacy.load("en_core_web_sm")


class Pre_Processing:

    def __init__(self, file_name):
        self.file_name = file_name
        self.undoced_instance_list = [] #List of all paragraphs in base form. (Not in Spacy Doc form)
        self.doc_instance_list = [] #list of every instance in Spacy doc form
        self.article_undoc_list = []
        self.article_doc_list = []
        self.instance_labels = [] #1 for pos 0 for neg


        """Method Calls Description
        
        1. extract_training calls ___clean_text__.
        2. __clean_text__ returns a refined list undoced_instance_list.
        3. __spacy_tokenizer__ makes the doc_instance_list. """

        #Method Calls
        self._extract_training_()
        self._spacy_docizer_()
        if file_name.endswith("neg.txt") or file_name.endswith("pos.txt"):
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


class Date_Dict_Pre_Processing:

    def __init__(self, date_dict):
        self.date_dict = date_dict
        self.date_dict_article_doc = {}
        self.date_dict_title_doc = {}

        """Method Calls"""
        self.__creator__()

    def __creator__(self):
        for date, values in self.date_dict.items():
            cleaned = self.__clean_text__(values["Article Text List"])
            doced = self.__spacy_docizer__(cleaned)
            self.date_dict_article_doc[date] = doced
        for d, v in self.date_dict.items():
            self.date_dict_title_doc[d] = v["Titles List"]

    def __clean_text__(self, raw_list):
        refined = [] #removes the special characters. Not to be confused with String Special Characters.
        for paragraph in raw_list:
            b_removed = paragraph.replace("<br /><br />", "")
            n_removed = b_removed.replace("\n", "")
            refined.append(n_removed)
        refined_new = [] #removes the empty paragraph or any empty object in list
        for para in refined:
            if para != "":
                refined_new.append(para)
        return refined_new

    def __spacy_docizer__(self, raw_list):
        refined_list = []
        for article in raw_list:
            new = nlp(article)
            refined_list.append(new)
        return refined_list


#Data Merger Function

def data_merger(pos_labels, neg_labels, feature_1_neg, feature_1_pos, feature_2_neg, feature_2_pos,
                feature_3_neg, feature_3_pos):
    labels_list = pos_labels + neg_labels
    feature_1 = feature_1_pos + feature_1_neg
    feature_2 = feature_2_pos + feature_2_neg
    feature_3 = feature_3_pos + feature_3_neg
    head_dict = {"Label": labels_list, "Bag of Words": feature_1, "Polarity": feature_2, "Vader Polarity": feature_3}
    pandas_dataframe = pd.DataFrame(head_dict)
    return pandas_dataframe

def article_merger(feature_1, feature_2, feature_3):
    head_dict = {"Bag of Words": feature_1, "Polarity": feature_2, "Vader Polarity": feature_3}
    pandas_dataframe = pd.DataFrame(head_dict)
    return pandas_dataframe

def output_frame(date_polarity, title_polarity, date_interest, pandas_dataframe, default = 0.1, title_default = 0.05,
                 interest_default = 0):
    date_list = []
    for date in date_polarity:
        date_list.append(date)
    sorted_date = sorted(date_list)
    pol_dict = {}
    title_dict = {}
    interest_dict = {}
    for d in sorted_date:
        for article_date, polarity in date_polarity.items():
            if d == article_date:
                pol_dict[str(d)] = polarity
        for ad, pl in title_polarity.items():
            if d == ad:
                title_dict[str(d)] = pl
        for adate, mentions in date_interest.items():
            if d == adate:
                interest_dict[str(d)] = mentions
    pols_list = []
    title_list = []
    interest_list = []
    for v in pandas_dataframe["date"]:
        date_time_object = str(v).split(" ")
        date1 = str(date_time_object[0])
        if date1 in pol_dict:
            pols_list.append(pol_dict[date1])
        else:
            pols_list.append(default)
        if date1 in title_dict:
            title_list.append(title_dict[date1])
        else:
            title_list.append(title_default)
        if date1 in interest_dict:
            interest_list.append(interest_dict[date1])
        else:
            interest_list.append(interest_default)
    pandas_dataframe.insert(loc = 6, column = "Articles Polarity", value = pols_list)
    pandas_dataframe.insert(loc = 7, column = "Titles Polarity", value = title_list)
    pandas_dataframe.insert(loc = 8, column = "Interest", value = interest_list)
    return pandas_dataframe

#main

















            






