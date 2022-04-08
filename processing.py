import pandas as pd
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import json
import csv




analyzer = SentimentIntensityAnalyzer()


#print(analyzer.polarity_scores())