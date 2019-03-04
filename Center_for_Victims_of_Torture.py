import requests
from bs4 import BeautifulSoup
from toolkit import Toolkit

# IMPORTANT NOTE FOR IN THE NEWS. NEWSPAGES GO TO DIFFERENT SOURCES. COULD NOT MAKE A SYSTEMATIC SCRAPE. SOME FILES MAY BE INCOMPLETE
# In the News
fileLocation = '.\\Center_for_Victims_of_Torture\\Newsroom\\In_The_News\\'
nameQualifier = 'CVT_In_The_News'
pageNumber = 50
bull = True
listofTitles = []
listofDates = []
listofHREFS = []
while(bull):
    linkRequest = requests.get('https://www.cvt.org/news-events/in-the-news?page=' + str(pageNumber) + '/')
    linkSoup = BeautifulSoup(linkRequest.content, features='lxml').find(class_="view-content")
    if linkSoup is not None:
        for page in linkSoup.find_all(class_="field-content newslist-title"):
            listofHREFS.append(page.find('a')['href'])
            listofTitles.append(page.find('a').text)
        for page in linkSoup.find_all(class_="date-display-single"):
            listofDates.append(page.text)
        print(pageNumber)
        pageNumber = pageNumber + 1
    else:
        bull = False
x = 0
for link in listofHREFS:
    print(link)
    if link != 'http://www.mcclatchydc.com/2014/12/09/249511/will-history-or-the-law-judge.html?sp=/99/100/&ihp=1' and link != 'http://www.ledger-enquirer.com/2014/08/21/3255454/curt-goering-just-call-torture.html' and link != 'http://www.miamiherald.com/2013/10/07/3676242/miami-herald-sources-capitol-hill.html' and link != 'http://www.miamiherald.com/2013/05/14/3397004/human-rights-groups-call-for-end.html' and link[-4:] != '.pdf':
        pageRequest = requests.get(link)
        soup = BeautifulSoup(pageRequest.content, features='lxml')
        title = listofTitles[x]
        date = listofDates[x]
        print(title)
        print(date)
        country = 'unknown'
        if link != 'https://www.facebook.com/mpacnational/videos/10156678599563394/' and link != 'http://goo.gl/BjzzKK':
            Toolkit.text(fileLocation, nameQualifier, date, country, title, soup)
        print(x)
        x = x + 1

# Press Releases
fileLocation = '.\\Center_for_Victims_of_Torture\\Newsroom\\Press_Releases\\'
nameQualifier = 'CVT_Press_Releases'
pageNumber = 0
bull = True
listofTitles = []
listofDates = []
listofHREFS = []
while(bull):
    linkRequest = requests.get('https://www.cvt.org/news-events/press-releases?field_press_release_date_value%5Bvalue%5D%5Byear%5D=&page=' + str(pageNumber) + '/')
    linkSoup = BeautifulSoup(linkRequest.content, features='lxml').find(class_="view-content")
    if linkSoup is not None:
        for page in linkSoup.find_all(class_="newslist-title"):
            listofHREFS.append(page.find('a')['href'])
            listofTitles.append(page.find('a').text)
        for page in linkSoup.find_all(class_="date-display-single"):
            listofDates.append(page.text)
        print(pageNumber)
        pageNumber = pageNumber + 1
    else:
        bull = False
print(listofHREFS)
x = 0
for link in listofHREFS:
    print('https://www.cvt.org' + link)
    pageRequest = requests.get('https://www.cvt.org' + link)
    soup = BeautifulSoup(pageRequest.content, features='lxml').find(class_="field-item even")
    title = listofTitles[x]
    date = listofDates[x]
    print(title)
    print(date)
    country = 'unknown'
    Toolkit.text(fileLocation, nameQualifier, date, country, title, soup)
    x = x+1

# Newsletters
fileLocation = '.\\Center_for_Victims_of_Torture\\Newsroom\\Newsletters\\'
nameQualifier = 'CVT_Newsletters'
pageNumber = 0
bull = True
listofTitles = []
listofDates = []
listofHREFS = []
while(bull):
    linkRequest = requests.get('https://www.cvt.org/news-events/newsletters?page=' + str(pageNumber) + '/')
    linkSoup = BeautifulSoup(linkRequest.content, features='lxml').find(class_="view-content")
    if linkSoup is not None:
        for page in linkSoup.find_all(class_="newslist-title"):
            listofTitles.append(page.text)
        for page in linkSoup.find_all(class_="date-display-single"):
            listofDates.append(page.text)
        for page in linkSoup.find_all(class_="file"):
            listofHREFS.append(page.find('a')['href'])
        pageNumber = pageNumber + 1
    else:
        bull = False
print(listofHREFS)
x = 0
for link in listofHREFS:
    pdf = link
    title = listofTitles[x]
    date = listofDates[x]
    country = 'unknown'
    Toolkit.pdf(fileLocation, nameQualifier, country, date, pdf)
    x = x+1

# Blog
fileLocation = '.\\Center_for_Victims_of_Torture\\Newsroom\\Healing_and_Human_Rights_Blog\\'
nameQualifier = 'CVT_Blog'
pageNumber = 0
bull = True
listofTitles = []
listofDates = []
listofHREFS = []
while(bull):
    print('https://www.cvt.org/blog/healing-and-human-rights?page=' + str(pageNumber) + '/')
    linkRequest = requests.get('https://www.cvt.org/blog/healing-and-human-rights?page=' + str(pageNumber) + '/')
    linkSoup = BeautifulSoup(linkRequest.content, features='lxml').find(class_="panel-pane pane-views-panes pane-cvt-blog-panel-pane-1")
    if linkSoup.find(class_='view-empty') is None:
        for page in linkSoup.find_all(class_="views-field views-field-title"):
            listofTitles.append(page.find('a').text)
            listofHREFS.append(page.find('a')['href'])
        for page in linkSoup.find_all(class_="views-field views-field-created"):
            listofDates.append(page.text)
        pageNumber = pageNumber + 1
    else:
        bull = False
print(listofHREFS)
x = 0
for link in listofHREFS:
    print('https://www.cvt.org' + link)
    pageRequest = requests.get('https://www.cvt.org' + link)
    soup = BeautifulSoup(pageRequest.content, features='lxml').find(class_="field field-name-body field-type-text-with-summary field-label-hidden")
    title = listofTitles[x]
    date = listofDates[x]
    print(title)
    print(date)
    country = 'unknown'
    Toolkit.text(fileLocation, nameQualifier, date, country, title, soup)
    x = x+1
