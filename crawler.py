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
	for link in soup.find_all('a', attrs={'href': re.compile("^http://")}):
		if "href" in link.attrs:
			print(link)
			#Check if each found link is in the internal_links set and if not add it
			if link.attrs["href"] not in internal_links:
				new_link = link.attrs["href"]
				print(new_link)
				internal_links.add(new_link)
				print("All links found so far, ", internal_links)
				time.sleep(6)
				crawl_bot(new_link)

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('url', help='Pass the website you wish to crawl \
		please include the http://')
	args = parser.parse_args()

	url = args.url


	crawl_bot(url)

if __name__ == '__main__':
	main()








