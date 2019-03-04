import requests
from bs4 import BeautifulSoup
from toolkit import Toolkit

# News
fileLocation = '.\\Commonwealth_Human_Rights_Initiative\\Press_Releases\\'
nameQualifier = 'CHI_Press_Releases'
pageNumber = 1
bull = True
listofTitles = []
listofDates = []
listofHREFS = []
while(bull):
    linkRequest = requests.get('http://www.humanrightsinitiative.org/press-releases?page=' + str(pageNumber) + '/')
    linkSoup = BeautifulSoup(linkRequest.content, features='lxml').find(class_="press-rel")
    if linkSoup.find(class_="post post-hor") is not None:
        for page in linkSoup.find_all(class_="col-sm-8"):
            listofTitles.append(page.text)
        for page in linkSoup.find_all(class_="meta"):
            listofDates.append(page.text)
        for page in linkSoup.find_all(class_="readmore"):
            listofHREFS.append(page.find('a')['href'])
        pageNumber = pageNumber + 1
    else:
        bull = False
    print(bull)
x = 0
for link in listofHREFS:
    pageRequest = requests.get('http://www.humanrightsinitiative.org/' + link)
    soup = BeautifulSoup(pageRequest.content, features='lxml').find(class_="text-style content-wrap")
    title = listofTitles[x]
    date = listofDates[x][2:][:-1]
    print(date)
    country = 'unknown'
    Toolkit.text(fileLocation, nameQualifier, date, country, title, soup)
    x = x+1

# CHRI In The News
fileLocation = '.\\Commonwealth_Human_Rights_Initiative\\Chri_in_the_News\\'
nameQualifier = 'CHRI_In_The_News'
pageNumber = 1
bull = True
listofTitles = []
listofDates = []
listofHREFS = []
while(bull):
    linkRequest = requests.get('http://www.humanrightsinitiative.org/in-the-news?page=' + str(pageNumber) + '/')
    linkSoup = BeautifulSoup(linkRequest.content, features='lxml').find(class_="news-list")
    if linkSoup.find(class_="post post-timeline") is not None:
        for page in linkSoup.find_all(class_="head"):
            listofTitles.append(page.text[:-17])
        for page in linkSoup.find_all(class_="comments-count"):
            listofDates.append(page.text)
        for page in linkSoup.find_all(class_="readmore"):
            listofHREFS.append(page.find('a')['href'])
        pageNumber = pageNumber + 1
    else:
        bull = False
    print(bull)
x = 0
for link in listofHREFS:
    pageRequest = requests.get('http://www.humanrightsinitiative.org/' + link)
    soup = BeautifulSoup(pageRequest.content, features='lxml').find(class_="text-style content-wrap")
    title = listofTitles[x]
    date = listofDates[x][2:][:-1]
    print(date)
    country = 'unknown'
    Toolkit.text(fileLocation, nameQualifier, date, country, title, soup)
    x = x+1

# Blog
fileLocation = '.\\Commonwealth_Human_Rights_Initiative\\Blog\\'
nameQualifier = 'CHI_Blog'
pageNumber = 1
bull = True
listofTitles = []
listofDates = []
listofHREFS = []
while(bull):
    linkRequest = requests.get('http://www.humanrightsinitiative.org/blog?page=' + str(pageNumber) + '/')
    linkSoup = BeautifulSoup(linkRequest.content, features='lxml').find(class_="blog-wrap")
    if linkSoup.find(class_="blog-list") is not None:
        for page in linkSoup.find_all(class_="title"):
            listofTitles.append(page.text)
            listofHREFS.append(page.find('a')['href'])
        for page in linkSoup.find_all(class_="meta"):
            listofDates.append(page.text[2:][:-1])
        pageNumber = pageNumber + 1
    else:
        bull = False
    print(bull)
x = 0
for link in listofHREFS:
    pageRequest = requests.get('http://www.humanrightsinitiative.org/' + link)
    soup = BeautifulSoup(pageRequest.content, features='lxml').find(class_="text-style content-wrap")
    title = listofTitles[x]
    date = listofDates[x][2:][:-1]
    print(date)
    country = 'unknown'
    Toolkit.text(fileLocation, nameQualifier, date, country, title, soup)
    x = x+1
