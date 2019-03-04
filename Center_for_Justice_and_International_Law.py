import requests
from bs4 import BeautifulSoup
from toolkit import Toolkit
import pycountry

# News
fileLocation = '.\\Center_for_Justice_and_International_Law\\Communication\\News\\'
nameQualifier = 'CEJIL_News'
pageNumber = 0
bull = True
listofTitles = []
listofDates = []
listofHREFS = []
while(bull):
    linkRequest = requests.get('https://cejil.org/en/news?page=' + str(pageNumber) + '/')
    linkSoup = BeautifulSoup(linkRequest.content, features='lxml').find(class_="view-content")
    if linkSoup is not None:
        for page in linkSoup.find_all(class_="cejil-articulos-seccion-titulo"):
            listofHREFS.append(page.find('a')['href'])
            listofTitles.append(page.find('a').text)
        for page in linkSoup.find_all(class_="views-field views-field-created"):
            listofDates.append(page.text)
        pageNumber = pageNumber + 1
    else:
        bull = False
x = 0
for link in listofHREFS:
    pageRequest = requests.get('https://cejil.org' + link)
    soup = BeautifulSoup(pageRequest.content, features='lxml').find(class_="views-field views-field-body body")
    title = listofTitles[x]
    date = listofDates[x]
    country = 'unknown'
    Toolkit.text(fileLocation, nameQualifier, date, country, title, soup)
    x = x+1

# Press_Releases
fileLocation = '.\\Center_for_Justice_and_International_Law\\Communication\\Press_Releases\\'
nameQualifier = 'CEJIL_Press_Releases'
pageNumber = 0
bull = True
listofTitles = []
listofDates = []
listofHREFS = []
while(bull):
    linkRequest = requests.get('https://cejil.org/en/press-releases?page=' + str(pageNumber) + '/')
    linkSoup = BeautifulSoup(linkRequest.content, features='lxml').find(class_="view-content")
    if linkSoup is not None:
        for page in linkSoup.find_all(class_="cejil-articulos-seccion-titulo"):
            listofHREFS.append(page.find('a')['href'])
            listofTitles.append(page.find('a').text)
        for page in linkSoup.find_all(class_="views-field views-field-created"):
            listofDates.append(page.text)
        pageNumber = pageNumber + 1
    else:
        bull = False
x = 0
for link in listofHREFS:
    pageRequest = requests.get('https://cejil.org' + link)
    soup = BeautifulSoup(pageRequest.content, features='lxml').find(class_="views-field views-field-body body")
    title = listofTitles[x]
    date = listofDates[x]
    country = 'unknown'
    Toolkit.text(fileLocation, nameQualifier, date, country, title, soup)
    x = x+1

# Blog
fileLocation = '.\\Center_for_Justice_and_International_Law\\Communication\\Blog\\'
nameQualifier = 'CEJIL_Blog'
pageNumber = 0
bull = True
listofTitles = []
listofDates = []
listofHREFS = []
while(bull):
    linkRequest = requests.get('https://cejil.org/en/blog?page=' + str(pageNumber) + '/')
    print('https://cejil.org/en/blog?page=' + str(pageNumber) + '/')
    linkSoup = BeautifulSoup(linkRequest.content, features='lxml').find(class_="panel-pane pane-views-panes pane-cejil-blog-listado-cejil-listado-blog col-md-46 col-md-offset-1 clearfix")
    if linkSoup is not None:
        for page in linkSoup.find_all(class_="cejil-listado-blog-content-titulo"):
            listofHREFS.append(page.find('a')['href'])
            listofTitles.append(page.find('a').text)
        for page in linkSoup.find_all(class_="cejil-listado-blog-content-fecha"):
            listofDates.append(page.text)
        pageNumber = pageNumber + 1
    else:
        bull = False
x = 0
for link in listofHREFS:
    pageRequest = requests.get('https://cejil.org' + link)
    soup = BeautifulSoup(pageRequest.content, features='lxml').find(class_="cejil-nodo-blog-content-cuerpo body")
    title = listofTitles[x]
    date = listofDates[x]
    country = 'unknown'
    Toolkit.text(fileLocation, nameQualifier, date, country, title, soup)
    x = x+1

# Publications
fileLocation = '.\\Center_for_Justice_and_International_Law\\Tools\\Publications\\'
nameQualifier = 'CEJIL_Publications'
pageNumber = 0
bull = True
listofTitles = []
listofDates = []
listofHREFS = []
while(bull):
    linkRequest = requests.get('https://cejil.org/en/publications?page=' + str(pageNumber) + '/')
    linkSoup = BeautifulSoup(linkRequest.content, features='lxml').find(class_="view-content")
    if linkSoup is not None:
        for page in linkSoup.find_all(class_="cejil-publicaciones-listado-content-titulo"):
            listofHREFS.append(page.find('a')['href'])
            listofTitles.append(page.find('a').text)
        for page in linkSoup.find_all(class_="cejil-publicaciones-listado-content-anio"):
            listofDates.append(page.text)
        pageNumber = pageNumber + 1
    else:
        bull = False
print(listofHREFS)
print(len(listofDates))
print(len(listofTitles))
x = 0
for link in listofHREFS:
    pageRequest = requests.get('https://cejil.org' + link)
    if BeautifulSoup(pageRequest.content, features='lxml').find(class_="archivo-idioma EN") is not None:
        pdf = BeautifulSoup(pageRequest.content, features='lxml').find(class_="archivo-idioma EN").find('a')['href']
    elif BeautifulSoup(pageRequest.content, features='lxml').find(class_="archivo-idioma ES") is not None:
        pdf = BeautifulSoup(pageRequest.content, features='lxml').find(class_="archivo-idioma ES").find('a')['href']
    else:
        pdf = BeautifulSoup(pageRequest.content, features='lxml').find(class_="archivo-idioma PO").find('a')['href']
    title = listofTitles[x]
    date = listofDates[x][:4]
    country = 'unknown'
    for place in pycountry.countries:
        if place.name in title:
            country = str(place.name)
    Toolkit.pdf(fileLocation, nameQualifier, country, date, pdf)
    x = x+1
