from django.shortcuts import render
import os
import events.services as services

# Create your views here.

def home_page(request):
	"""
	retrives the categories and passes them to home page.
	"""
	categories = services.get_categories()
	return render(request, "events/home.html", categories)

def events(request, categories_string='', page_no=1):
	"""
	retrives the events based on categories string and passes them to event page.
	"""
	if request.method == "POST":
		categories_string = ','.join(request.POST.getlist('categories'))
	if categories_string =='':
		categories = services.get_categories()
		return render(request, "events/home.html", categories)
	else:
		events = services.get_events(categories_string, page_no)
		return render(request, "events/events.html", {'data': events})