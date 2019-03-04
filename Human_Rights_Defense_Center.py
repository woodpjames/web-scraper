import requests
from bs4 import BeautifulSoup
from toolkit import Toolkit

# HRDs in the News
fileLocation = '.\\Human_Rights_Defense_Center\\Annual_Reports\\'
nameQualifier = 'HRDC_Annual_Reports'
pageNumber = 0
bull = True
listofDates = []
listofHREFS = []

linkRequest = requests.get('https://www.humanrightsdefensecenter.org/annual-reports/')
linkSoup = BeautifulSoup(linkRequest.content, features='lxml')
for page in linkSoup.find_all(class_='block'):
    listofHREFS.append('https://www.humanrightsdefensecenter.org/' + page.find('a')['href'])
    listofDates.append(page.text.strip())
x = 0
for link in listofHREFS:
    pageRequest = requests.get(link)
    pdf = link
    date = listofDates[x]
    country = 'Unknown'
    Toolkit.pdf(fileLocation, nameQualifier, country, date, pdf)
    x = x+1

# In the News
fileLocation = '.\\Human_Rights_Defense_Center\\In_the_News\\'
nameQualifier = 'HRDC_In_the_News'
bull = True
listofTitles = []
listofDates = []
listofHREFS = []
linkRequest = requests.get('https://www.humanrightsdefensecenter.org/action/news/#letters-to-editor-or-editorials')
y = 0
for header in BeautifulSoup(linkRequest.content, features='lxml').find_all(class_='article-list'):
    if y != 4 and y != 5:
        for page in header.find_all(class_="article-detail"):
            listofHREFS.append('https://www.humanrightsdefensecenter.org/' + page.find('a')['href'])
            listofTitles.append(page.find('a').text)
            listofDates.append(page.text.strip()[-4:])
    y = y+1
x = 0
for link in listofHREFS:
    pageRequest = requests.get(link)
    soup = BeautifulSoup(pageRequest.content, features='lxml')
    title = listofTitles[x]
    date = listofDates[x]
    country = 'Unknown'
    Toolkit.text(fileLocation, nameQualifier, date, country, title, soup)
    x = x+1

