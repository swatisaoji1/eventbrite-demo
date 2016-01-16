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

def get_events(categories, page_no=1):
    url = EVENTBRITE_URL + 'events/search/'
    params = {'token': os.environ['EVENTBRITE_TOKEN'],'categories': categories, 'page' : page_no, 'expand' : 'logo,venue'}
    r = requests.get(url, params)
    events = r.json()
    page_no_list = get_start_page(events['pagination']['page_number'], events['pagination']['page_count'])
    events_list = {	
    				'events' 		: events['events'],
    				'meta'			: events['pagination'],
    				'categories'	: categories,
    				'page_no_list'	: page_no_list,
    				'next_page' 	: events['pagination']['page_number'] + 1,
    				'previous_page' : events['pagination']['page_number'] - 1
    				}
    return events_list

def get_start_page(current_page, pages):
	start_page = (current_page - 5) if (current_page - 5) > 0 else 1
	end_page = (start_page + 10) if (start_page + 10) < pages else pages
	return list(range(start_page, end_page+1))