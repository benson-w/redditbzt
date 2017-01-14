#!/usr/bin/python

import praw 
# import pdb 
import re 
import os 
import random 

ember_quotes = \
[
"Destiny awaits us all.",
"Balance in all things.",
"Flame lights the way.",
"The road is endless.",
"Be wary, be cautious.",
"Harmony must be earned.",
"Walk a warrior's way.",
"Come and learn humility.",
"From knowledge comes skill.",
"Let weakness become strength.",
"Everything lies within nothing. ",
"Greatness in small measures.",
"Let death become peace.",
"Discover what lies beyond"
]

reddit = praw.Reddit('bot1')        # create reddit instance 

# if file doesn't exist, create an empty list
if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []
# else, open the file, take list and each line is an element, throw away empty elements
else:
    with open("posts_replied_to.txt", "r") as f:
        posts_repiled_to = f.read()
        posts_repiled_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))
subreddit = reddit.subreddit('the_perplexing_benson')

#subreddit = reddit.subreddit('dota2')
        
#for submission in subreddit.hot(limit=3):
#    print(submission.title)
    
#   #if we haven't replied to this post before, do a case insensitive search
#    if submission.id not in posts_replied_to:
#        if re.search("wow what a cool subreddit", submission.title, re.IGNORECASE):
#            #reply to post 
#            submission.reply("I am a bot weee; this is a comment")
#            print("Bot replying to : ", submission.title)
#
#            #store id to our list
#            posts_repiled_to.append(submission.id)

for comment in subreddit.stream.comments():
    print(comment.body)
    if re.search("ember give me inspiration", comment.body, re.IGNORECASE):
        areply = random.choice(ember_quotes) + " -Ember Spirit"
        comment.reply(areply)
        print(areply)

#write our update list back to the file 
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:        
        f.write(post_id + "\n")
