import tweepy

# TODO:
# -Set up stream listening on Trixie's glorious tweets
class TrixTweetListener(tweepy.StreamListener):

	def on_status(self, status):
		print(status.text)
	
	def on_error(self, status_code):
		if status_code == 420:
			# Disconnect the stream
			return False

		# Otherwise reconnect with back-off

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
trixTweetListener = TrixTweetListener()
trixTweetStream = tweepy.Stream(auth = api.auth, listener=trixTweetListener)
#trixTweetStream.filter(follow=["1064620395179925504"])
# Using my (@nenmyx) ID for now
trixTweetStream.filter(follow=["1102775856722780161"])
