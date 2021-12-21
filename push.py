import os
import sys
import requests
import json
from pushbullet import Pushbullet

ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
if not ACCESS_TOKEN: sys.exit('no ACCESS_TOKEN found in environment')

pb = Pushbullet(ACCESS_TOKEN)

line = sys.stdin.readline()
event = json.loads(line)

pb.push_link(event["title"],event["url"],event["body"])
