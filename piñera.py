#!./env/bin/python

import random
import twitter
import json
import sys

def stupify(s):
    ns = []
    lst = s.split(" ")
    for w in lst:
        if w[0] != '@' and not 'http' in w:
            nw = ""
            for c in w:
                func = random.choice([str.lower, str.upper])
                nw += func(c)
            ns.append(nw)

    return(" ".join(ns))

auth = json.loads(open('auth.json').read())

api = twitter.Api(consumer_key=auth['consumer_key'],
                  consumer_secret=auth['consumer_secret'],
                  access_token_key=auth['access_token_key'],
                  access_token_secret=auth['access_token_secret'],
                  tweet_mode= 'extended')

def troll(victim):
    timeline = api.GetUserTimeline(screen_name=victim, include_rts=False)
    victim_last = timeline[0]
    victim_text = victim_last.full_text

    my_last = api.GetReplies()[0]
    my_last_text = my_last.full_text

    stupified = stupify(victim_text)

    if my_last_text.lower() == stupified.lower():
        return

    api.PostUpdate(status=stupified, in_reply_to_status_id=victim_last.id, auto_populate_reply_metadata=True)

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        troll(sys.argv[1])
