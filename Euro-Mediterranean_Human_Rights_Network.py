import requests
from bs4 import BeautifulSoup
from toolkit import Toolkit

# News
fileLocation = '.\\Euro-Mediterranean_Human_Rights_Network\\E-Library\\'
nameQualifier = 'EMHRN_E-Library'
pageNumber = 1
bull = True
listofTitles = []
listofDates = []
listofHREFS = []
while(bull):
    linkRequest = requests.get('https://euromedrights.org/e-library/?fwp_paged=' + str(pageNumber) + '/')
    linkSoup = BeautifulSoup(linkRequest.content, features='lxml').find(class_="list-unstyled")
    if linkSoup.find('article') is not None:
        for page in linkSoup.find_all('h4'):
            listofTitles.append(page.text)
            listofHREFS.append(page.find('a')['href'])
        for page in linkSoup.find_all('time'):
            listofDates.append(page.text.strip())
        print(pageNumber)
        pageNumber = pageNumber + 1
    else:
        bull = False
x = 0
for link in listofHREFS:
    pageRequest = requests.get(link)
    title = listofTitles[x]
    country = "Unknown"
    date = listofDates[x]
    href_there = False
    if BeautifulSoup(pageRequest.content, features='lxml').find(class_="wrapped") is not None:
        soup = BeautifulSoup(pageRequest.content, features='lxml').find(class_="wrapped")
        for href in soup.find_all('a'):
            if href.text.strip() == "Read the full report here" or href.text.strip() == "Download":
                href_there = True
                pdf = href['href']
                Toolkit.pdf(fileLocation, nameQualifier, country, date, pdf, title=title)
                break
        if href_there is False:
            Toolkit.text(fileLocation, nameQualifier, date, country, title, soup)
    x = x+1
