from craw.model.grabIndex import grabIndex

from craw.dataLayer.contentData import contentData
from craw.model.grabContent import grabContent
from craw.writeFile.toEpub import toEpub
import sys
class craw(object):
    '''
    還沒想好要怎麼用啦~
    atributes:
        url: url of index
    '''
    def __init__(self, url):
        self.url = url

    def grabFromChapter(self):
        '''
        next start from here
        '''
        index = self.index
        contentObj = grabContent(index)

        self.contentsData = contentObj.grabAllContent()
        return self.contentsData
    def grabIndex(self):
        url=self.url
        indexObj=grabIndex(url)
        self.index = indexObj.getChapterInfo()
        self.index = indexObj.getBookInfo(self.index)
        print('title: ', self.index.title)
        print('author: ', self.index.author)
        print('published: ', self.index.published)
        print('series: ', self.index.series)
        return self.index
    def outputToEpub(self, path = None , fileName=None):
        idxData = self.index
        conData = self.contentsData
        outObj = toEpub(idxData, conData)
        outObj.output()
