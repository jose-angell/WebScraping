from tweepy import Stream
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler


consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

class MyListener(StreamListener):
    def on_data(self, data):
        try:
            with open('python.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
    
    def on_error(self, status):
        print(status)
        return True
    

twitter_stream = Stream(auth, MyListener())
#busca y almacena todos los tweets nuevos con el #python
twitter_stream.filter(track=['#python'])