"""Import Files"""
import pre_processing
import decision_tree_classifier
import bag_of_words_feature
import textblob_polarity_feature
import vader_polarity_feature
import scrapping
import file_creator
import extract_stocks

"""Input"""

news_name = 'financialpost'
news_link = 'https://business.financialpost.com/page/1?s='
date = '2019-03-25'
company_name = 'apple'
company_ticker = "AAPL"
news_result = scrapping.WebScrapper(news_link, date, company_name, news_name)

"""News Pre-Processing"""

news_file = file_creator.file_creator(company_name, date)
news_initiation = pre_processing.Pre_Processing(news_file)
news_list = news_initiation.doc_instance_list

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

article_1 = bag_of_words_feature.Bag_of_words_feature().get_feature(news_list)


"""Feature 2: TextBlob Polarity"""

#Training

training_pos_2 = textblob_polarity_feature.TextBlob_Polarity().get_feature(training_pos_list)
training_neg_2 = textblob_polarity_feature.TextBlob_Polarity().get_feature(training_neg_list)

#Test

article_2 = textblob_polarity_feature.TextBlob_Polarity().get_feature(news_list)


"""Feature 3: Vader Polarity"""

#Training

training_pos_3 = vader_polarity_feature.Vader_polarity().get_feature(training_pos_list)
training_neg_3 = vader_polarity_feature.Vader_polarity().get_feature(training_neg_list)

#Test

article_3 = vader_polarity_feature.Vader_polarity().get_feature(news_list)


"""Data Merger"""

training_data = pre_processing.data_merger(training_pos_labels, training_neg_labels, training_neg_1, training_pos_1
                                           ,training_neg_2, training_pos_2, training_neg_3, training_pos_3)
test_data = pre_processing.article_merger(article_1, article_2, article_3)

"""Decision Tree"""

decision_tree = decision_tree_classifier.Decision_Tree(training_data, test_data)
pos_degree = decision_tree.article_classifier()

print("Positive Degree of Articles for the day is: ",pos_degree)

"Stock Price Change"

change = extract_stocks.stock_change_day(company_ticker, date)

print("Stock Price Fluctuation for the Day:", change)






