from django.test import TestCase
from django.http import HttpRequest

from events.views import  home_page

# Create your tests here.

class homePageViewTest(TestCase):

	def test_home_page_html(self):
		request= HttpRequest()
		response = home_page(request)
		self.assertIn('<title>EventBrite Events</title>', response.content.decode('utf8'))
