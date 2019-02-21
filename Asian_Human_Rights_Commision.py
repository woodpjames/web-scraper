import requests
from bs4 import BeautifulSoup
from toolkit import Toolkit
import pycountry

fileLocation = '.\\Asian_Human_Rights_Commission\\AHRC_News\\'
nameQualifier = 'AHRC_News'
page = 1
bull = True
while bull:
    linkRequest = requests.get('http://www.humanrights.asia/latest-news/ahrc-news/page/' + str(page) + '/')
    linkSoup = BeautifulSoup(linkRequest.content, features='lxml')
    NewsPage = linkSoup.find(class_='news_item')
    if NewsPage is None:
        bull = False
    else:
        try:
            for article in NewsPage.find_all(class_='row'):
                print()
                if article.find(class_='news_metas') is not None:
                    link2 = article.find('a')['href']
                    title = article.find('a').text
                    date = 'Unknown'
                    for a in article.find(class_='news_metas').find_all('a'):
                        date = a.text
                    date = date.replace(',', '')
                    print(date)
                    country = 'Unknown'
                    if article.find(class_='country'):
                        country = article.find(class_='country').text
                    else:
                        for place in pycountry.countries:
                            if place.name in title:
                                country = str(place.name)
                    link2Request = requests.get(link2)
                    link2Soup = BeautifulSoup(link2Request.content, features='lxml')
                    link2Soup = link2Soup(class_='article_body')
                    Toolkit.text(fileLocation, nameQualifier, date, country, title, linkSoup)
        except requests.exceptions.ConnectionError:
            pass
    page = page + 1

fileLocation = '.\\Asian_Human_Rights_Commission\\Urgent_Appeals\\'
nameQualifier = 'AHRC_Urgent_Appeals'
page = 1
bull = True
while bull:
    linkRequest = requests.get('http://www.humanrights.asia/latest-news/urgent-appeals/page/' + str(page) + '/')
    linkSoup = BeautifulSoup(linkRequest.content, features='lxml')
    NewsPage = linkSoup.find(class_='news_item')
    if NewsPage is None:
        bull = False
    else:
        for article in NewsPage.find_all(class_='row'):
            if article.find(class_='news_metas') is not None:
                link2 = article.find('a')['href']
                title = article.find('a').text
                date = 'Unknown'
                for a in article.find(class_='news_metas').find_all('a'):
                    date = a.text
                print(date)
                country = 'Unknown'
                if article.find(class_='country'):
                    country = article.find(class_='country').text
                else:
                    for place in pycountry.countries:
                        if place.name in title:
                            country = str(place.name)
                link2Request = requests.get(link2)
                link2Soup = BeautifulSoup(link2Request.content, features='lxml')
                link2Soup = link2Soup(class_='article_body')
                Toolkit.text(fileLocation, nameQualifier, date, country, title, linkSoup)
    page = page + 1

fileLocation = '.\\Asian_Human_Rights_Commission\\Press_Releases\\'
nameQualifier = 'AHRC_Press_Releases'
page = 1
bull = True
while bull:
    linkRequest = requests.get('http://www.humanrights.asia/latest-news/press-releases/page/' + str(page) + '/')
    linkSoup = BeautifulSoup(linkRequest.content, features='lxml')
    NewsPage = linkSoup.find(class_='news_item')
    if NewsPage is None:
        bull = False
    else:
        for article in NewsPage.find_all(class_='row'):
            if article.find(class_='news_metas') is not None:
                link2 = article.find('a')['href']
                title = article.find('a').text
                date = 'Unknown'
                for a in article.find(class_='news_metas').find_all('a'):
                    date = a.text
                print(date)
                country = 'Unknown'
                if article.find(class_='country'):
                    country = article.find(class_='country').text
                else:
                    for place in pycountry.countries:
                        if place.name in title:
                            country = str(place.name)
                link2Request = requests.get(link2)
                link2Soup = BeautifulSoup(link2Request.content, features='lxml')
                link2Soup = link2Soup(class_='article_body')
                Toolkit.text(fileLocation, nameQualifier, date, country, title, linkSoup)
    page = page + 1

