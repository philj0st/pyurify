import requests
import json

# all games/consoles listings
api_url = "https://api.anibis.ch/v3/de/"
listings_url = "https://api.anibis.ch/v3/de/search/listings?cun=games-spielkonsolen"
latest_url = "https://api.anibis.ch/v3/de/listings/latests"

detail_url = "https://api.anibis.ch/v3/de/listings/41160353"

def get_listings():
    response = requests.get(latest_url)
    return response.json()


# store the x most recent entries to detect new ones
memory_size = 3
memory = [hash(json.dumps(listing, sort_keys=True)) for listing in get_listings()[:memory_size]]

import time
import sys

while True:
    new_listings = list()
    # get latest listings
    for listing in get_listings():
        # once we encounter previously known, stop
        hsh = hash(json.dumps(listing, sort_keys=True))
        if hsh in memory:
            break

        new_listings.append(listing)

        # remember new listing
        memory.pop()
        memory = [hsh]+memory

    for new_listing in new_listings:
        line = "I found a new one!\n"
        sys.stdout.write(line)
        sys.stdout.write(new_listing['title']+'\n')
        sys.stdout.flush()
    time.sleep(9)
