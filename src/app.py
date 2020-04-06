import boto3
import tweepy
import os
import json

ssm = boto3.client('ssm', region_name='us-east-1')


def authenticate_twitter():

    access_token=os.environ['access_token']
    access_token_secret=os.environ['access_token_secret']
    consumer_key=os.environ['consumer_key']
    consumer_secret=os.environ['consumer_secret']
       
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    return api

def retweet(api, search, numberOfTweets):
    
    for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
        try:
            tweet_id = tweet.id
            print("ID = " + tweet_id)
            # Create a tweet
            api.update_status("Hello Tweepy")
            print("Hello Tweepy")
            if tweet.lang == "en":
                #print(tweet.body)
                tweet.retweet()
                print('Retweeted the tweet')
            else:
                print('no retweet')
        except tweepy.TweepError as e:
            print(e.reason)
        except StopIteration:
            break


def lambda_handler(event, context):
    try:     
        apiuse = authenticate_twitter()
        
        searchString = os.environ['TweetSearchString']
        
        numberOfTweets = 5
        print('String to look for: {0} and nb of tweets to retrieve: {1}'.format(searchString,numberOfTweets))
        
        retweet(apiuse, searchString, numberOfTweets)

    except Exception as e:
        print(e)
    
    return {
        "statusCode": 200,
        "body": json.dumps(
            {"message": "TwitterPoller"}
        ),
    }
