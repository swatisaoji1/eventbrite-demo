import unittest
from selenium import webdriver

class HomePageTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_home_page(self):
		# Alice hears about this cool website 
		# she visits the website and see the title ''
		self.browser.get('http://localhost:8000')
		self.assertIn ('EventBrite Events' , self.browser.title)

		# she notices a list of checkboxes to chose from
		


		



if __name__ == '__main__':
	unittest.main()