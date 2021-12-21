import os
import functools
import requests

steps = [
]


# memory_location = os.path.basename(__file__) + '.cache'
# if no state has been cached so far create a new one

def compose(*functions):
    return functools.reduce(lambda f, g: lambda x: f(g(x)), functions, lambda x: x)

url = 'https://phils-strapi.herokuapp.com/api/products/13'

event = requests.get(url).json()['data']['attributes']

filters = compose(
    lambda e: e if e['price'] <= 30 else None,
    lambda e: e if 'open source' in e['description'] else None
)
