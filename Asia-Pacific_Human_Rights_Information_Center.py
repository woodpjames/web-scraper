import requests
from bs4 import BeautifulSoup
from toolkit import Toolkit
import pycountry

# Focus Archive
fileLocation = '.\\Asia-Pacific_Human_Rights_Information_Center\\FOCUS_Archive\\'
nameQualifier = 'Asia-Pacific_Human_Rights_Information_Center_FOCUS_Archive'
linkRequest = requests.get('https://www.hurights.or.jp/archives/focus/')
linkSoup = BeautifulSoup(linkRequest.content, features='lxml')
listOfPages = []
print(linkSoup.prettify())
for a in linkSoup(id='trace'):
    listOfPages.append(a['href'])
for archive in listOfPages:
    requestNewsPage = requests.get(archive)
    NewsPage = BeautifulSoup(archive.content, features='lxml')
    NewsPage = NewsPage.find(class_='archives')
    date = NewsPage.h2.text[:-9][5:]
    print(date)
    for article in NewsPage.find_all('a'):
        pdf = article['href']
        title = article.text
        country = 'Unknown'
        for place in pycountry.countries:
            if place.name in title:
                country = str(place.name)
        Toolkit.pdf(fileLocation, nameQualifier, country, date, pdf)

# Human Rights Education In Asian Schools
fileLocation = '.\\Asia-Pacific_Human_Rights_Information_Center\\Human_Rights_Education_In_Asian_Schools\\'
nameQualifier = 'ASPHRIC_HR_Education_In_Asian_Schools'
linkRequest = requests.get('https://www.hurights.or.jp/archives/human_rights_education_in_asian_schools/')
linkSoup = BeautifulSoup(linkRequest.content, features='lxml')
listOfPages = []
print(linkSoup.find(id='trace'))
for a in linkSoup(id='trace'):
    listOfPages.append(a['href'])
for archive in listOfPages:
    requestNewsPage = requests.get(archive)
    NewsPage = BeautifulSoup(archive.content, features='lxml')
    NewsPage = NewsPage.find(class_='archives')
    date = NewsPage.h2.text[:-9][5:]
    print(date)
    for article in NewsPage.find_all('a'):
        pdf = article['href']
        title = article.text
        country = 'Unknown'
        for place in pycountry.countries:
            if place.name in title:
                country = str(place.name)
        Toolkit.pdf(fileLocation, nameQualifier, country, date, pdf)

# Human Rights Education in Asian-Pacific
fileLocation = '.\\Asia-Pacific_Human_Rights_Information_Center\\Human_Rights_Education_In_Asia-Pacific\\'
nameQualifier = 'APHRI_Human_Rights_Education_In_Asia-Pacific'
linkRequest = requests.get('https://www.hurights.or.jp/archives/asia-pacific/')
linkSoup = BeautifulSoup(linkRequest.content, features='lxml')
listOfPages = []
print(linkSoup.find(id='trace'))
for a in linkSoup(id='trace'):
    listOfPages.append(a['href'])
for page in listOfPages:
    pageRequest = requests.get(page)
    pageSoup = BeautifulSoup(pageRequest.content, features='lxml')
    NewsPage = pageSoup.find(id='contents')
    listOfPDFs = []
    listOfTitles = []
    date = 'Unknown'
    for a in NewsPage.find_all('a'):
        listOfPDFs.append(a['href'])
        listOfTitles.append(a.text)
    num = 0
    for link in listOfPages:
        country = 'Unknown'
        for place in pycountry.countries:
            if place.name in listOfTitles[num]:
                country = str(place.name)
        Toolkit.pdf(fileLocation, nameQualifier, country, date, link)
        num = num + 1

# Other Documents
fileLocation = '.\\Asia-Pacific_Human_Rights_Information_Center\\Human_Rights_Declarations_In_Asia-Pacific\\'
nameQualifier = 'Asia-Pacific_Human_Rights_Information_Human_Rights_Declarations'
linkRequest = requests.get('https://www.hurights.or.jp/archives/other_documents/')
linkSoup = BeautifulSoup(linkRequest.content, features='lxml')
NewsPage = linkSoup.find(id='contents')
listOfPages = []
listOfDates = []
listOfTitles = []
for a in NewsPage.find_all('a'):
    listOfPages.append(a['href'])
    listOfTitles.append(a.text)
for li in NewsPage.find_all('li'):
    listOfDates.append(li.text[-5:][:-1])
num = 0
for link in listOfPages:
    country = 'Unknown'
    for place in pycountry.countries:
        if place.name in listOfTitles[num]:
            country = str(place.name)
    request = requests.get(link)
    linkSoup = BeautifulSoup(request.content, features='lxml')
    soup = linkSoup.find(class_='archives')
    Toolkit.text(fileLocation, nameQualifier, listOfDates[num], country, listOfTitles[num], soup)
    num = num + 1
