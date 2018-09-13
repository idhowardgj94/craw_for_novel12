import requests
import urllib.parse
from bs4 import BeautifulSoup


class crawler(object):
    def __init__(self, url):
        self.__url = url

    def getUrl(self):
        return self.__url


def run(url):
    print("hello, world")
    return 0
    # run the crawler
