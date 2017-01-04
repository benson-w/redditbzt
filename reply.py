#!/usr/bin/python

import praw 
import pdb 
import re 
import os 

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

# get the top 5 values from our subreddit 
subreddit = reddit.subreddit('pythonforengineers')
for submission in subreddit.hot(limit=10):
    print(submission.title)
    
    #if we haven't replied to this post before, do a case insensitive search
    if submission.id not in posts_replied_to:
        if re.search("i love python", submission.title, re.IGNORECASE):
            #reply to post 
            submission.reply("hey asdkfjsadl;f")
            print("Bot replying to : ", submission.title)

            #store id to our list
            posts_repiled_to.append(submission.id)

#write our update list back to the file 
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:        
        f.write(post_id + "\n")


