import requests
import urllib.parse
from bs4 import BeautifulSoup
from craw.dataLayer.indexData import indexData

class grabIndex(object):
    '''
    Atributes:
    url: URL
    response: recieve request from url
    soup: BeautifulSoup object
    '''
    def __init__(self,url):
        self.url = url;
        self.response = requests.get(url);
        self.soup = BeautifulSoup(self.response.text, 'lxml')

        print('URL: ', self.url)
    def getBookInfo(self, ret=None):
        if ret == None:
            ret = indexData(self.url)

        # set up the checkTable and grab info from website
        # title is another case
        '''
        execTable = {'Title':getTitle, 'author':self.getauthor, 'Genres':self.getGenres,
                    'Series': self.getSeries, 'Published':self.getPublished}
        '''
        matchTable = {'Title':'title', 'Author': 'author', 'Genres': 'genres',
                    'Series': 'series', 'Published': 'published'}

        meta = self.soup.find('div', 'desc')
        setattr(ret, matchTable['Title'], meta.findChild('div', 'title').string)
        #matchTable['Title'] = meta.findChild('div', 'title').string
        infoTable = meta.findChildren('ul')

        '''
        try to store book intro with html tag,
        compare which way is better way
        '''
        setattr(ret, intro, self.sop.find('div', 'mota'))

        for item in infoTable:
            #print(item)
            key=item.findChild('span').string.strip(' :')
            print(type(key))
            if key is not None:
                if key == 'Published':
                    value = item.findChildren('span')[1].string
                    setattr(ret, matchTable[key], value)
                    matchTable[key] = value
                elif item.findChild('a') is not None:
                    value = item.findChild('a').string.strip()
                    setattr(ret, matchTable[key], value)
        return ret

    def getChapterInfo(self, ret=None):
        if ret == None:
            ret = indexData(self.url)
        '''
        ret.topic=self.soup.find('div', id='motaaa').findChild('span').string
        print('book name:', ret.topic)
        '''
        print('start getting the chapter of this book ......')

        #idxContent.findChild('li').findChild('span').string.replace('.', "")
        contents = self.soup.find('ul', 'chuong')
        for content in contents.findChildren('li'):
            #這是章節標題
            chp = content.findChild('a').string

            #這是網址
            link = content.findChild('a').get('href')
            ret.appendLink(chp, link)
        print('getting chapter done.')
        return ret
