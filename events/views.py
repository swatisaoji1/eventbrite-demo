from django.shortcuts import render
import os
import events.services as services

# Create your views here.

def home_page(request):
	categories = services.get_categories()
	return render(request, "events/home.html", categories)

def events(request, categories_string='', page_no=1):
	if request.method == "POST":
		categories_string = ','.join(request.POST.getlist('categories'))
	if categories_string =='':
		categories = services.get_categories()
		return render(request, "events/home.html", categories)
	else:
		events = services.get_events(categories_string, page_no)
		return render(request, "events/events.html", {'data': events})