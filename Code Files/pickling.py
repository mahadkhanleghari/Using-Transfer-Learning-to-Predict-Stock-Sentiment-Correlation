import pickle
import pre_processing

training_pos = pre_processing.Pre_Processing("train_pos.txt")
training_pos_list = training_pos.doc_instance_list
training_neg = pre_processing.Pre_Processing("train_neg.txt")
training_neg_list = training_neg.doc_instance_list
test_pos = pre_processing.Pre_Processing("test_pos.txt")
test_pos_list = test_pos.doc_instance_list
test_neg = pre_processing.Pre_Processing("test_neg.txt")
test_neg_list = test_neg.doc_instance_list

def pickling_full(doc_list, name):
    final_name = name + ".out"
    with open(final_name, "wb") as file_o:
        pickle.dump(doc_list, file_o)

#training pickle files
pos = pickling_full(training_pos_list, "train_pos_pickle")
neg = pickling_full(training_neg_list, "train_neg_pickle")
#test
pos_test = pickling_full(test_pos_list, "test_pos_pickle")
neg_test = pickling_full(test_neg_list, "test_neg_pickle")



