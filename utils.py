import BST as BST
import search as s
import json
import plotly.graph_objs as go
from collections import Counter
import re
import spacy

en = spacy.load('en_core_web_sm')

def generate_trees():
    full_tweets = s.read_csv_to_dicts('tweets_with_scores.csv')
    cops = []
    state_violence = []
    police_violence = []
    police_brutality = []
    police_misconduct = []
    for tweet in full_tweets:
        if tweet['query'] == 'cops':
            if tweet['compound_score'] != '0.0':
                cops.append((float(tweet['compound_score']), tweet['text']))
        elif tweet['query'] == 'state violence':
            if tweet['compound_score'] != '0.0':
                state_violence.append((float(tweet['compound_score']), tweet['text']))
        elif tweet['query'] == 'police violence':
            if tweet['compound_score'] != '0.0':
                police_violence.append((float(tweet['compound_score']), tweet['text']))
        elif tweet['query'] == 'police brutality':
            if tweet['compound_score'] != '0.0':
                police_brutality.append((float(tweet['compound_score']), tweet['text']))
        else:
            if tweet['compound_score'] != '0.0':
                police_misconduct.append((float(tweet['compound_score']), tweet['text']))
    cops_tree = BST.BSTNode()
    state_violence_tree = BST.BSTNode()
    police_violence_tree = BST.BSTNode()
    police_brutality_tree = BST.BSTNode()
    police_misconduct_tree = BST.BSTNode()
    for cop in cops:
        cops_tree.insert(cop)
    for state in state_violence:
        state_violence_tree.insert(state)
    for violence in police_violence:
        police_violence_tree.insert(violence)
    for brutality in police_brutality:
        police_brutality_tree.insert(brutality)
    for misconduct in police_misconduct:
        police_misconduct_tree.insert(misconduct)
    return (cops_tree, state_violence_tree, police_violence_tree, police_brutality_tree, police_misconduct_tree)

def input_checker():
    inp = input("Please type the phrase of the subject you are most interested in exploring (options are 'quit', 'cops', 'state violence', 'police violence', 'police brutality', or 'police misconduct'): ")
    if inp not in ('cops', 'state violence', 'police violence', 'police brutality', 'police misconduct', 'quit'):
        print("Looks like that's not one of the valid entries. Remember, your options are 'quit', 'cops', 'state violence', 'police violence', 'police brutality', or 'police misconduct'")
        input_checker()
    if inp == 'quit':
        print("Thanks for interacting with this program! Bye!")
    return inp

def print_bst_to_json(filepath, tree):
    with open(filepath, 'w') as file_obj:
        json.dump(tree.inorder([]), file_obj)

def read_bst_from_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as file_obj:
        return json.load(file_obj)

def get_averages(data, neg, pos):
    for d in data:
        if d[0] < 0:
            neg += d[0]
        else:
            pos += d[0]
    return (neg, pos)

def split_and_filter(desc):
    stop_words = en.Defaults.stop_words
    desc_list = []
    for d in desc:
        desc_list.extend(re.split('\s+', d[1]))
    other_words = ['', 'Cops', 'cops', 'police', 'Police', 'cops.', 'police.', 'ass', 'shit', 'fuck', 'bitch', 'WATCH:', "It's", 'like', 'state', 'State', 'Misconduct', 'brutality.', 'state.', 'Violence', 'violence.', '.', ',', '-', ';']
    desc_filtered = [d for d in desc_list if d.lower() not in stop_words and d.lower() not in other_words]
    count = Counter(desc_filtered)
    return count.most_common(10)