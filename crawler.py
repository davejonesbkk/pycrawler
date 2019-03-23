import re
import time
import requests
import argparse
from bs4 import BeautifulSoup
from urllib.parse import urlparse

#Sets to hold links when we find them and ones that have been crawled
found_links = set()

crawled_links = set()


def crawl_bot(starting_page, url):


	#Add the current link we are on to both the sets as it has been found and crawled

	found_links.add(url)

	crawled_links.add(url)


	time.sleep(3)

	html = requests.get(url).text
	soup = BeautifulSoup(html, "html.parser")

	links = {link['href'] for link in soup.select("a[href]")}
	for l in links:
		print(l)
	found_links.update(links) 

	#Create a new array consisting of found links that havent been crawled yet
	links_intersect = { i for i in found_links if i in crawled_links}

	print('The links intersect is ', links_intersect)

	for item in found_links:
		print(item)
		#Has the current link been crawled before? 
		if item not in links_intersect:
			#Check if target hostname is in the link and if so crawl it next
			if starting_page.hostname in item: 
				time.sleep(6)
				crawl_bot(starting_page, item)

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('url', help='Pass the website you wish to crawl please include the http://')
	args = parser.parse_args()

	url = args.url

	#Create a coopy of our starting domain to check all internal links against later
	#and parse to get just the hostname
	starting_page = urlparse(url)


	crawl_bot(starting_page, url)

if __name__ == '__main__':
	main()








