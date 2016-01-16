from django.shortcuts import render
import os
import events.services as services

# Create your views here.

def home_page(request):
	categories = services.get_categories()
	return render(request, "events/home.html", categories)
