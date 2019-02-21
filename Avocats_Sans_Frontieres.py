import requests
from bs4 import BeautifulSoup
from toolkit import Toolkit
import pycountry

# News
fileLocation = '.\\Avocats_Sans_Frontieres\\News\\'
nameQualifier = 'ASF_News'
page = 0
bull = True
flag = False
while bull:
    linkRequest = requests.get('https://www.asf.be/blog/category/news/page/' + str(page) + '/')
    linkSoup = BeautifulSoup(linkRequest.content, features='lxml')
    NewsPage = linkSoup.find(class_='inner white100')
    if NewsPage is None:
        print('false')
        bull = False
    else:
        print('true')
        num = 0
        listOfDates = []
        for date in NewsPage.find_all(class_='column c4x'):
            listOfDates.append(date.find(class_='date').text)
        for article in NewsPage.find_all(class_='inner'):
            link2 = article.find('a')['href']
            title = article.find(class_='teaser').text
            country = 'Unknown'
            for place in pycountry.countries:
                if place.name in title:
                    country = str(place.name)
            link2Request = requests.get(link2)
            link2Soup = BeautifulSoup(link2Request.content, features='lxml')
            if link2Soup.find(class_='post') is not None:
                linkstuff = link2Soup.find(class_='post')
                Toolkit.text(fileLocation, nameQualifier, listOfDates[num], country, title, linkstuff)
            elif link2Soup.find(class_='more downloadpdf') is not None and not flag:
                pdf = link2Soup.find(class_='more downloadpdf')['href']
                Toolkit.pdf(fileLocation, nameQualifier, country, listOfDates[num], pdf)
            num = num + 1
    page = page + 1
    flag = True

# Publications
fileLocation = '.\\Avocats_Sans_Frontieres\\Publications\\'
nameQualifier = 'ASF_Publications'
page = 1
bull = True
while bull:
    linkRequest = requests.get('https://www.asf.be/action/publications/page/' + str(page) + '/')
    linkSoup = BeautifulSoup(linkRequest.content, features='lxml')
    NewsPage = linkSoup.find(id='content')
    if NewsPage.find(class_='inner white100 publi') is None:
        print('false')
        bull = False
    else:
        print('true')
        for article in NewsPage.find_all(class_='inner white100 publi'):
            date = article.find(class_='date').text
            title = article.find('h3').text
            country = 'Unknown'
            for place in pycountry.countries:
                if place.name in title:
                    country = str(place.name)
            pdf = article.find(class_='more alignright downloadpdf')['href']
            Toolkit.pdf(fileLocation, nameQualifier, country, date, pdf)
    page = page + 1
