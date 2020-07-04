import tweepy, csv, time
import pandas as pd

#private information

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

tweets = []
query = "sad"

print("starting crawl:",query)

try:
    for tweet in tweepy.Cursor(api.search,q="#"+query,lang="en",since="2017-01-01").items(2000):
        text = tweet.text.replace("&amp;","&").replace(",","").replace("RT","")
        print(text)
        tweets.append(text)
        time.sleep(1e-3)
    pd.DataFrame(tweets).to_csv(query+".csv")
except Exception as e:
    print(e)
    pd.DataFrame(tweets).to_csv(query+".csv")