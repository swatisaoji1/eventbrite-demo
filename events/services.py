import os
import requests

#constants
EVENTBRITE_URL = 'https://www.eventbriteapi.com/v3/'
def get_categories():
    url = EVENTBRITE_URL + 'categories/?token=' + os.environ['EVENTBRITE_TOKEN']
    r = requests.get(url)
    categories = r.json()
    categories_list = {'categories':categories['categories']}
    return categories_list