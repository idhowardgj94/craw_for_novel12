import requests
import urllib.parse
from config import constants
from bs4.element import NavigableString
from bs4.element import Tag
from bs4 import BeautifulSoup
import re


class Crawler(object):
    def __init__(self, url=None):
        self.__url = url
        self.__urlList = []
        self.__root_soup = None
        # if __url is set, than loadUrl
        if self.__url != None:
            self.load_url()

    def load_url(self, url=None):
        """load and return beautifulSoup object

        Keyword argument:
        url -- loading url (default none)
        """
        if url != None:
            self.__url = url
        self.__response = requests.get(self.__url)
        # beautifulsoup object
        self.__root_soup = BeautifulSoup(self.__response.text, 'lxml')

        return self.__root_soup

    def get_url(self):
        return self.__url

    def set_url(self, url):
        self.__url = url
        return self

    def grab_info(self, url=None):
        """ grab info from website(author, title, etc)"""
        if url != None:
            self.__url = url

        # check if __url set
        if self.__url == None:
            return "error"

        self.load_url()

        # try to grab info from web site
        Info = Information(self.__root_soup)
        Info.run()

        return Info

    def grab_index(self, url=None):
        if url != None:
            self.__url = url

        # check if __url set
        if self.__url == None:
            return "error"

        # try to grab index from website

# ----------------------------------------------------


class Information(object):
    def __init__(self, soup):
        self.__soup = soup
        self.__info = {}
        self.__key_dict = {key: None for key in constants.INFO_KEYWORDS}

    def get_info(self):
        return self.__info

    def _get_info_from_website(self):
        """try to get info from website"""
        keywords = constants.INFO_KEYWORDS

        soup = self.__soup
        for keyword in keywords:
            # try to grab content in keyword
            keyword_text = soup.find(string=re.compile(keyword))
            # try to get Author and debug
            self._try_to_get_info_from_ul(keyword_text)

    def _try_to_get_info_from_ul(self, text):
        """try to get info from ul tag
        keywords argument:
            text -- must be beautifulSoup's NavigableString object
        """
        def get_key_value_pair(soup):
            """ try to get key value pair"""
            # go up to li tag
            # and go down to value string
            if type(soup) is NavigableString:
                cur_key = self._trim_text(soup)
                cur_li_key_soup = self._go_up(soup, level)
            elif type(soup) is Tag:
                cur_li_key_soup = soup
                cur_key_untrim = self._go_down(soup, level)
                cur_key = self._trim_text(cur_key_untrim)
            cur_li_value_soup = self._next_sibling(cur_li_key_soup)
            cur_value = self._go_down(cur_li_value_soup, level)
            return cur_key, cur_value
        key_dict = self.__key_dict

        if text in key_dict:
            if key_dict[text] is not None:
                return self
        if text is None:
            return False
        level = None
        # assume search going up 3 level
        # if didn't find li than fail
        for idx, parent in enumerate(text.parents, start=1):
            # find target
            if parent.name == "li":
                # store idx
                level = idx
                break
        # endfor

        # if find li, than start grabing content that match keywords
        if level != None:
            key, value = get_key_value_pair(text)
            print(key, value)
            if key in key_dict:
                key_dict[key] = value

            # try to go next and previos ul to find other info
            # go up to ul
            cur_ul_soup = self._go_up(text, level + 1)
            while self._next_sibling(cur_ul_soup).name == 'ul':
                # get cur soup
                cur_ul_soup = self._next_sibling(cur_ul_soup)
                # try to get key, value pair
                key, value = get_key_value_pair(
                    self._go_down(cur_ul_soup, level + 1))
                if key in key_dict:
                    key_dict[key] = value
            # next check end
            # check prevous
            cur_ul_soup = self._go_up(text, level + 1)
            while self._previous_sibling(cur_ul_soup).name == 'ul':
                # get cur soup
                cur_ul_soup = self._previous_sibling(cur_ul_soup)
                # try to get key, value pair
                key, value = get_key_value_pair(
                    self._go_down(cur_ul_soup, level + 1))
                if key in key_dict:
                    key_dict[key] = value
            self.__info = {key: value for key,
                           value in key_dict.items() if value is not None}
            self.__key_dict = key_dict
            return self
        else:
            return False

    def _go_down(self, soup, level):
        """ return navigableString """
        soup = soup.contents[(level - 1) - 1]
        return soup.string

    def _go_up(self, soup, level):
        """ parameter is navigableString"""
        for iter in range(0, level):
            soup = soup.parent
        return soup

    def _next_sibling(self, soup):
        next_soup = soup.next_sibling
        # next_sibling may be new line char,
        # so if it's true, than read next;
        if next_soup.string == '\n':
            next_soup = next_soup.next_sibling
        return next_soup

    def _previous_sibling(self, soup):
        previous_soup = soup.previous_sibling
        # next_sibling may be new line char,
        # so if it's true, than read next;
        if previous_soup.previous_sibling == '\n':
            previous_soup = previous_soup.previous_sibling
        return previous_soup

    def _trim_text(self, text):
        """trim text to match key_dict's key"""
        text = re.sub(r"[ :,.]*$", '', text)
        return text

    def run(self):
        """ run grab Information """
        self._get_info_from_website()
        pass

# -------------------------------------------------------


class Index(object):
    def __init__(self, soup):
        self.__soup = soup

    def get_keywords(self):
        return self.__keywords


def run(url):
    print("hello, world")
    return 0
    # run the crawler
