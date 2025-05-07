# /// script
# dependencies = [
#   "praw",
#    "python-dotenv"
# ]
# ///
import praw
from dotenv import load_dotenv
import os
load_dotenv()
reddit=praw.Reddit(client_id=os.getenv('client_id'),client_secret=os.getenv('client_secret'),user_agent=os.getenv('user_agent'),username=os.getenv('username'),password=os.getenv('password'))
me=reddit.redditor(os.getenv('outuser'))
l=[]
for i in me.comments.hot():
    l.append((i.submission.title,i.submission.author))
print(l)

