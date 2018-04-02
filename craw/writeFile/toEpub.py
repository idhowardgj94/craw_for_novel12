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
            self.fileName = idxData.title + ".epub"
        else:
            self.fileName = fileName

        self.idxData = idxData
        self.conData = conData
    def output(self):
        book = epub.EpubBook()
        #set meta data
        book.set_title(self.idxData.title)
        book.set_language('en')
        book.add_author(self.idxData.author)

        #create chapter
        #chapterNamber = len(idxData.links)

        chapterList=[]
        for chpNum, content in self.conData.contents.items():
            curchap = epub.EpubHtml(title=chpNum, file_name=chpNum+'.xhtml', lang = 'en')
            curchap.content = content
            book.add_item(curchap)
            chapterList.append(curchap)

        chapterTuple = tuple(chapterList)



        intro=epub.EpubHtml(title='book Intro', file_name='bookItroPage.xhtml', lang='en')
        intro.content=self.idxData.intro
        book.add_item(intro)

        #define Table of contents

        book.toc =(
        epub.Link('bookItroPage.xhtml', 'book Introduction','bookintro'),
        (epub.Section('Chapter: '),chapterTuple)
        )

        # add default NCX and Nav file
        book.add_item(epub.EpubNcx())
        book.add_item(epub.EpubNav())

        book.spine = ['nav', intro]


        # define CSS style
        style = 'BODY {color: white;}'
        nav_css = epub.EpubItem(uid="style_nav", file_name="style/nav.css", media_type="text/css", content=style)

        # add CSS file
        book.add_item(nav_css)
        epub.write_epub(self.path+'\\' + self.fileName , book, {})
