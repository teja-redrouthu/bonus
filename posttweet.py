import tweepy
consumer_key = 'ZpDzaMMj2z7ksWaD4FK0e6sz8'
consumer_secret = 'k2For37Wojb52mkjQKBJAUJX0PEzOQ5bdnJQw0scHLzTabW20q'
access_token = '1067655783544872962-gaI60rFoAKI0No5Gj1wSk9ZrAgprl9'
access_token_secret = 'jS1cSBm4IUj3xeqrLHuudeuaXFN6VwikUmD4sFPWDELKO'


bearer_token="AAAAAAAAAAAAAAAAAAAAANNWwQEAAAAAJiF%2BNsV5Ha12W0HvW%2Bvys4n1KaM%3DfaMCTSapcP4a8Kd03iUSrrGZbmOSHUZhHMGyRLS1YBWDNd22qK"

# Initialize the client
client = tweepy.Client(
    bearer_token=bearer_token,
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

# Function to post a tweet
def post_tweet(text):
    try:
        response = client.create_tweet(text=text)
        print("Tweet posted successfully.")
    except tweepy.Forbidden as e:
        print("Error: You do not have permission to perform this action.")
        print("Details:", e)

if __name__ == "__main__":
    tweet_text = input("enter the tweeet post:::")


    
    post_tweet(tweet_text)