# import pandas as pd
# import nltk
# nltk.download('vader_lexicon')
# from nltk.sentiment.vader import SentimentIntensityAnalyzer
# import json
# import csv
import search as s
import re


raw_tweets = s.read_json('raw_tweets.json')
cleaned_tweets = {}
all_keys = set().union(*(tweet.keys() for tweet in raw_tweets))
for key in all_keys:
    if key not in cleaned_tweets.keys():
        cleaned_tweets[key] = []


# analyzer = SentimentIntensityAnalyzer()

tweets = s.read_json('cleaned_tweets.json')
# all_keys = set().union(*(tweet.keys() for tweet in tweets))

cleaned_tweets = {}
for key in tweets.keys():
    if key not in cleaned_tweets.keys():
        cleaned_tweets[key] = []

for tweet in tweets.keys():
    for key in cleaned_tweets.keys():
        if key == tweet:
            for t in tweets[tweet]:
                if t not in cleaned_tweets[key]:
                    t = re.sub(",", "", t)
                    t = re.sub("’", '', t)
                    t = re.sub("&amp;", '', t)
                    t = s.remove_emoji(t)
                    t = t.replace('\n', '')
                    if 'https' in t:
                        t = re.sub('https:\/\/t.co\/\w+', '', t)
                    cleaned_tweets[key].append(t)

s.write_json('cleaned_tweets.json', cleaned_tweets)

#print(analyzer.polarity_scores())