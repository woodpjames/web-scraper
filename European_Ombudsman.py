import requests
from bs4 import BeautifulSoup
from toolkit import Toolkit

# Press Releases
fileLocation = '.\\European_Ombudsman\\'
nameQualifier = 'EO_Press_Releases'
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