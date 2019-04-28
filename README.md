# Stocks_Sentiment_Analysis

***Recommended Environment***:
1. Python 3.7.1
2. Spacy 2.1.3
3. textblob 0.15.3
4. scikit-learn 0.20.3
5. urrlib3
6. newspaper 3k
7. nltk 3.4
8. numpy 1.16.2
9. 0.24.2
10. Vader (Any version)

**Data Set**
IMDB Movie Reviews Data Set (Select Few)

**System**
1. Charlie Main: Requires user input for company and date and returns the range with sentiment. All files are imported into this file. All modules end up here. The user should only be concerned with this file.
2. Beta Main: Just a test file on the optiional webscraper. Serves as the framework for Charlie Main
3. Alpha Main: Calculates the accuracy of the features of IMDB training data on the IMDB test data. 
4. Extract Stocks: It extracts the stock information using the IEX Api
5. Decision Tree Classifier: Labels the data according to the entropy calculations.
6. Pre-Processing: Uses spacy to process the training data and do other operations on test data. 
7. Web-Scraper: Uses newspaper 3k to extract articles and do the Google headline sweep.
8. Textblob Polarity Feature
9. Bag of Words Feature
10. Vader Feature
11. File Creator: Since the training data is in separate files, it is used to concatenate all of the training or test data depending on the input. Use this separately from all the other modules or files. But since the test_neg and the train_neg and the other files in the same format are uploaded, no need to run this.
12. Positive Words: Used for bag of words
13. Negative Words: Used for bag of words
14. Optional: Multiple Polarities
15. Optional: Random Forest Classifier
16. Optional: Scrapping

**Main File Sample Usage**
1. Open Charlie Main
2. Input company name, date and range.
3. It should return a company_name out file and some print statements showing the correlation and the articles and title polarity for the input. 




