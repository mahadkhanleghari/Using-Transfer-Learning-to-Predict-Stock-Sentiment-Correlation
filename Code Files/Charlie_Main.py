"""Import Files"""
import pre_processing
import web_scraper
import decision_tree_classifier
import bag_of_words_feature
import textblob_polarity_feature
import vader_polarity_feature
import extract_stocks

"""Input"""

class Charlie_Main:

    def __init__(self, company_name, company_ticker, date = "", interval = 0):
        """Company Attributes"""
        self.company_name = company_name
        self.company_ticker = company_ticker
        self.date = date
        self.interval = interval

        """Scraper Attributes"""
        self.web_scraper_company = web_scraper.News_Extractor(self.company_name,
                                                         datebased=True, date=self.date, interval=self.interval)
        self.google_sweep = self.web_scraper_company.google_headliner()
        self.extract_articles = self.web_scraper_company.article_extractor()
        self.date_dict = pre_processing.Date_Dict_Pre_Processing(self.extract_articles)
        self.date_articles = self.date_dict.date_dict_article_doc
        self.date_title = self.date_dict.date_dict_title_doc

        """Training Attributes"""
        self.training_pos_labels = []
        self.training_pos_1 = []
        self.training_neg_labels = []
        self.training_neg_1 = []
        self.training_pos_2 = []
        self.training_neg_2 = []
        self.training_pos_3 = []
        self.training_neg_3 = []

        """Test Attributes"""
        self.date_polarity = {}
        self.date_title_polarity = {}
        self.interest = {}

        """Financial Attributes"""
        self.pandas_dataframe = self.__extract_financials__()

        """Method Calls"""

        self.__training__()
        self.__test_simulation__()

        """Final Output"""
        self.frame = pre_processing.output_frame(self.date_polarity, self.date_title_polarity, self.interest ,self.pandas_dataframe
                                                 , default=0.1, title_default=0.02, interest_default=0)
        self.frame.to_csv((str(company_name) + "_data.csv"), encoding= "utf-8", index = False)
        print(self.frame)
        self.correlation = self.__correlation__()
        print(self.correlation)
        self.__google_scrape__()

    def __training__(self): #performs all training computation on the IMDB movies dataset
        training_pos = pre_processing.Pre_Processing("train_pos.txt")
        training_pos_list = training_pos.doc_instance_list
        self.training_pos_labels = training_pos.instance_labels
        self.training_pos_1 = bag_of_words_feature.Bag_of_words_feature().get_feature(training_pos_list)

        training_neg = pre_processing.Pre_Processing("train_neg.txt")
        training_neg_list = training_neg.doc_instance_list
        self.training_neg_labels = training_neg.instance_labels
        self.training_neg_1 = bag_of_words_feature.Bag_of_words_feature().get_feature(training_neg_list)

        self.training_pos_2 = textblob_polarity_feature.TextBlob_Polarity().get_feature(training_pos_list)
        self.training_neg_2 = textblob_polarity_feature.TextBlob_Polarity().get_feature(training_neg_list)

        self.training_pos_3 = vader_polarity_feature.Vader_polarity().get_feature(training_pos_list)
        self.training_neg_3 = vader_polarity_feature.Vader_polarity().get_feature(training_neg_list)

    def __test_simulation__(self): #for every date, does a date wise test decision tree polarity calculation
        for date, article_list in self.date_articles.items():
            interest = len(article_list)
            self.interest[date] = interest
            article_1 = bag_of_words_feature.Bag_of_words_feature().get_feature(article_list)
            article_2 = textblob_polarity_feature.TextBlob_Polarity().get_feature(article_list)
            article_3 = vader_polarity_feature.Vader_polarity().get_feature(article_list)
            data_merged = self.__data_merger__(self.training_pos_labels, self.training_neg_labels, self.training_neg_1,
                                               self.training_pos_1, self.training_neg_2, self.training_pos_2,
                                               self.training_neg_3, self.training_pos_3, article_1, article_2, article_3)
            training_data = data_merged[0]
            test_data = data_merged[1]
            positive_degree = self.__decision_tree__(training_data, test_data)
            self.date_polarity[date] = positive_degree

        for date, titles_list in self.date_title.items():
            average_title_polarity = textblob_polarity_feature.TextBlob_Polarity()
            average_pol = average_title_polarity.get_polarity(titles_list)
            self.date_title_polarity[date] = average_pol

    def __data_merger__(self, training_pos_labels, training_neg_labels, training_neg_1, training_pos_1,
                        training_neg_2, training_pos_2, training_neg_3, training_pos_3, article_1, article_2,
                        article_3): #merges data for the test and training set to be used
        training_data = pre_processing.data_merger(training_pos_labels, training_neg_labels, training_neg_1,
                                                   training_pos_1
                                                   , training_neg_2, training_pos_2, training_neg_3, training_pos_3)
        test_data = pre_processing.article_merger(article_1, article_2, article_3)

        return training_data, test_data

    def __decision_tree__(self, training_data, test_data):
        decision_tree = decision_tree_classifier.Decision_Tree(training_data, test_data)
        pos_degree = decision_tree.article_classifier()
        return pos_degree

    def __extract_financials__(self): #extracts the date wise and range wise financial info
        result = extract_stocks.stock_change_day(self.company_ticker, self.date, self.interval)
        return result

    def __correlation__(self): #calculates different sorts of calculation
        day_change_correlation = self.frame["day change"].corr(self.frame["Articles Polarity"])
        change_correlation = self.frame["change"].corr(self.frame["Articles Polarity"])
        open_correlation = self.frame["open"].corr(self.frame["Articles Polarity"])
        close_correlation = self.frame["close"].corr(self.frame["Articles Polarity"])
        volume_mention_correlation = self.frame["volume"].corr(self.frame["Interest"])

        correlation_dict = {"Day Change - Articles": day_change_correlation,
                            "Change - Articles": change_correlation,
                            "Open - Articles": open_correlation,
                            "Close - Articles": close_correlation,
                            "Volume - Mention": volume_mention_correlation}
        return correlation_dict

    def __google_scrape__(self):
        average = self.google_sweep[0]
        pos = self.google_sweep[1]
        neg = self.google_sweep[2]
        pos_head = self.google_sweep[3]
        neg_head = self.google_sweep[4]
        print("The Average Polarity on Google Headline Sweep is: %0.2f" % average)
        print("The Positive Headlines Count: %d The Negative Headline Count: %d" % (pos, neg))
        print("The Positive Headlines")
        for p_head in pos_head:
            print(p_head, pos_head[p_head])
        for n_head in neg_head:
            print(n_head, neg_head[n_head])


if __name__ == '__main__':
    company = "tesla"
    ticker = "TSLA"
    date = "2019-04-05"
    interval = 5
    baseline = Charlie_Main(company, ticker, date, interval)



















