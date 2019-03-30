"""Import Files"""
import pre_processing
import decision_tree_classifier
import bag_of_words_feature
import polarity_feature


"Feature 1: Bag of Words"
#Training

training_pos = pre_processing.Pre_Processing("train_pos.txt")
training_pos_list = training_pos.doc_instance_list
training_pos_labels = training_pos.instance_labels
training_pos_1 = bag_of_words_feature.Bag_of_words_feature().get_feature(training_pos_list)


training_neg = pre_processing.Pre_Processing("train_neg.txt")
training_neg_list = training_neg.doc_instance_list
training_neg_labels = training_neg.instance_labels
training_neg_1 = bag_of_words_feature.Bag_of_words_feature().get_feature(training_neg_list)

#Test

test_pos = pre_processing.Pre_Processing("test_pos.txt")
test_pos_list = test_pos.doc_instance_list
test_pos_labels = test_pos.instance_labels
test_pos_1 = bag_of_words_feature.Bag_of_words_feature().get_feature(test_pos_list)

test_neg = pre_processing.Pre_Processing("test_neg.txt")
test_neg_list = test_neg.doc_instance_list
test_neg_labels = test_neg.instance_labels
test_neg_1 = bag_of_words_feature.Bag_of_words_feature().get_feature(test_neg_list)

"""Feature 2: Polarity"""

#Training

training_pos_2 = polarity_feature.Polarity_feature().get_feature(training_pos_list)
training_neg_2 = polarity_feature.Polarity_feature().get_feature(training_neg_list)

#Test

test_pos_2 = polarity_feature.Polarity_feature().get_feature(test_pos_list)
test_neg_2 = polarity_feature.Polarity_feature().get_feature(test_neg_list)

"""Data Merger"""

training_data = pre_processing.data_merger(training_pos_labels, training_neg_labels, training_neg_1, training_pos_1
                                           ,training_neg_2, training_pos_2)
test_data = pre_processing.data_merger(test_pos_labels, test_neg_labels, test_neg_1, test_pos_1, test_neg_2, test_pos_2)

"""Decision Tree"""

decision_tree = decision_tree_classifier.Decision_Tree(training_data, test_data)
accuracy = decision_tree.accuracy

print(accuracy)







