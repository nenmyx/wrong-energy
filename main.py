import tweepy

class MyStreamListener(tweepy.StreamListener):
	def on_status(self, status):
		print(status.text)

def get_api():
	credsfile = open("CREDENTIALS", "r")
	fullcreds = credsfile.read()
	creds = fullcreds.split("\n")
	credsfile.close()

	auth = tweepy.OAuthHandler(creds[0], creds[1])
	auth.set_access_token(creds[2], creds[3])
	api = tweepy.API(auth)
	return api

api = get_api()

public_tweets = api.home_timeline()
for tweet in public_tweets:
	print(tweet.text)
