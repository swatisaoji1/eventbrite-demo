from django.test import TestCase
from django.http import HttpRequest

from events.views import  home_page
from events.services import get_categories

# Create your tests here.

class homePageViewTest(TestCase):

	def test_home_page_html(self):
		request= HttpRequest()
		response = home_page(request)
		self.assertIn('<title>EventBrite Events</title>', response.content.decode('utf8'))

	def test_services_get_categories(self):
		categories = get_categories()
		self.assertIsNotNone(categories)

	def test_home_has_categories(self):
		request= HttpRequest()
		response = home_page(request)
		self.assertIn('<div class="checkbox">', response.content.decode('utf8'))