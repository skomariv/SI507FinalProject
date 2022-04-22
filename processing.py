import pandas as pd
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

#https://gist.github.com/gdatavalley/a6ca071b12a7734f3534600b73a27b1f#file-sentiment_calculation_with_vader-py
df = pd.read_csv('tweet.csv')
analyzer = SentimentIntensityAnalyzer()
df['negative_score'] = [analyzer.polarity_scores(x)['neg'] for x in df['text']]
df['neutral_score'] = [analyzer.polarity_scores(x)['neu'] for x in df['text']]
df['positive_score'] = [analyzer.polarity_scores(x)['pos'] for x in df['text']]
df['compound_score'] = [analyzer.polarity_scores(x)['compound'] for x in df['text']]
df.to_csv('tweets_with_scores.csv')