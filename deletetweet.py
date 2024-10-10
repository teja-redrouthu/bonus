import tweepy
consumer_key = 'ZpDzaMMj2z7ksWaD4FK0e6sz8'
consumer_secret = 'k2For37Wojb52mkjQKBJAUJX0PEzOQ5bdnJQw0scHLzTabW20q'
access_token = '1067655783544872962-gaI60rFoAKI0No5Gj1wSk9ZrAgprl9'
access_token_secret = 'jS1cSBm4IUj3xeqrLHuudeuaXFN6VwikUmD4sFPWDELKO'


bearer_token="AAAAAAAAAAAAAAAAAAAAANNWwQEAAAAAJiF%2BNsV5Ha12W0HvW%2Bvys4n1KaM%3DfaMCTSapcP4a8Kd03iUSrrGZbmOSHUZhHMGyRLS1YBWDNd22qK"

# Authenticate to Twitter using OAuth1
def authenticate_twitter_api():
    auth = tweepy.OAuth1UserHandler(
        consumer_key,
        consumer_secret,
        access_token,
        access_token_secret
    )
    return tweepy.API(auth)

# Function to delete a tweet by its ID
def delete_tweet(api, tweet_id):
    try:
        api.destroy_status(tweet_id)  # Use destroy_status to delete the tweet
        print(f"Tweet with ID {tweet_id} deleted successfully!")

    except tweepy.NotFound:
        print(f"Error: No tweet found with ID {tweet_id}. Please verify the Tweet ID.")
    except tweepy.Forbidden:
        print("Error: You do not have permission to delete this tweet.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Main function to run the deletion process
if __name__ == "__main__":
    api = authenticate_twitter_api()  # Authenticate and create API object
    tweet_id_to_delete = input('Enter the Tweet ID you want to delete: ')  # Prompt for tweet ID
    delete_tweet(api, tweet_id_to_delete)  # Attempt to delete the specified tweet