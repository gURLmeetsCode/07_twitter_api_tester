import tweepy

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

# creating an OAuthHandler instance

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Write a tweet to push to our Twitter account
# tweet = 'Hello, world!'
# api.update_status(status=tweet)

# # Using the API object to get tweets from your timeline, and storing it in a variable called public_tweets
# public_tweets = api.home_timeline()
# # foreach through all tweets pulled
# for tweet in public_tweets:
#    # printing the text stored inside the tweet object
#    print tweet.text
# #    you can use the extention below to find spatial data on tweeters. 
#    user.location

# Popular applications of this type of data can include:

# Running analysis on specific users, and how they interact with the world
# Finding Twitter influencers and analyzing their follower trends and interactions
# Monitoring the changes in the followers of a user

# # The Twitter user who we want to get tweets from
# name = "nytimes"
# # Number of tweets to pull
# tweetCount = 20

# # Calling the user_timeline function with our parameters
# results = api.user_timeline(id=name, count=tweetCount)

# # foreach through all tweets pulled
# for tweet in results:
#    # printing the text stored inside the tweet object
#    print tweet.text

# The search term you want to find
query = "Junior Developer"
# Language code (follows ISO 639-1 standards)
language = "en"

# Calling the user_timeline function with our parameters
results = api.search(q=query, lang=language)

# foreach through all tweets pulled
for tweet in results:
   # printing the text stored inside the tweet object
   print tweet.user.screen_name,"Tweeted:",tweet.text
