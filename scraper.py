# /// script
# dependencies = [
#   "praw",
#    "python-dotenv"
# ]
# ///
import praw
from dotenv import load_dotenv
import os
import csv
from fns import get_body
load_dotenv()
reddit=praw.Reddit(client_id=os.getenv('client_id'),client_secret=os.getenv('client_secret'),user_agent=os.getenv('user_agent'),username=os.getenv('username'),password=os.getenv('password'))
usr=reddit.redditor(os.getenv('outuser'))
sub=reddit.subreddit(os.getenv('subname'))
d={}
for subs in sub.new(limit=2000):
    if subs.title in d:
        d[subs.title]=max(d[subs.title],subs.upvote_ratio)
    else:
        d[subs.title]=subs.upvote_ratio

f=open(sub.display_name+".csv",'w')
cw=csv.writer(f)
for i in d:
    cw.writerow([i,d[i]])
f.close()