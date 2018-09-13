import pytest
from crawler import crawler


def test_init():
    test = crawler('www.yahoo.com.tw')
    url = test.getUrl()
    assert url == 'www.yahoo.com.tw'
