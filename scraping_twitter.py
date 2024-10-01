import tweepy
from tweepy import OAuthHandler



consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

def process(data):
    print(data)

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth) #punto de entrada para las operaciones con twitter

#lectura de la linea de tiempo de mi propio perfil
for status in tweepy.Cursor(api.home_timeline).items(10):
    process(status.text)

#procesar o almacenar JSON
for status in tweepy.Cursor(api.home_timeline).items(10):
    process(status._json)


#lecctuara de todos los seguidores
for friend in tweepy.Cursor(api.friends).items():
    process(friend._json)

#lista de todos mis tweets
for tweet in tweepy.Cursor(api.user_timeline).items():
    process(tweet)