#!./env/bin/python

import random
import twitter
import json

def stupify(s):
    ns = ""
    for c in s:
        func = random.choice([str.lower, str.upper])
        ns += func(c)
    return(ns)

auth = json.loads(open('auth.json').read())

api = twitter.Api(consumer_key=auth['consumer_key'],
                  consumer_secret=auth['consumer_secret'],
                  access_token_key=auth['access_token_key'],
                  access_token_secret=auth['access_token_secret'])

last_id = open('last.txt').read()
timeline = api.GetUserTimeline(13623532)
last = timeline[0]
if last.id_str == last_id:
    exit()
stupified = stupify(last.text)
api.PostUpdate(stupified, in_reply_to_status_id=last.id, auto_populate_reply_metadata=True)
with open('last.txt', 'w') as out:
    out.write(last.id_str)
