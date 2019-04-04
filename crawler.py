import re
import time
import requests
import argparse
from bs4 import BeautifulSoup
from urllib.parse import urlparse

#Sets to hold links when we find them and ones that have been crawled
found_links = set()

crawled_links = set()

user_agents = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/602.2.14 (KHTML, like Gecko) Version/10.0.1 Safari/602.2.14',
                 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
                 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.98 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36',
                 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0']


user_agent = {'User-agent': 'Mozilla/5.0'}


def check_response(url):

	UA = random.choice(user_agents)

	print(UA)

	#Check url is valid and returns a http response

	response = requests.get(url, headers= user_agent)

	print(url, 'HTTP response is ', response.status_code, 'site is crawlable, continuing')

	if response.status_code != 200:
		print('Target site is not returning a 200 response code, please check the url')
	else:
		#Create a copy of our starting domain to check all internal links against later
		#and parse to get just the hostname
		starting_page = urlparse(url)

		crawl_bot(starting_page, url)


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

	print('The current links intersect is ', links_intersect)

	for item in found_links:
		print(item)
		#Has the current link been crawled before? 
		if item not in links_intersect:
			#Check if target hostname is in the link and if so crawl it next
			if starting_page.hostname in item: 
				print("Writing ", item, " to file")
				with open('links-file', 'a') as f:
					f.write("%s, \n" % item)
					time.sleep(6)
					crawl_bot(starting_page, item)

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('url', help='Pass the website you wish to crawl please include the http://')
	args = parser.parse_args()

	url = args.url


	check_response(url)

if __name__ == '__main__':
	main()








