import requests
from bs4 import BeautifulSoup
from toolkit import Toolkit

# # About
# fileLocation = '.\\Human_Rights_First\\About\\'
# nameQualifier = 'HRF_About'
# listofDates = []
# listofHREFS = []
# linkRequest = requests.get('https://www.humanrightsfirst.org/about/annual-reports-financials')
# linkSoup = BeautifulSoup(linkRequest.content, features='lxml').find(class_='row')
# for page in linkSoup.find_all('p'):
#     listofHREFS.append('https://www.humanrightsfirst.org/' + page.find('a')['href'])
#     listofDates.append(page.text[:4])
# x = 0
# for link in listofHREFS:
#     pdf = link
#     date = listofDates[x]
#     country = 'Unknown'
#     Toolkit.pdf(fileLocation, nameQualifier, country, date, pdf)
#     x = x+1

# # Blog
# fileLocation = '.\\Human_Rights_First\\Blog\\'
# nameQualifier = 'HRF_Blog'
# pageNumber = 0
# bull = True
# listofTitles = []
# listofDates = []
# listofHREFS = []
# while(bull):
#     linkRequest = requests.get('https://www.humanrightsfirst.org/blog?page=' + str(pageNumber) + '/')
#     linkSoup = BeautifulSoup(linkRequest.content, features='lxml').find(class_="clearfix secondary-content")
#     if linkSoup.find(class_='content-left left') is not None:
#         for page in linkSoup.find_all(class_="views-field views-field-created"):
#             listofDates.append(page.text)
#         for page in linkSoup.find_all(class_="views-field views-field-title"):
#             if page.find('a')['href'][:6] == '/blog/' or page.find('a')['href'][:2] == '/2':
#                 listofHREFS.append('https://www.humanrightsfirst.org' + page.find('a')['href'])
#                 listofTitles.append(page.find('a').text)
#         pageNumber = pageNumber + 1
#     else:
#         bull = False
# x = 0
# for link in listofHREFS:
#     print(link)
#     pageRequest = requests.get(link)
#     soup = BeautifulSoup(pageRequest.content, features='lxml').find(class_="field field-name-body field-type-text-with-summary field-label-hidden")
#     title = listofTitles[x]
#     date = listofDates[x]
#     country = 'unknown'
#     if BeautifulSoup(pageRequest.content, features='lxml').find(class_="field field-name-body field-type-text-with-summary field-label-hidden") is not None:
#         Toolkit.text(fileLocation, nameQualifier, date, country, title, soup)
#     x = x+1

# Resources
fileLocation = '.\\Human_Rights_First\\Resources\\'
nameQualifier = 'HRF_Resources'
pageNumber = 90
bull = True
listofTitles = []
listofDates = []
listofHREFS = []
while(bull):
    linkRequest = requests.get('https://www.humanrightsfirst.org/resources?page=' + str(pageNumber) + '/')
    linkSoup = BeautifulSoup(linkRequest.content, features='lxml').find(class_="column")
    print(linkSoup.find('views-field views-field-created'))
    if linkSoup.find('views-field views-field-created') is not None:
        for page in linkSoup.find_all(class_="views-field views-field-created"):
            listofDates.append(page.text.split(' | ')[1].strip())
            print(page.text.split(' | ')[1].strip())
        for page in linkSoup.find_all(class_="views-field views-field-title"):
            if page.find('a')['href'][:6] == '/resou' or page.find('a')['href'][:2] == '/2':
                listofHREFS.append('https://www.humanrightsfirst.org' + page.find('a')['href'])
                listofTitles.append(page.find('a').text)
                print(page.find('a').text)
        print(pageNumber)
        pageNumber = pageNumber + 1
    else:
        bull = False
x = 0
for link in listofHREFS:
    print(link)
    pageRequest = requests.get(link)
    soup = BeautifulSoup(pageRequest.content, features='lxml').find(class_="field field-name-body field-type-text-with-summary field-label-hidden")
    title = listofTitles[x]
    date = listofDates[x]
    country = 'Unknown'
    Toolkit.text(fileLocation, nameQualifier, date, country, title, soup)
    x = x+1

# Press
fileLocation = '.\\Human_Rights_First\\Press\\'
nameQualifier = 'HRF_Press'
pageNumber = 0
bull = True
listofTitles = []
listofDates = []
listofHREFS = []
while(bull):
    linkRequest = requests.get('https://www.humanrightsfirst.org/press?page=' + str(pageNumber) + '/')
    linkSoup = BeautifulSoup(linkRequest.content, features='lxml').find(class_="block block-views last even")
    if linkSoup is not None:
        for page in linkSoup.find_all(class_="views-field views-field-created"):
            listofDates.append(page.text)
        for page in linkSoup.find_all(class_="views-field views-field-title"):
            if page.find('a')['href'][:6] == '/press' or page.find('a')['href'][:2] == '/2':
                listofHREFS.append('https://www.humanrightsfirst.org' + page.find('a')['href'])
                listofTitles.append(page.find('a').text)
        print(pageNumber)
        pageNumber = pageNumber + 1
    else:
        bull = False
x = 0
for link in listofHREFS:
    print(link)
    pageRequest = requests.get(link)
    soup = BeautifulSoup(pageRequest.content, features='lxml').find(class_="field field-name-body field-type-text-with-summary field-label-hidden")
    title = listofTitles[x]
    date = listofDates[x]
    country = 'Unknown'
    Toolkit.text(fileLocation, nameQualifier, date, country, title, soup)
    x = x+1
