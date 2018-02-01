import urllib.parse
class indexData(object):
    '''
    this class define the data structure of index data, which means
    the index content in website:
    https://novel12.com
    Attributes:
        url: index url of the website
        links: dictionary, 'chapter number', 'link'
        title: title of this book
        author: author of the book
        genres: genres of the book
        series: series of the book
        published: published day
        intro: intro of the book
        chapterList
    '''
    def __init__(self, url):
        nullMessage = 'No info'
        self.url = url
        self.title = nullMessage
        self.author = nullMessage
        self.genres = nullMessage
        self.series = nullMessage
        self.published = nullMessage
        self.links = dict({})
        self.chapterList = list()
        self.intro = nullMessage
    def appendLink(self, chapter, link):
        link = self.mergeLink(link)
        self.chapterList.append(chapter)
        self.links.update({str(chapter): link})
    def mergeLink(self, link):
        return urllib.parse.urljoin(self.url, link)
