import re
import time
import requests
import argparse
from bs4 import BeautifulSoup

#Set for storing found internal links with no duplicates
internal_links = set()


def crawl_bot(url):


	#Get the first page content with requests and parse with bs4
	html = requests.get(url).text
	soup = BeautifulSoup(html, "html.parser")
	#Find all a href tags
	for link in soup.find_all('a'):
		internal_links.add(link)

	for l in internal_links:
		print(l)
		

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('url', help='Pass the website you wish to crawl')
	args = parser.parse_args()

	url = args.url

	crawl_bot(url)

if __name__ == '__main__':
	main()








