import pandas as pd
import datetime

"""Extracting Stock Related Financials Based on Input"""

def stock_change_day(sym, date_of_article, range):
    set_range = range + 1
    date_list = date_of_article.split("-")
    new_date = "".join(reversed(date_list))
    end_date = datetime.datetime.strptime(new_date, "%d%m%Y").date()
    start_date = end_date - datetime.timedelta(days=set_range)
    request_call = pd.read_json("https://api.iextrading.com/1.0/stock/" + sym + "/chart/3m") #specific request from the IEX API
    main_data = pd.DataFrame(request_call[["date","change", "open", "close", "volume"]]) #initialize the dataframe
    difference = main_data["open"] - main_data["close"]
    difference_list = difference.tolist()
    main_data.insert(loc=5, column = "day change", value = difference_list)
    ranging_board = (main_data['date'] >= str(start_date)) & (main_data['date'] <= str(end_date))
    new = main_data.loc[ranging_board]
    return new


if __name__ == '__main__':
    ticker = "AAPL"
    date = "2019-03-27"
    result = stock_change_day(ticker, date, 5)
    print(result)










