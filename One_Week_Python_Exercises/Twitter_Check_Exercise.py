tweet=input("Please enter your tweet here: ")
allowed_tweet_length=140

if len(tweet) <= allowed_tweet_length:
    print(f"That {len(tweet)} character tweet will work!")

else:
    print(f"Your tweet is {len(tweet)-allowed_tweet_length} symbols too long!")