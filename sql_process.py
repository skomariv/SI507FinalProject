import sqlite3
import search as s

#Creation of tables
conn = sqlite3.connect('tweets.sqlite')
cur = conn.cursor()
cur.execute(""" DROP TABLE queries;
            """)
cur.execute(""" DROP TABLE tweets;
            """)
query_table = """ CREATE TABLE queries (
                query_id INTEGER PRIMARY KEY AUTOINCREMENT,
                query TEXT NOT NULL
              ); """
tweet_table = """ CREATE TABLE tweets (
                query_id INT,
                tweet_id INTEGER PRIMARY KEY AUTOINCREMENT,
                tweet TEXT,
                positive_score REAL,
                negative_score REAL,
                neutral_score REAL,
                compound_score REAL,
                FOREIGN KEY (query_id) REFERENCES query(query_id)
              );"""
conn.execute(query_table)
conn.execute(tweet_table)
print("Tables are ready!")
conn.close()

scores = s.read_csv_to_dicts('tweets_with_scores.csv')
queries = []
tweets = []
for element in scores:
    if element['query'] not in queries:
        queries.append(element['query'])
     # change append statement to exclude element['query'] if you want to run the insert code below.
     # If you are running the update based on select query output, leave it in.
    tweets.append((element['query'], element['text'], element['positive_score'], element['negative_score'], element['neutral_score'], element['compound_score']))

conn = sqlite3.connect('tweets.sqlite')
cur = conn.cursor()
for tweet in tweets:
    cur.execute("INSERT INTO tweets(tweet, positive_score, negative_score, neutral_score, compound_score) VALUES(?, ?, ?, ?, ?)", (tweet[0], tweet[1], tweet[2], tweet[3], tweet[4]))
conn.commit()
for query in queries:
    cur.execute("INSERT INTO queries(query) VALUES(?)", [query])
conn.commit()
conn.close()

conn = sqlite3.connect('tweets.sqlite')
cur = conn.cursor()
for tweet in tweets:
    cur.execute("SELECT query_id FROM queries WHERE query=?", [tweet[0]])
    temp = int(cur.fetchall()[0][0])
    cur.execute("UPDATE tweets SET query_id=? where tweet=?", [temp, tweet[1]])
    conn.commit()
conn.close()