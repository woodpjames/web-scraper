import requests
from bs4 import BeautifulSoup
from toolkit import Toolkit

# News
fileLocation = '.\\Doctors_Without_Borders\\News_and_Stories\\'
nameQualifier = 'DWB_News_and_Stories'
pageNumber = 0
bull = True
listofTitles = []
listofDates = []
listofHREFS = []
while(bull):

    linkRequest = requests.get('https://www.doctorswithoutborders.org/what-we-do/news-stories?search_api_fulltext=&page=' + str(pageNumber) + '/')
    linkSoup = BeautifulSoup(linkRequest.content, features='lxml').find(class_="views-element-container")
    if linkSoup.find(class_='views-row') is not None:
        for page in linkSoup.find_all(class_="search-result__title"):
            listofTitles.append(page.text)
        for page in linkSoup.find_all(class_="search-result__time"):
            listofDates.append(page.text.strip()[2:])
        for page in linkSoup.find_all(class_="search-result search-result--node search-result--Story"):
            listofHREFS.append(page.find('a')['href'])
        pageNumber = pageNumber + 1
    else:
        bull = False
x = 772
for link in listofHREFS[773:]:
    pageRequest = requests.get('https://www.doctorswithoutborders.org' + link)
    soup = BeautifulSoup(pageRequest.content, features='lxml').find(class_="field__item")
    title = listofTitles[x]
    date = listofDates[x]
    country = 'unknown'
    Toolkit.text(fileLocation, nameQualifier, date, country, title, soup)
    x = x+1

# Research
fileLocation = '.\\Doctors_Without_Borders\\Research\\'
nameQualifier = 'DWB_Research'
pageNumber = 0
bull = True
listofTitles = []
listofDates = []
listofHREFS = []
while(bull):
    linkRequest = requests.get('https://www.doctorswithoutborders.org/what-we-do/research?search_api_fulltext=&page=' + str(pageNumber) + '/')
    linkSoup = BeautifulSoup(linkRequest.content, features='lxml').find(class_="views-element-container")
    if linkSoup.find(class_='views-row') is not None:
        for page in linkSoup.find_all(class_="search-result__title"):
            listofTitles.append(page.text)
        for page in linkSoup.find_all(class_="search-result__time"):
            listofDates.append(page.text.strip()[2:])
        for page in linkSoup.find_all(class_="search-result search-result--node search-result--Research"):
            listofHREFS.append(page.find('a')['href'])
        pageNumber = pageNumber + 1
    else:
        bull = False
x = 0
for link in listofHREFS:
    pageRequest = requests.get('https://www.doctorswithoutborders.org' + link)
    soup = BeautifulSoup(pageRequest.content, features='lxml').find(class_="field__item")
    title = listofTitles[x]
    date = listofDates[x]
    country = 'unknown'
    Toolkit.text(fileLocation, nameQualifier, date, country, title, soup)
    x = x+1
