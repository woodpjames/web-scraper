import requests
from bs4 import BeautifulSoup
from toolkit import Toolkit
import pycountry

# Latest
# fileLocation = '.\\Anti-Slavery_International\\Latest\\'
# nameQualifier = 'Anti-Slavery_International_Latest'
# page = 1
# bull = True
# while bull:
#     linkRequest = requests.get('https://www.antislavery.org/latest/page/' + str(page) + '/')
#     print(page)
#     linkSoup = BeautifulSoup(linkRequest.content, features='lxml')
#     if linkSoup.find('article') is not None:
#         num = 0
#         NewsPage = linkSoup.find(class_='left-column')
#         NewsPageHrefs = []
#         NewsPageDates = []
#         NewsPageTitles = []
#         for a in NewsPage.find_all('a', rel='bookmark', href=True):
#             NewsPageHrefs.append(a['href'])
#             NewsPageTitles.append(a.text)
#         print(NewsPageHrefs)
#         print(NewsPageTitles)
#         for date in NewsPage.find_all(class_='date'):
#             NewsPageDates.append(date.text)
#         print(NewsPageDates)
#         for link in NewsPageHrefs:
#             country = "Unknown"
#             for place in pycountry.countries:
#                 if place.name in NewsPageTitles[num]:
#                     country = str(place.name)
#             request = requests.get(link)
#             soup = BeautifulSoup(request.content, features='lxml')
#             refinedSoup = soup.find(class_='left-column')
#             Toolkit.text(fileLocation, nameQualifier, NewsPageDates[num], country, NewsPageTitles[num], refinedSoup)
#             num = num + 1
#     else:
#         bull = False
#     page = page + 1
#     print(bull)

# Reports and Resources
fileLocation = '.\\Anti-Slavery_International\\Reports_And_Resources\\'
nameQualifier = 'Anti-Slavery_International_Reports_And_Resources'
linkRequest = requests.get('https://www.antislavery.org/reports-and-resources/')
linkSoup = BeautifulSoup(linkRequest.content, features='lxml')
NewsPage = linkSoup.find(class_='site-main')
for article in NewsPage.find_all(class_='signpost-text'):
    groupHeader = article.h3.text
    print(groupHeader)
    firstHref = article.find('a')['href']
    print(firstHref)
    date = "Unknown"
    country = "unknown"
    for place in pycountry.countries:
        if place.name in groupHeader:
            country = str(place.name)
    request = requests.get(firstHref)
    soup = BeautifulSoup(request.content, features='lxml')
    refinedSoup = soup.find(class_='entry-content')
    if refinedSoup is not None:
        for pdf in refinedSoup.find_all('a'):
            try:
                print(pdf['href'])
                Toolkit.pdf(fileLocation, nameQualifier, country, date, pdf['href'])
            except requests.exceptions.InvalidSchema:
                pass

# Annual Reviews
fileLocation = '.\\Anti-Slavery_International\\Annual_Reviews\\'
nameQualifier = 'Anti-Slavery_International_Annual_Reviews'
linkRequest = requests.get('https://www.antislavery.org/about-us/accounts-and-annual-reviews/')
linkSoup = BeautifulSoup(linkRequest.content, features='lxml')
NewsPage = linkSoup.find(class_='entry-content')
NewsPage = NewsPage.find('ul')
country = "Unknown"
date = "Unknown"
for a in NewsPage.find_all('a'):
    Toolkit.pdf(fileLocation, nameQualifier, country, date, a['href'])
