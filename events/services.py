"""
@author: Swati Patel
Services module has the methods to send request to the EventBrite API,
process and return the data to the calling methods of the view.

"""
import os
import requests

#constants
EVENTBRITE_URL = 'https://www.eventbriteapi.com/v3/'
def get_categories():
    """
    sends a get request to EventBrite API to retrieve the categories.
    returns dictionary of categories.

    """
    url = EVENTBRITE_URL + 'categories/?token=' + os.environ['EVENTBRITE_TOKEN']
    r = requests.get(url)
    categories = r.json()
    categories_list = {'categories':categories['categories']}
    return categories_list

def get_events(categories, page_no=1):
    """
    sends a get request to EventBrite API to retrieve the events searched by specific categories.
    event search is expanded to include venue and logo.
    arguments:
    categories -- comma separated string of categories include
    page_no -- integer to retrive the specofoc page-paginated response (default 1)

    returns dictionary of events, meta data, categories,
     page_no_list, next_page and previous_page (used for pagination).
    
    """
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
    """
    calculates the list of pages to be shown in pagination

    arguments:
    current_page 
    pages -- total number of pages in the search

    returns a list of page numbers
    """
	start_page = (current_page - 5) if (current_page - 5) > 0 else 1
	end_page = (start_page + 10) if (start_page + 10) < pages else pages
	return list(range(start_page, end_page+1))