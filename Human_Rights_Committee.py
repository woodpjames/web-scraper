import requests
from bs4 import BeautifulSoup
from toolkit import Toolkit

# HRDs in the News
fileLocation = '.\\Human_Rights_Committee\\Annual_Reports\\'
nameQualifier = 'HRC_Annual_Reports'
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
