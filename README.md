# pycrawler

This web crawler will crawl a specified website and look for internal links only and then save them to a file.

Requires Pyhon 3 or higher.

Create a python3 virtualenv:

```
virtualenv -p python3 env
```


Please install all the pip requirements as so:

```
pip install -r requirements.txt
```
To run the program:

```
python crawler.py http://yourwebsite.com
```


<h3>How to improve further</h3>

 - Checking for both relative and full path internal links

 - Test that each page can resolve *before* crawling it

 - Use threads to simultaneously crawl many pages

 - Using multiprocessing with Threadpool to also speed up crawling

 - User agents, waits and ip proxying to avoid being blocked

 







