import requests
import secrets
import json
import csv

# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = secrets.TWITTER_BEARER_TOKEN

search_url = "https://api.twitter.com/2/tweets/search/recent"

# Optional params: start_time,end_time,since_id,until_id,max_results,next_token,
# expansions,tweet.fields,media.fields,poll.fields,place.fields,user.fields
phrase = 'police brutality'
def create_query_params(phrase):
    query_params = {'query':('place_country: US' 'lang:en') and (f'{phrase} -is:retweet -is:reply')}
    return query_params

query_params = create_query_params(phrase)
def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r

def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()

def write_json(file, text):
    with open(file, 'w', encoding='utf-8') as file_obj:
        json.dump(text, file_obj, ensure_ascii=False, indent=2)

def write_csv_file(output_filepath, dict_to_write, header):
    with open(output_filepath,'w') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for key,val in dict_to_write.items():
            for v in val:
                writer.writerow((key,v))

def read_json(file):
    with open(file, 'r', encoding='utf-8') as file_obj:
        return json.load(file_obj)


def main():
    json_response = connect_to_endpoint(search_url, query_params)
    text = read_json('tweets.json')
    if phrase not in text.keys():
        text[phrase] = []
    for tweet in json_response['data']:
        if tweet['text'] not in text[phrase]:
            text[phrase].append((tweet['text']))
    write_csv_file('tweets.csv', text, ('text', 'query'))


if __name__ == "__main__":
    main()