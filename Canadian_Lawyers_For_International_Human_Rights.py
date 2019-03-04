import requests
from bs4 import BeautifulSoup
from toolkit import Toolkit
import pycountry

# News
fileLocation = '.\\Canadian_Lawyers_For_International_Human_Rights\\Blog\\'
nameQualifier = 'CLAIHR_Blog'
pageNumber = 1
bull = True
listofTitles = []
listofDates = []
listofHREFS = []
while(bull):
    linkRequest = requests.get('http://claihr.ca/category/blog/page/' + str(pageNumber) + '/')
    linkSoup = BeautifulSoup(linkRequest.content, features='lxml').find(id="posts-container")
    if linkSoup is not None:
        for page in linkSoup.find_all(class_="entry-title"):
            listofHREFS.append(page.find('a')['href'])
            listofTitles.append(page.find('a').text)
        for page in linkSoup.find_all(class_="published"):
            listofDates.append(page.text)
        pageNumber = pageNumber + 1
    else:
        bull = False
x = 0
for link in listofHREFS:
    pageRequest = requests.get(link)
    soup = BeautifulSoup(pageRequest.content, features='lxml').find(class_="post-content")
    title = listofTitles[x]
    date = listofDates[x]
    country = 'unknown'
    for place in pycountry.countries:
        if place.name in title:
            country = str(place.name)
    Toolkit.text(fileLocation, nameQualifier, date, country, title, soup)
    x = x+1
