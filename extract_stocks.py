import numpy as np
import pandas as pd


def stock_change_day(sym, date_of_article):
    request_call = pd.read_json("https://api.iextrading.com/1.0/stock/" + sym + "/chart/3m") #specific request from the IEX API
    request_call.set_index("date", inplace = True) #Changes the index of the date
    main_data = pd.DataFrame(request_call[["change", "open", "close"]]) #initialize the dataframe
    main_data_reversed = main_data.reindex(index=main_data.index[::-1]) #reverse the sequence of dataframe to extract most recent prices
    print(main_data_reversed.loc[date_of_article])
    change = main_data_reversed.loc[date_of_article, "close"] - main_data_reversed.loc[date_of_article, "open"]
    return change








