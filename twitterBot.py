#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, time, tweepy

argfile = str(sys.argv[1])

CONSUMER_KEY = 'or6E5EkRhI3ehTOYb9R1Fs2ah'
CONSUMER_SECRET = 'XKmNTNsvVi4l4eWQ17J7ckFCfHjIDJAt9ioaVypLD0832EPbPu'
ACCESS_KEY = '271432745-wXdu6X77Mb8BRDcuHOiP7Phc8sZPsk8wWfwtKfGt'
ACCESS_SECRET = 'RjbKMJt0MLJgRSSYRmUJX73aiQ0GOM5RSPBzmGkIP8d6V'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


filename = open(argfile, 'r')
f = filename.readlines()
filename.close()

for line in f:
	api.update_status(line)
	time.sleep(60)