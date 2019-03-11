# from .venv.auth import (
#     consumer_key,
#     consumer_secret,
#     access_token,
#     access_token_secret
# )

import json

from twython import Twython


secrets = {}
with open('../.venv/auth.json') as json_file:  
    json_secrets = json.load(json_file)

    secrets['consumer_key'] = json_secrets['consumer_key']
    secrets['consumer_secret'] = json_secrets['consumer_secret']
    secrets['access_token'] = json_secrets['access_token']
    secrets['access_token_secret'] = json_secrets['access_token_secret']

twitter = Twython(
    secrets['consumer_key'],
    secrets['consumer_secret'],
    secrets['access_token'],
    secrets['access_token_secret'],
)

mentions = twitter.get_mentions_timeline()

print(mentions)        