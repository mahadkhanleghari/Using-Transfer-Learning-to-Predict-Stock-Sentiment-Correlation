import requests
from textblob import TextBlob
from bs4 import BeautifulSoup
import newspaper
import datetime

"""Extracting Articles, Headlines for Pre-Processing"""

class News_Extractor:

    def __init__(self, company_name, datebased = True,  date = "", interval = 0):
        self.company_name = company_name.lower()
        self.datebased = datebased
        self.date = date
        self.interval_count = interval
        self.date_range = 0
        self.__option__()
        self.papers_list = ["https://www.reuters.com/finance", "https://www.thestreet.com",
                            "https://business.financialpost.com", "https://www.cnbc.com/make-it/money"]

        print("Papers List: ", self.papers_list)

    def google_headliner(self): #extracts all google headlines related to the company
        news_list = ["cnn", "cnbc", "nytimes", "financial", "bloomberg", "reuters"]
        polarity_cumulative = []
        positive_headlines = {}
        negative_headlines = {}
        for news in news_list:
            name = news + " " + self.company_name
            self.company_url = "https://www.google.com/search?q={0}&source=lnms&tbm=nws".format(name)
            result = requests.get(self.company_url)
            initiation = BeautifulSoup(result.text, "html.parser")
            article_headlines = initiation.find_all("div", class_ = "st")
            for title in article_headlines:
                text = TextBlob(title.get_text())
                polarity = text.sentiment.polarity
                if polarity >= 0.5:
                    positive_headlines[polarity] = text
                else:
                    negative_headlines[polarity] = text

                polarity_cumulative.append(polarity)
        pos_count = len(positive_headlines.keys())
        neg_count = len(negative_headlines.keys())
        polarity_aggregate = sum(polarity_cumulative)/len(polarity_cumulative)
        return polarity_aggregate, pos_count, neg_count, positive_headlines, negative_headlines

    def article_extractor(self): #extracts the articles, titles from sources and returns a dict with date as key.
        article_titles_list = []
        article_dates_list = []
        article_text = []
        for major_news in self.papers_list:
            major_news_build = self.__news_built__(major_news)
            print("News Source: %s Total Size: %s\n" % (major_news, major_news_build.size()))
            for article in major_news_build.articles:
                try:
                    article.download()
                    article.parse()
                    article.nlp()
                except:
                    continue
                article_title = (str(article.title)).split(" ")
                check = self.__title_checker__(article_title)
                if self.datebased == True:
                    try:
                        article.publish_date.date()
                    except:
                        continue
                    print(article.publish_date, article.title)
                    if (check == True) and (article.publish_date.date() in self.date_range):
                        article_titles_list.append(article.title)
                        article_text.append(article.text)
                        article_dict = {"Date": str(article.publish_date.date()), "Article Title": str(article.title),
                                        "Article Text": str(article.text)}
                        article_dates_list.append(article_dict)
                        print("Article Title: %s Article Date: %s" % (article.title, article.publish_date))
                else:
                    if check == True:
                        article_titles_list.append(article.title)
                        article_text.append(article.text)
                        print("Article Title: %s Article Date: %s" %(article.title, article.publish_date))

        refined_dict = self.__article_dictizer(article_dates_list)
        return refined_dict

    def __news_built__(self, news):
        built = newspaper.build(news, language='en', memoize_articles=False)
        return built


    def __article_dictizer(self, article_dates_list): #converts the article_prop dict into a date:article, title dict
        refined_article_dict = {}
        for article_properties in article_dates_list:
            date = article_properties["Date"]
            refined_article_dict[date] = {"Titles List": [], "Article Text List": []}
        for dates, values in refined_article_dict.items():
            for ap in article_dates_list:
                if dates == ap["Date"]:
                    values["Titles List"].append(ap["Article Title"])
                    values["Article Text List"].append(ap["Article Text"])
        return refined_article_dict


    def __title_checker__(self, title_list): #checks whether the company name is in the article headline
        refined_list = [word.lower() for word in title_list]
        if self.company_name in refined_list:
            return True
        else:
            return False

    def __date_range_creator__(self, date): #creates a date range for the input date using the interval
        date_list = [date - datetime.timedelta(days= interval) for interval in range(0, self.interval_count)]
        return date_list

    def __option__(self):
        if self.datebased == True:
            refined_date_list = self.date.split("-")
            new_date = "".join(reversed(refined_date_list))
            self.date = datetime.datetime.strptime(new_date, "%d%m%Y").date()
            self.date_range = self.__date_range_creator__(self.date)

    def __open_news_list___(self):
        with open("news_links.txt") as news_file:
            self.papers_list = [link.replace("\n", "") for link in news_file]

if __name__ == '__main__':
    a = News_Extractor("tesla", datebased=True,   date = "2019-04-05", interval = 30)
    c = a.article_extractor()



