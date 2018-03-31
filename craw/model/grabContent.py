import requests
from bs4 import BeautifulSoup
from craw.dataLayer.contentData import contentData
import sys
class grabContent(object):
    '''
    use to grab the content of story in nove112
    restrict:
    must grab the index first.
    attributes:
    IndexData object
    '''

    def __init__(self, data):
        #data: indexData
        self.data = data
        self.titleNumber = list()


    def grabAllContent(self):
        contentsData = contentData()
        for chapter, link in self.data.links.items():
                contentsData.addChapter(chapter, self.grabContentText(chapter,
                            self.data.links[chapter]))
                print(chapter, ' done!')
        return contentsData
    def grabContentText(self, chapter, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        article = soup.find('div', 'content wl')
        contents = article.find('div', 'adsfooter').findAllNext('p')[1]
        # contents = article.findAll('p')[1];
        # print(contents);
        completedContent = list()
        for content in contents.children:
            # print(content.string);
            completedContent.append(str(content));

        # print(type(contents))
        return ''.join(completedContent)
