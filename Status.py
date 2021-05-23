import tweepy
from Config import config.py

#Con esta linea de codigo, ya autenticado, genero un nuevo tweet.
def NuevoTwit(tweet):
    api = config.create_api()
    api.update_status(tweet)
   
    



