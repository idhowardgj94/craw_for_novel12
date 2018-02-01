import os
from ebooklib import epub

'''
this module is dependence on ebbokLib.
you can get this module by pip:
pip install ebooklib
'''

class toEpub(object):
    '''
    attributes:
    idxData: indexData object
    conData: contentData object
    book: epub.Epubook() object
    '''
    def __init__(self,idxData, conData ,fileName=None, path=None):
        if path is None:
            self.path = os.getcwd()
        else:
            self.path = path

        if fileName is None:
            self.fileName = idxData.title
        else:
            self.fileName = idxData.title
        global book
        book = epub.EpubBook()

        #set meta data
        book.set_title(idxData.title)
        boook.set_language('en')
        book.add_author(idxData.author)

        #create chapter
        chapterNamber = len(idxData.links)
        for chp in chapterNumber:
            curchp = epub.E
