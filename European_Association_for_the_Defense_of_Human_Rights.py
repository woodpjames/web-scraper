import requests
from bs4 import BeautifulSoup
from toolkit import Toolkit

# Statements
fileLocation = '.\\European_Association_for_the_Defense_of_Human_Rights\\Statements\\'
nameQualifier = 'EADHR_Statements'
pageNumber = 1
bull = True
listofTitles = []
listofDates = []
listofHREFS = []
while(bull):
    linkRequest = requests.get('http://www.aedh.eu/en/category/statements/page/' + str(pageNumber) + '/')
    linkSoup = BeautifulSoup(linkRequest.content, features='lxml').find(class_="archive-content")
    if linkSoup is not None:
        for page in linkSoup.find_all(class_="blog_title"):
            listofHREFS.append(page.find('a')['href'])
            listofTitles.append(page.find('a').text)
        for page in linkSoup.find_all(class_="date"):
            print(page.text.strip())
            listofDates.append(page.text.strip())
        pageNumber = pageNumber + 1
        print(pageNumber)
    else:
        bull = False
x = 0
for link in listofHREFS:
    pageRequest = requests.get(link)
    soup = BeautifulSoup(pageRequest.content, features='lxml').find(class_="entry-content")
    title = listofTitles[x]
    date = listofDates[x]
    country = 'Unknown'
    Toolkit.text(fileLocation, nameQualifier, date, country, title, soup)
    x = x+1

# News_from_AEDH
fileLocation = '.\\European_Association_for_the_Defense_of_Human_Rights\\News\\News_from_AEDH\\'
nameQualifier = 'News_from_AEDH'
pageNumber = 1
bull = True
listofTitles = []
listofDates = []
listofHREFS = []
while(bull):
    linkRequest = requests.get('http://www.aedh.eu/en/category/news/news-from-aedh/page/' + str(pageNumber) + '/')
    linkSoup = BeautifulSoup(linkRequest.content, features='lxml').find(class_="archive-content")
    if linkSoup is not None:
        for page in linkSoup.find_all(class_="blog_title"):
            listofHREFS.append(page.find('a')['href'])
            listofTitles.append(page.find('a').text)
            print(page.find('a').text)
        for page in linkSoup.find_all(class_="date"):
            print(page.text.strip())
            listofDates.append(page.text.strip())
        pageNumber = pageNumber + 1
        print(pageNumber)
    else:
        bull = False
x = 0
for link in listofHREFS:
    pageRequest = requests.get(link)
    soup = BeautifulSoup(pageRequest.content, features='lxml').find(class_="entry-content")
    title = listofTitles[x]
    date = listofDates[x]
    country = 'Unknown'
    Toolkit.text(fileLocation, nameQualifier, date, country, title, soup)
    x = x+1

# News_from_out_Members
fileLocation = '.\\European_Association_for_the_Defense_of_Human_Rights\\News\\News_from_our_Members\\'
nameQualifier = 'News_from_our_Members'
pageNumber = 1
bull = True
listofTitles = []
listofDates = []
listofHREFS = []
while(bull):
    linkRequest = requests.get('http://www.aedh.eu/en/category/news/news-from-our-member-leagues/page/' + str(pageNumber) + '/')
    linkSoup = BeautifulSoup(linkRequest.content, features='lxml').find(class_="archive-content")
    if linkSoup is not None:
        for page in linkSoup.find_all(class_="blog_title"):
            listofHREFS.append(page.find('a')['href'])
            listofTitles.append(page.find('a').text)
            print(page.find('a').text)
        for page in linkSoup.find_all(class_="date"):
            print(page.text.strip())
            listofDates.append(page.text.strip())
        pageNumber = pageNumber + 1
        print(pageNumber)
    else:
        bull = False
x = 0
for link in listofHREFS:
    pageRequest = requests.get(link)
    soup = BeautifulSoup(pageRequest.content, features='lxml').find(class_="entry-content")
    title = listofTitles[x]
    date = listofDates[x]
    country = 'Unknown'
    Toolkit.text(fileLocation, nameQualifier, date, country, title, soup)
    x = x+1

# Newsletter
fileLocation = '.\\European_Association_for_the_Defense_of_Human_Rights\\News\\AEDH_Newsletter\\'
nameQualifier = 'Newsletter'
pageNumber = 1
bull = True
listofTitles = []
listofDates = []
listofHREFS = []
while(bull):
    linkRequest = requests.get('http://www.aedh.eu/en/category/news/the-aedh-newsletter/page/' + str(pageNumber) + '/')
    linkSoup = BeautifulSoup(linkRequest.content, features='lxml').find(class_="archive-content")
    if linkSoup is not None:
        for page in linkSoup.find_all(class_="blog_title"):
            listofHREFS.append(page.find('a')['href'])
            listofTitles.append(page.find('a').text)
            print(page.find('a').text)
        for page in linkSoup.find_all(class_="date"):
            print(page.text.strip())
            listofDates.append(page.text.strip())
        pageNumber = pageNumber + 1
        print(pageNumber)
    else:
        bull = False
x = 0
for link in listofHREFS:
    pageRequest = requests.get(link)
    soup = BeautifulSoup(pageRequest.content, features='lxml').find(class_="entry-content")
    title = listofTitles[x]
    date = listofDates[x]
    country = 'Unknown'
    Toolkit.text(fileLocation, nameQualifier, date, country, title, soup)
    x = x+1

# Who We Are
fileLocation = '.\\European_Association_for_the_Defense_of_Human_Rights\\Who_we_Are\\'
nameQualifier = 'Newsletter'
listofDates = []
listofHREFS = []
linkRequest = requests.get('http://www.aedh.eu/en/who-we-are/activity-reports/')
linkSoup = BeautifulSoup(linkRequest.content, features='lxml').find(class_="so-panel widget widget_sow-features panel-last-child")
for page in linkSoup.find_all('a'):
    listofHREFS.append(page['href'])
for page in linkSoup.find_all('h5'):
    listofDates.append(page.text.strip()[-9:])
x = 0
for link in listofHREFS:
    date = listofDates[x]
    country = 'Unknown'
    Toolkit.pdf(fileLocation, nameQualifier, country, date, link)
    x = x+1
