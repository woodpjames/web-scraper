import requests
from bs4 import BeautifulSoup
from toolkit import Toolkit

# News
fileLocation = '.\\Commonwealth_Secretariat\\Newsroom\\'
nameQualifier = 'CS_Newsroom'
pageNumber = 205
bull = True
listofTitles = []
listofDates = []
listofHREFS = []
while(bull):
    linkRequest = requests.get('http://thecommonwealth.org/newsroom?page=' + str(pageNumber) + '/')
    linkSoup = BeautifulSoup(linkRequest.content, features='lxml').find(class_="view-content")
    for page in linkSoup.find_all('h3'):
        listofTitles.append(page.text.strip())
        listofHREFS.append(page.find('a')['href'])
    for page in linkSoup.find_all(class_="list-view"):
        if page.find(class_='created') is not None:
            if page.find(class_='created').text.strip()[:12] == 'Release date':
                listofDates.append(page.find(class_='created').text.strip()[12:])
            else:
                listofDates.append(page.find(class_='created').text.strip())
        else:
            listofDates.append("UnknownDate")
    print(pageNumber)
    pageNumber = pageNumber + 1
    if pageNumber > 275:
        if BeautifulSoup(linkRequest.content, features='lxml').find(class_="pager-current last") is not None:
            bull = False
x = 0
for link in listofHREFS:
    pageRequest = requests.get('http://thecommonwealth.org' + link)
    soup = BeautifulSoup(pageRequest.content, features='lxml').find(class_="content clearfix")
    title = listofTitles[x]
    date = listofDates[x]
    if date[:-12] is "Release date":
        date = date[13:]
    country = 'UnknownCountry'
    try:
        Toolkit.text(fileLocation, nameQualifier, date, country, title, soup)
    except Exception:
        pass
    x = x+1
