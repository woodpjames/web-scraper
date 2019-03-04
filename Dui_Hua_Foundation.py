import requests
from bs4 import BeautifulSoup
from toolkit import Toolkit

# News
fileLocation = '.\\Dui_Hua_Foundation\\Digest\\'
nameQualifier = 'DHF_Digest'
pageNumber = 1
bull = True
listofTitles = []
listofDates = []
listofHREFS = []
while(bull):
    linkRequest = requests.get('https://duihua.org/category/digest/page/' + str(pageNumber) + '/')
    linkSoup = BeautifulSoup(linkRequest.content, features='lxml').find(class_="row small-up-1 medium-up-2 xlarge-up-3 m-t-35")
    if linkSoup is not None:
        for page in linkSoup.find_all('h3'):
            listofTitles.append(page.text)
            listofHREFS.append(page.find('a')['href'])
        for page in linkSoup.find_all('time'):
            listofDates.append(page.text.strip())
        pageNumber = pageNumber + 1
    else:
        bull = False
x = 0
for link in listofHREFS:
    pageRequest = requests.get(link)
    soup = BeautifulSoup(pageRequest.content, features='lxml').find(class_="column medium-10 large-9 medium-centered")
    title = listofTitles[x]
    date = listofDates[x]
    print(date)
    country = 'unknown'
    Toolkit.text(fileLocation, nameQualifier, date, country, title, soup)
    x = x+1

# Human_Rights_Journal
fileLocation = '.\\Dui_Hua_Foundation\\Human_Rights_Journal\\'
nameQualifier = 'DHF_Journal'
pageNumber = 2007
bull = True
while(bull):
    linkRequest = requests.get('https://www.duihuahrjournal.org/' + str(pageNumber) + '/')
    linkSoup = BeautifulSoup(linkRequest.content, features='lxml')
    print('https://www.duihuahrjournal.org/' + str(pageNumber) + '/')
    if linkSoup.find(class_='date-outer') is not None:
        for articles in linkSoup.find_all(class_='date-outer'):
            date = articles.find(class_='date-header').text
            title = articles.find(class_='post-title entry-title').text
            soup = articles.find(class_='post-body entry-content')
            country = 'unknown'
            Toolkit.text(fileLocation, nameQualifier, date, country, title, soup)
        pageNumber = pageNumber + 1
    else:
        bull = False
    print(pageNumber)


# Press Statements
fileLocation = '.\\Dui_Hua_Foundation\\Press_Statements\\'
nameQualifier = 'DHF_Press_Statements'
pageNumber = 1
bull = True
listofTitles = []
listofDates = []
listofHREFS = []
while(bull):
    linkRequest = requests.get('https://duihua.org/category/press-statement/page/' + str(pageNumber) + '/')
    linkSoup = BeautifulSoup(linkRequest.content, features='lxml').find(class_="row small-up-1 medium-up-2 xlarge-up-3 m-t-35")
    if linkSoup is not None:
        for page in linkSoup.find_all('h3'):
            listofTitles.append(page.text)
            listofHREFS.append(page.find('a')['href'])
        for page in linkSoup.find_all('time'):
            listofDates.append(page.text.strip())
        pageNumber = pageNumber + 1
    else:
        bull = False
    print(pageNumber)
x = 0
for link in listofHREFS:
    pageRequest = requests.get(link)
    soup = BeautifulSoup(pageRequest.content, features='lxml').find(class_="column medium-10 large-9 medium-centered")
    title = listofTitles[x]
    date = listofDates[x]
    print(date)
    country = 'unknown'
    Toolkit.text(fileLocation, nameQualifier, date, country, title, soup)
    x = x+1
