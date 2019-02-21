import requests
from bs4 import BeautifulSoup
from toolkit import Toolkit
import pycountry

# fileLocation = '.\\Asian_Center_For_Human_Rights\\Press-Releases\\'
# nameQualifier = 'Asian-Center_For_Human_Rights_Press-Releases'
# linkRequest = requests.get('http://www.achrweb.org/press-releases/')
# linkSoup = BeautifulSoup(linkRequest.content, features='lxml')
# NewsPage = linkSoup.find(class_="content-area")
# for ul in NewsPage.find_all('ul'):
#     for a in ul.find_all('a'):
#         try:
#             linkRequest = requests.get(a['href'])
#             print(a['href'])
#             linkSoup = BeautifulSoup(linkRequest.content, features='lxml')
#             if linkSoup.find(class_='entry-title') is not None:
#                 title = linkSoup.find(class_='entry-title').text
#                 date = linkSoup.find('time').text
#                 country = "Unknown"
#                 for place in pycountry.countries:
#                     if place.name in title:
#                         country = str(place.name)
#                 linkSoup = linkSoup.find(class_='entry-content')
#                 print(title)
#                 print(date)
#                 print(country)
#                 Toolkit.text(fileLocation, nameQualifier, date, country, title, linkSoup)
#         except requests.exceptions.MissingSchema:
#             pass
#
# # Programmes
# fileLocation = '.\\Asian_Center_For_Human_Rights\\Programmes\\'
# nameQualifier = 'Asian-Center_For_Human_Rights_Programmes'
# page = 1
# bull = True
# while bull:
#     linkRequest = requests.get('http://www.achrweb.org/category/programme/page/' + str(page) + '/')
#     linkSoup = BeautifulSoup(linkRequest.content, features='lxml')
#     NewsPage = linkSoup.find(class_='content-area')
#     if NewsPage.find('article') is None:
#         bull = False
#     for article in NewsPage.find_all('article'):
#         date = article.find('time').text
#         title = article.find(class_='entry-title').text
#         link2 = article.find('a')['href']
#         country = "Unknown"
#         for place in pycountry.countries:
#             if place.name in title:
#                 country = str(place.name)
#         link2Request = requests.get(link2)
#         link2Soup = BeautifulSoup(link2Request.content, features = 'lxml')
#         link2Soup = link2Soup(class_='entry-content')
#         Toolkit.text(fileLocation, nameQualifier, date, country, title, linkSoup)
#     page = page + 1

# Publications
fileLocation = '.\\Asian_Center_For_Human_Rights\\Publications\\'
nameQualifier = 'Asian-Center_For_Human_Rights_Publications'
page = 1
bull = True
while bull:
    linkRequest = requests.get('http://www.achrweb.org/category/publications/page/' + str(page) + '/')
    linkSoup = BeautifulSoup(linkRequest.content, features='lxml')
    NewsPage = linkSoup.find(class_='content-area')
    if NewsPage.find('article') is None:
        bull = False
    for article in NewsPage.find_all('article'):
        date = article.find('time').text
        title = article.find(class_='entry-title').text
        link2 = article.find('a')['href']
        print(date)
        print(title)
        country = "Unknown"
        for place in pycountry.countries:
            if place.name in title:
                country = str(place.name)
        link2Request = requests.get(link2)
        link2Soup = BeautifulSoup(link2Request.content, features='lxml')
        link2Soup = link2Soup.find(class_='entry-content')
        pdf = link2Soup.find('a', target="_blank")['href']
        try:
            Toolkit.pdf(fileLocation, nameQualifier, country, date, pdf)
        except requests.exceptions.MissingSchema:
            pass
    page = page + 1
