#Unit tests for crawler.py


import unittest
from bs4 import BeautifulSoup
import requests
import argparse
from crawler import crawl_bot, check_response, main
from urllib.parse import urlparse

class TestCrawler(unittest.TestCase):
			

	def test_check_response(self):

		url = 'http://example.com'
		check_response(url)
		response = requests.get(url).status_code
		self.assertEqual(response, 200)





if __name__ == '__main__':
	unittest.main()

