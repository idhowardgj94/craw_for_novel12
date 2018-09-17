import pytest
from crawler import Crawler, Information
import re


class TestCrawler(object):
    def test_init(self):
        test = Crawler('https://novel12.com/241169/cirque-du-freak.htm')
        url = test.get_url()
        assert url == 'https://novel12.com/241169/cirque-du-freak.htm'

    def test_init_with_no_arg(self):
        test = Crawler()
        url = test.get_url()
        assert url == None

        # set using setter
        test.set_url('www.yahoo.com.tw')
        url = test.get_url()
        assert url == 'www.yahoo.com.tw'

    def wait_test_grab_info(self):
        test = Crawler()
        a = test.grab_index('https://novel12.com/241169/cirque-du-freak.htm')
        # print(a)
        assert False


class TestInformation(object):
    def set_up(self):
        """ init_soup
        Return
        soup
        """
        self.__soup = Crawler(
            'https://novel12.com/241169/cirque-du-freak.htm').load_url()
        self.__information = Information(self.__soup)

    def test_try_to_get_info_from_ul(self):
        result = {'Author': 'Darren Shan', 'Genres': 'Young Adult',
                  'Series': 'The Saga of Darren Shan #1', 'Published': '4 January 2000'}
        self.set_up()
        self.__information.try_to_get_info_from_ul(
            self.__soup.find(string=re.compile('Author')))
        assert result == self.__information.get_info()

    def test_trim_text(self):
        self.set_up()
        text = self.__information.trim_text('Author :')
        print(text)
        assert text == 'Author'
    # **************************************************
    # below is Feature Test

    def wait_test_get_info(self):
        self.set_up()
        test = Information(self.__soup)
        info = test.get_info()
        assert info['Author'] == 'Darren Shan'
