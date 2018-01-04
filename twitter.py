import chances
import tweepy
import os
from os.path import join, dirname
import dotenv

dotenv_path = join(dirname(__file__), '.env')
dotenv.load_dotenv(dotenv_path)

CONSUMER_KEY = os.environ.get("PROBZERO_CONSUMER_KEY")
CONSUMER_SECRET = os.environ.get("PROBZERO_CONSUMER_SECRET")
ACCESS_TOKEN = os.environ.get("PROBZERO_ACCESS_TOKEN")
ACCESS_SECRET = os.environ.get("PROBZERO_ACCESS_SECRET")

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

phrase = chances.randomPhrase()

print("Random phrase: " + phrase)

print("Posting...")

api.update_status(phrase)

print("Posted Successfully!")
