# Further Work needs to be done to make it so country and date are displayed

import requests
from bs4 import BeautifulSoup
from toolkit import Toolkit
from newsplease import NewsPlease
import pycountry

# Reports and Studies
fileLocation = '.\\Amman_Center_For_Human_Rights\\Center_News\\Reports_And_Studies\\'
nameQualifier = 'ACHRS_Reports_And_Studies'
linkRequest = requests.get('https://www.achrs.org/english/index.php/center-news-mainmenu-78/data-and-reports-mainmenu-37')
linkSoup = BeautifulSoup(linkRequest.content, features='lxml')
NewsPage = linkSoup.find(class_='blog_more')
NewsPageHrefs = []
for a in NewsPage.find_all('a', href=True):
    NewsPageHrefs.append(a['href'])
for linkFromList in NewsPageHrefs:
    country = 'Unknown'
    date = 'Unknown'
    pageRequest = requests.get('https://www.achrs.org/' + linkFromList)
    pageSoup = BeautifulSoup(pageRequest.content, features='lxml')
    article = NewsPlease.from_html(pageSoup.prettify())
    pageSoup = pageSoup.find('div', class_="article-content")
    title = str(article.title)
    print(title)
    text = str(article.text)
    print(date)
    for country in pycountry.countries:
        if country.name in text:
            countryName = str(country.name)
            print(countryName)
    if pageSoup.find('a', href=True) is None:
        textFileName = Toolkit.textNamingConvention(fileLocation, nameQualifier, countryName, date)
        try:
            Toolkit.textFileCompiler(title, date, textFileName, linkSoup)
        except UnicodeEncodeError:
            pass
    else:
        pdf = 'https://www.achrs.org/' + pageSoup.find('a')['href']
        Toolkit.pdf(fileLocation, nameQualifier, countryName, date, pdf)

# The News
fileLocation = '.\\Amman_Center_For_Human_Rights\\Arab_And_International\\The_News\\'
nameQualifier = 'ACHRS_News'
linkRequest = requests.get('https://www.achrs.org/english/index.php/arab-and-international-mainmenu-45/arab-and-international')
linkSoup = BeautifulSoup(linkRequest.content, features='lxml')
NewsPage = linkSoup.find(class_='blog_more')
NewsPageHrefs = []
for a in NewsPage.find_all('a', href=True):
    NewsPageHrefs.append(a['href'])
for linkFromList in NewsPageHrefs:
    country = 'Unknown'
    date = 'Unknown'
    pageRequest = requests.get('https://www.achrs.org/' + linkFromList)
    pageSoup = BeautifulSoup(pageRequest.content, features='lxml')
    article = NewsPlease.from_html(pageSoup.prettify())
    pageSoup = pageSoup.find('div', class_="article-content")
    title = str(article.title)
    print(title)
    text = str(article.text)
    print(date)
    for country in pycountry.countries:
        if country.name in text:
            countryName = str(country.name)
            print(countryName)
    if pageSoup.find('a', href=True) is None:
        textFileName = Toolkit.textNamingConvention(fileLocation, nameQualifier, countryName, date)
        try:
            Toolkit.textFileCompiler(title, date, textFileName, linkSoup)
        except UnicodeEncodeError:
            pass
    else:
        pdf = 'https://www.achrs.org/' + pageSoup.find('a')['href']
        Toolkit.pdf(fileLocation, nameQualifier, countryName, date, pdf)

# Press Releases
fileLocation = '.\\Amman_Center_For_Human_Rights\\Arab_And_International\\Press_Releases\\'
nameQualifier = 'ACHRS_Press_Releases'
linkRequest = requests.get('https://www.achrs.org/english/index.php/arab-and-international-mainmenu-45/international-news-mainmenu-47')
linkSoup = BeautifulSoup(linkRequest.content, features='lxml')
NewsPage = linkSoup.find(class_='blog_more')
NewsPageHrefs = []
for a in NewsPage.find_all('a', href=True):
    NewsPageHrefs.append(a['href'])
for linkFromList in NewsPageHrefs:
    countryName = 'Unknown'
    date = 'Unknown'
    pageRequest = requests.get('https://www.achrs.org/' + linkFromList)
    pageSoup = BeautifulSoup(pageRequest.content, features='lxml')
    article = NewsPlease.from_html(pageSoup.prettify())
    pageSoup = pageSoup.find('div', class_="article-content")
    title = str(article.title)
    text = str(article.text)
    for country in pycountry.countries:
        if country.name in text:
            countryName = str(country.name)
    if pageSoup.find('a', href=True) is None:
        textFileName = Toolkit.textNamingConvention(fileLocation, nameQualifier, countryName, date)
        Toolkit.textFileCompiler(title, date, textFileName, linkSoup)
    else:
        pdf = 'https://www.achrs.org/' + pageSoup.find('a', href=True)['href']
        Toolkit.pdf(fileLocation, nameQualifier, countryName, date, pdf)

# Reports and Studies
fileLocation = '.\\Amman_Center_For_Human_Rights\\Arab_And_International\\Reports_And_Studies\\'
nameQualifier = 'ACHRS_Reports_And_Studies'
linkRequest = requests.get('https://www.achrs.org/english/index.php/arab-and-international-mainmenu-45/reports-and-studies-mainmenu-49')
linkSoup = BeautifulSoup(linkRequest.content, features='lxml')
NewsPage = linkSoup.find(class_='blog_more')
NewsPageHrefs = []
for a in NewsPage.find_all('a', href=True):
    NewsPageHrefs.append(a['href'])
for linkFromList in NewsPageHrefs:
    country = 'Unknown'
    date = 'Unknown'
    pageRequest = requests.get('https://www.achrs.org/' + linkFromList)
    pageSoup = BeautifulSoup(pageRequest.content, features='lxml')
    article = NewsPlease.from_html(pageSoup.prettify())
    pageSoup = pageSoup.find('div', class_="article-content")
    title = str(article.title)
    print(title)
    text = str(article.text)
    print(date)
    for country in pycountry.countries:
        if country.name in text:
            countryName = str(country.name)
            print(countryName)
    if pageSoup.find('a', href=True) is None:
        textFileName = Toolkit.textNamingConvention(fileLocation, nameQualifier, countryName, date)
        Toolkit.textFileCompiler(title, date, textFileName, linkSoup)
    else:
        pdf = 'https://www.achrs.org/' + pageSoup.find('a')['href']
        Toolkit.pdf(fileLocation, nameQualifier, countryName, date, pdf)
