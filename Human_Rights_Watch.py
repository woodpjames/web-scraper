import requests
from bs4 import BeautifulSoup
from toolkit import Toolkit

# Reports
fileLocation = '.\\Human_Rights_Watch\\Reports\\'
nameQualifier = 'CLAIHR_Blog'
pageNumber = 90
bull = True
listofTitles = []
listofDates = []
listofHREFS = []
while(bull):
    linkRequest = requests.get('https://www.hrw.org/publications?page=' + str(pageNumber) + '/')
    print('https://www.hrw.org/publications?page=' + str(pageNumber) + '/')
    linkSoup = BeautifulSoup(linkRequest.content, features='lxml').find(class_="report-body")
    print(linkSoup)
    if linkSoup is not None:
        for page in linkSoup.find_all(class_="report-content"):
            listofHREFS.append('https://www.hrw.org' + page.find('a')['href'])
            listofTitles.append(page.find('a').text)
        for page in linkSoup.find_all('time'):
            listofDates.append(page.text)
        pageNumber = pageNumber + 1
    else:
        bull = False
print('hello')
x = 0
for link in listofHREFS:
    pageRequest = requests.get(link)
    print(link)
    soup = BeautifulSoup(pageRequest.content, features='lxml').find(class_="report-body")
    title = listofTitles[x]
    date = listofDates[x]
    country = 'unknown'
    Toolkit.text(fileLocation, nameQualifier, date, country, title, soup)
    x = x+1
