import requests
from bs4 import BeautifulSoup
from craw.dataLayer.contentData import contentData

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
        self.contentsData = contentData()
        for chapter, link in data.links.items():
                self.contentsData.addChapter(chapter, self.grabContentText(chapter,
                            data.links[chapter]))
                print(chapter, ' done!')
    def grabContentText(self, chapter, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        article = soup.find('div', 'content wl')
        contents = article.find('div', 'adsfooter').findAllNext('p')

        completedContent = list()
        for content in contents[1].stripped_strings:
            completedContent.append(content)
            completedContent.append("\n\n")
            #print(content)
        return ''.join(completedContent)
