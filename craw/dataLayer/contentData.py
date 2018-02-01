class contentData(object):
    '''
    this class define the data structure of 'inside chapter'
    in website https://novel12.com
    Attributes
        chapter: list of chapter number
        content: content
        contents: dictionary of content
    '''
    def __init__(self):
        self.contents = dict({})
        self.chapterList = list()
    def addChapter(self, chapterNumber, content):
        self.chapterList.append(chapterNumber)
        self.contents.update({str(chapterNumber): content})
