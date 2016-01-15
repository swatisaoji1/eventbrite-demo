from django.shortcuts import render
from django.http import HttpResponse
import os

# Create your views here.

def home_page(request):
	return HttpResponse('<title>EventBrite Events</title>')