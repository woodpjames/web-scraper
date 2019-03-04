import requests
from bs4 import BeautifulSoup
from toolkit import Toolkit

# HRDs in the News
fileLocation = '.\\Front_Line_Defenders\\Meet_the_Human_Rights_Defenders\\HRDs_in_the_News\\'
nameQualifier = 'FLD_HRDs_in_the_News'
pageNumber = 0
bull = True
listofTitles = []
listofDates = []
listofHREFS = []
while(bull):
    linkRequest = requests.get('https://www.frontlinedefenders.org/en/hrd-in-the-news?page=' + str(pageNumber) + '/')
    linkSoup = BeautifulSoup(linkRequest.content, features='lxml').find(class_="view-content")
    if linkSoup is not None:
        for page in linkSoup.find_all('h3'):
            listofHREFS.append('https://www.frontlinedefenders.org/' + page.find('a')['href'])
            listofTitles.append(page.find('a').text)
        for page in linkSoup.find_all(class_="group-publish-date field-group-div"):
            listofDates.append(page.text)
        pageNumber = pageNumber + 1
    else:
        bull = False
x = 0
for link in listofHREFS:
    pageRequest = requests.get(link)
    soup = BeautifulSoup(pageRequest.content, features='lxml').find(class_="field field-name-body field-type-text-with-summary field-label-hidden")
    title = listofTitles[x]
    date = listofDates[x]
    country = 'Unknown'
    Toolkit.text(fileLocation, nameQualifier, date, country, title, soup)
    x = x+1

# Reports
fileLocation = '.\\Front_Line_Defenders\\Visibility\\Reports\\'
nameQualifier = 'FLD_Reports'
pageNumber = 0
listofTitles = []
listofDates = []
listofHREFS = []
linkRequest = requests.get('https://www.frontlinedefenders.org/en/reports')
linkSoup = BeautifulSoup(linkRequest.content, features='lxml').find(class_="view-content")
if linkSoup is not None:
    for page in linkSoup.find_all('h3'):
        listofHREFS.append('https://www.frontlinedefenders.org/' + page.find('a')['href'])
        listofTitles.append(page.find('a').text)
    for page in linkSoup.find_all(class_="group-publish-date field-group-div"):
        listofDates.append(page.text)
x = 0
for link in listofHREFS:
    pageRequest = requests.get(link)
    title = listofTitles[x]
    date = listofDates[x]
    country = 'Unknown'
    if BeautifulSoup(pageRequest.content, features='lxml').find(class_="button") is not None:
        pdf = 'https://www.frontlinedefenders.org/' + BeautifulSoup(pageRequest.content, features='lxml').find(class_="button")['href']
        Toolkit.pdf(fileLocation, nameQualifier, country, date, pdf, title=title)
    else:
        soup = BeautifulSoup(pageRequest.content, features='lxml').find(class_="field field-name-body field-type-text-with-summary field-label-hidden")
        Toolkit.text(fileLocation, nameQualifier, date, country, title, soup)
    x = x+1

# Statements
fileLocation = '.\\Front_Line_Defenders\\Visibility\\Statements\\'
nameQualifier = 'FLD_Statements'
pageNumber = 0
bull = True
listofTitles = []
listofDates = []
listofHREFS = []
while(bull):
    linkRequest = requests.get('https://www.frontlinedefenders.org/en/statements?page=' + str(pageNumber) + '/')
    linkSoup = BeautifulSoup(linkRequest.content, features='lxml').find(class_="view-content")
    if linkSoup is not None:
        for page in linkSoup.find_all('h3'):
            listofHREFS.append('https://www.frontlinedefenders.org/' + page.find('a')['href'])
            listofTitles.append(page.find('a').text)
        for page in linkSoup.find_all(class_="group-publish-date field-group-div"):
            listofDates.append(page.text)
        pageNumber = pageNumber + 1
    else:
        bull = False
x = 0
for link in listofHREFS:
    pageRequest = requests.get(link)
    soup = BeautifulSoup(pageRequest.content, features='lxml').find(class_="field field-name-body field-type-text-with-summary field-label-hidden")
    if BeautifulSoup(pageRequest.content, features='lxml').find(class_='action-bar-item hrd-status center') is not None:
        secondLink = 'https://www.frontlinedefenders.org/' + BeautifulSoup(pageRequest.content, features='lxml').find(class_='action-bar-item hrd-status center').find('a')['href']
        request = requests.get(secondLink)
        soup = BeautifulSoup(request.content, features='lxml').find(class_="field field-name-field-case-updates field-type-field-collection field-label-hidden")
    title = listofTitles[x]
    date = listofDates[x]
    country = 'Unknown'
    Toolkit.text(fileLocation, nameQualifier, date, country, title, soup)
    x = x+1

# Blog
fileLocation = '.\\Front_Line_Defenders\\Visibility\\Blog\\'
nameQualifier = 'FLD_Blog'
pageNumber = 0
bull = True
listofTitles = []
listofDates = []
listofHREFS = []
while(bull):
    linkRequest = requests.get('https://www.frontlinedefenders.org/en/blog?page=' + str(pageNumber) + '/')
    linkSoup = BeautifulSoup(linkRequest.content, features='lxml')
    if linkSoup.find is not None and (linkSoup.find(class_='pager-current last') is None or pageNumber < int(linkSoup.find(class_='pager-current last').text)):
        for page in linkSoup.find_all('h3'):
            listofHREFS.append('https://www.frontlinedefenders.org/' + page.find('a')['href'])
            listofTitles.append(page.find('a').text)
        for page in linkSoup.find_all(class_="group-publish-date field-group-div"):
            listofDates.append(page.text)
        pageNumber = pageNumber + 1
    else:
        bull = False
x = 0
for link in listofHREFS:
    pageRequest = requests.get(link)
    soup = BeautifulSoup(pageRequest.content, features='lxml').find(class_="field field-name-body field-type-text-with-summary field-label-hidden")
    title = listofTitles[x]
    date = listofDates[x]
    country = 'Unknown'
    Toolkit.text(fileLocation, nameQualifier, date, country, title, soup)
    x = x+1

# FLD_in_the_News
fileLocation = '.\\Front_Line_Defenders\\Visibility\\FLD_in_the_News\\'
nameQualifier = 'FLD_Blog'
listofTitles = []
listofDates = []
listofHREFS = []
linkRequest = requests.get('https://www.frontlinedefenders.org/en/front-line-in-the-news')
linkSoup = BeautifulSoup(linkRequest.content, features='lxml').find(class_="view-content")
for page in linkSoup.find_all('h3'):
    listofHREFS.append('https://www.frontlinedefenders.org/' + page.find('a')['href'])
    listofTitles.append(page.find('a').text)
for page in linkSoup.find_all(class_="group-publish-date field-group-div"):
    listofDates.append(page.text)
x = 0
for link in listofHREFS:
    pageRequest = requests.get(link)
    soup = BeautifulSoup(pageRequest.content, features='lxml').find(class_="field field-name-body field-type-text-with-summary field-label-hidden")
    title = listofTitles[x]
    date = listofDates[x]
    country = 'Unknown'
    Toolkit.text(fileLocation, nameQualifier, date, country, title, soup)
    x = x+1
