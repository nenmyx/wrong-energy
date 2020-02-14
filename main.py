import tweepy

class TrixTweetListener(tweepy.StreamListener):

	def __init__(self, api):
		self.api = api

	def on_status(self, status):
		#print(status.text)
		text = status.text
		isFiltered = text.startswith("RT") or text.startswith("@") or text.startswith("https://t.co")
		if isFiltered:
			return
		print("tweeting " + text.lower())
		self.api.update_status(text.lower())
	
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
trixTweetListener = TrixTweetListener(api)
trixTweetStream = tweepy.Stream(auth = api.auth, listener=trixTweetListener)
trixTweetStream.filter(follow=["1064620395179925504"])
