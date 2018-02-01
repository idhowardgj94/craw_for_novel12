from craw.model.grabIndex import grabIndex

from craw.dataLayer.contentData import contentData
from craw.model.grabContent import grabContent
class craw(object):
    '''
    還沒想好要怎麼用啦~
    atributes:
        url: url of index
    '''
    def __init__(self, url):
        self.url = url
        indexObj=grabIndex(url)
        self.index = indexObj.getChapterInfo()
        self.index = indexObj.getBookInfo(index)
        print('title: ', index.title)
        print('author: ', index.author)
        print('published: ', index.published)
        print('series: ', index.series)
        '''
        next start from here
        '''
        self.centents = grabContent(index)
        for i, j in self.test.contentsData.contents.items():
            print(j)
    def grabFromChapter(self, url):
        pass
    def grabFromIndex(self, url):
        pass
    def outputToTxt(self, fileName, path = './' ):
        pass
