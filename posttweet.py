import tweepy
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
bearer_token= ''

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
