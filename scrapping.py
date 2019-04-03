import os
import requests
from bs4 import BeautifulSoup
import datetime
import re

class WebScrapper:

    def __init__(self, weblink, date, companyname, blogname):

        # these variables are used for Financial Post
        self.punctuations = '''!()-[]{};:'"\,.?@#$%^&*_~'''
        self.nextpage = False
        self.store_company_name = ''
        self.store_date = ''
        self.name_of_folder = ''
        self.links_by_finincial_post = []

        # these variables are used for Bloomberg
        self.bloomberg_date = ''


        if blogname == 'financialpost':
            self.__scrap_news_from_financial_post__(weblink, companyname, date)
            self.__scrap_financial_post_blog__()
        elif blogname == 'bloomberg':
            self.__convert_date__(date)
            self.__scrap_news_from_bloomberg__(weblink, companyname, self.bloomberg_date)


    def __createFolder__(self, directory):
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
        except OSError:
            print('Error Creating Directory. ' + directory)

    def __convert_date__(self, date):

        yearmonthday = date.split('-')

        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']

        yearmonthday[1] = months[int(yearmonthday[1]) - 1]

        self.bloomberg_date = yearmonthday[1] + ' ' + yearmonthday[2] + ', ' + yearmonthday[0]

        print(self.bloomberg_date)

    def __scrap_news_from_financial_post__(self, weblink, companyname, articledate):

        counter = 0

        if self.nextpage != False:
            self.store_company_name = companyname
            companyname = ''

        financialpost = weblink + companyname

        if self.nextpage != False:
            companyname = self.store_company_name

        response = requests.get(financialpost)

        soup = BeautifulSoup(response.text, 'html.parser')

        next_page_links = soup.find_all(class_="pagination for-search")

        posts = soup.find_all(itemtype='https://schema.org/NewsArticle')

        length = len(posts)

        for post in posts:
            counter += 1
            title = post.find(class_='entry-title').get_text().replace('\n', '')
            date = post.find(class_='pubdatelong').get_text().replace('\n', '')
            date = date.split(' ', 1)[0]
            date = "".join(date.split())
            self.store_date = date
            tag = post.span
            tag.clear()
            link = post.find('a')['href']
            title_temp = title.lower()
            try:
                if date < articledate:
                    break
                else:
                    index_no = re.search(r'\b({})\b'.format(companyname), title_temp)
                    if index_no.end() > 0:
                        if articledate == date:
                            print(title + '\t' + date + '\n' + link + '\n')
                            self.links_by_finincial_post.append(link)
                        else:
                            print('Not printing due to date not matched!')
            except:
                print('Title didnt matched!')

        if counter == length:

            for next_page_link in next_page_links:
                link = next_page_link.find('a')['href']

            self.nextpage = True
            self.__scrap_news_from_financial_post__(link, companyname, articledate)
        else:
            self.name_of_folder = './' + companyname + '-' + self.store_date + '/'
            self.__createFolder__(self.name_of_folder)
            self.store_company_name = ''
            self.nextpage = False

    def __scrap_financial_post_blog__(self):

        article_no = 0

        for link in self.links_by_finincial_post:
            article_no += 1
            response = requests.get(link)
            soup = BeautifulSoup(response.text, 'html.parser')
            content = soup.find(itemprop="articleBody")

            a_text = content.find_all('p')
            y = [re.sub(r'<.+?>', r'', str(a)) for a in a_text]

            filename = self.name_of_folder + 'article-no-' + str(article_no) + '.txt'
            with open(filename, 'w') as f:
                for para in y:
                    f.write("%s\n" % para)


def main():

    financialpost = 'https://business.financialpost.com/page/1?s='
    #bloomberg = 'https://www.bloomberg.com/search?query=apple+inc&page=1'

    # now = datetime.datetime.now()
    # date = now.strftime("%Y-%m-%d")
    # print(now.strftime("%b-%d-%Y"))

    obj1 = WebScrapper(financialpost, '2019-03-26', 'apple', 'financialpost')
    #obj2 = WebScrapper(bloomberg, '2019-03-26', 'apple', 'bloomberg')


if __name__ == "__main__":
    main()
    # main(sys.argv)