fileLocation = '.\\Asian_Human_Rights_Commission\\Hunger_Alerts\\'
nameQualifier = 'AHRC_Hunger_Alerts'
page = 1
bull = True
while bull:
    linkRequest = requests.get('http://www.humanrights.asia/latest-news/hunger-alerts/page/' + str(page) + '/')
    linkSoup = BeautifulSoup(linkRequest.content, features='lxml')
    NewsPage = linkSoup.find(class_='news_item')
    if NewsPage is None:
        bull = False
    else:
        for article in NewsPage.find_all(class_='row'):
            if article.find(class_='news_metas') is not None:
                link2 = article.find('a')['href']
                title = article.find('a').text
                date = 'Unknown'
                for a in article.find(class_='news_metas').find_all('a'):
                    date = a.text
                print(date)
                country = 'Unknown'
                if article.find(class_='country'):
                    country = article.find(class_='country').text
                else:
                    for place in pycountry.countries:
                        if place.name in title:
                            country = str(place.name)
                link2Request = requests.get(link2)
                link2Soup = BeautifulSoup(link2Request.content, features='lxml')
                link2Soup = link2Soup(class_='article_body')
                Toolkit.text(fileLocation, nameQualifier, date, country, title, linkSoup)
    page = page + 1

fileLocation = '.\\Asian_Human_Rights_Commission\\ALRC_News\\'
nameQualifier = 'ALRC_News'
page = 1
bull = True
while bull:
    linkRequest = requests.get('http://www.humanrights.asia/latest-news/alrc-news/page/' + str(page) + '/')
    linkSoup = BeautifulSoup(linkRequest.content, features='lxml')
    NewsPage = linkSoup.find(class_='news_item')
    if NewsPage is None:
        bull = False
    else:
        for article in NewsPage.find_all(class_='row'):
            if article.find(class_='news_metas') is not None:
                link2 = article.find('a')['href']
                title = article.find('a').text
                date = 'Unknown'
                for a in article.find(class_='news_metas').find_all('a'):
                    date = a.text
                print(date)
                country = 'Unknown'
                if article.find(class_='country'):
                    country = article.find(class_='country').text
                else:
                    for place in pycountry.countries:
                        if place.name in title:
                            country = str(place.name)
                link2Request = requests.get(link2)
                link2Soup = BeautifulSoup(link2Request.content, features='lxml')
                link2Soup = link2Soup(class_='article_body')
                Toolkit.text(fileLocation, nameQualifier, date, country, title, linkSoup)
    page = page + 1

fileLocation = '.\\Asian_Human_Rights_Commission\\Forwarded_News\\'
nameQualifier = 'Forwarded_News'
page = 1
bull = True
while bull:
    linkRequest = requests.get('http://www.humanrights.asia/latest-news/forwarded-news/page/' + str(page) + '/')
    linkSoup = BeautifulSoup(linkRequest.content, features='lxml')
    NewsPage = linkSoup.find(class_='news_item')
    if NewsPage is None:
        bull = False
    else:
        for article in NewsPage.find_all(class_='row'):
            if article.find(class_='news_metas') is not None:
                link2 = article.find('a')['href']
                title = article.find('a').text
                date = 'Unknown'
                for a in article.find(class_='news_metas').find_all('a'):
                    date = a.text
                print(date)
                country = 'Unknown'
                if article.find(class_='country'):
                    country = article.find(class_='country').text
                else:
                    for place in pycountry.countries:
                        if place.name in title:
                            country = str(place.name)
                link2Request = requests.get(link2)
                link2Soup = BeautifulSoup(link2Request.content, features='lxml')
                link2Soup = link2Soup(class_='article_body')
                Toolkit.text(fileLocation, nameQualifier, date, country, title, linkSoup)
    page = page + 1
