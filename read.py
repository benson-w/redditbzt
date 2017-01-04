#/usr/bin/python

# will only work if python binary is in /usr/bin

import praw 

reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit("dota2")

for submission in subreddit.hot(limit=5):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("-------\n")
    print(dir(submission))
