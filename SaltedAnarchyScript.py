#!/usr/bin/env python
import sys
from twython import Twython

tweetStr = "Today, my favorite punk group is Operation Ivy. Specifically, I love their song Bombshell."

apiKey = 'mCR8rttzMM1rwWPOwX6bpeqFj'
apiSecret = 'lYUPOd67hRrXbECFGX0eswrgRFmYFYzsexm214GZr0vsDgF7Fm'
accessToken = '778017947461779456-tXFTb3XH6a1lCGm3MuusE3JGT10SmWk'
accessTokenSecret = '0LWKOyD3QXY7qpZHakW03MeE3ru4ni3yyNEMblYvZtMDa'

api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)

api.update_status(status=tweetStr)

print "Tweeted: " + tweetStr
