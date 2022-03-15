import tweepy as tw
import os
consumer_key="zQbQfJUTNdbXKqE3gMjpaquog"
consumer_secret="ODYUPPC10o1cPWprXGymEUvZDPERZjacTXypmTtnucbOOOKGeO"
access_token="1003983286685712384-ifoDZU34daaIZ1Hy4S9XGNQgKRJjVV"
access_token_secret="t4XrZl9OGAlZrK29wmgZghQGbXYf35lbXxVBdr3WdQsgR"
auth=tw.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tw.API(auth,wait_on_rate_limit=True)
api.update_status("laliga>premier league")