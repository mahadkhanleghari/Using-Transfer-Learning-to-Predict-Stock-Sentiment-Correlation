import decision_tree_classifier
import pandas as pd

def data_merger(pos_labels, neg_labels, feature_1_neg, feature_1_pos, feature_2_neg, feature_2_pos,
                feature_3_neg, feature_3_pos):
    labels_list = pos_labels + neg_labels
    feature_1 = feature_1_pos + feature_1_neg
    feature_2 = feature_2_pos + feature_2_neg
    feature_3 = feature_3_pos + feature_3_neg
    head_dict = {"Label": labels_list, "Bag of Words": feature_1, "Polarity": feature_2, "Vader Polarity": feature_3}
    pandas_dataframe = pd.DataFrame(head_dict)
    return pandas_dataframe

pos_labels = [10,20,30,40,5]
neg_labels = [11,22,33,44,5]
feature_1_neg = [1,2,3,4,5]
feature_1_pos = [1,2,3,4,5]
feature_2_neg = [10,20,30,40,50]
feature_2_pos = [10,20,30,40,50]
feature_3_neg = [111,222,333,444,555]
feature_3_pos = [122,211,322,444,554]

new = data_merger(pos_labels, neg_labels, feature_1_neg, feature_1_pos, feature_2_neg, feature_2_pos,
                  feature_3_neg, feature_3_pos)


acc = decision_tree_classifier.Decision_Tree(new, new)