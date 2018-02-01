from craw.model.grabIndex import grabIndex

from craw.dataLayer.contentData import contentData
from craw.model.grabContent import grabContent
from craw.writeFile.toEpub import toEpub
class craw(object):
    '''
    還沒想好要怎麼用啦~
    atributes:
        url: url of index
    '''
    def __init__(self, url):
        self.url = url

    def grabFromChapter(self, index = None):
        '''
        next start from here
        '''
        if index is None:
            index = self.index

        contentObj = grabContent(index)
        self.contentsData = contentObj.grabAllContent()
        '''
        for i, j in self.contentsData.contents.items():
            print(j)
        '''

        return self.contentsData
    def grabIndex(self, url=None):
        if url is None:
            url=self.url
        indexObj=grabIndex(url)
        self.index = indexObj.getChapterInfo()
        self.index = indexObj.getBookInfo(self.index)
        print('title: ', self.index.title)
        print('author: ', self.index.author)
        print('published: ', self.index.published)
        print('series: ', self.index.series)
        return self.index
    def outputToTxt(self, idxData=None , conData=None , path = None , fileName=None):
        if idxData is None:
            idxData = self.index
        if conData is None:
            conData = self.contentsData

        outObj = toEpub(idxData, conData)
        outObj.output()
