import os
import sys
import requests
from pushbullet import Pushbullet

ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
if not ACCESS_TOKEN: sys.exit('no ACCESS_TOKEN found in environment')

BASE_URL = 'https://api.pushbullet.com/v2/'
headers = { 'Access-Token': ACCESS_TOKEN }

pb = Pushbullet(ACCESS_TOKEN)
pb.push_note("title","Body")
