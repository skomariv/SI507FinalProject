# Twitter Sentiment Analysis on topics related to the Police

### Libraries neeeded to interact with program on user end: plotly, spacy, re
### Libraries needed to interact with program on back end: requests, pandas, nltk, nltk.sentiment.vader

### In order to run the `search.py` file, download the `secrets.py` file under my Canvas submission which contains necessary API keys.

### In order to run program from command line, type: `python3 main.py`.

### When interacting with the program, you can look at specific analytics related to the queried tweets of 5 topics:

1. Cops
2. Police Brutality
3. Police Violence
4. State Violence
5. Police Misconduct

Regardless of the query you choose to look at, you will be provided with a graph comparing the average positive/negative compound valuation score of each query's sample of 200 tweets. The maximum range is (-1, 1). 

If you are interested in changing the 200 tweets that have been used as the sample size for each query, you must first run `python3 search.py`, then `python3 processing.py`, and finally `python3 main.py` once again.

## BST Description
Each individual tweet, its query, and its compound score (given by the NLTK classifier) is saved as a tuple (excluding the query). Each tuple is now a node. There are 5 BSTs, one for each query. The BST ordering is decided by the compound score (so the compound score that is considered to be the root will be the tweet with the most extreme negative or positive compound score). The BSTNode class in `BST.py` has the methods necessary for insertion, initialization, and in-order traversal.
