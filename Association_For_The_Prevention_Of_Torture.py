import requests
from bs4 import BeautifulSoup
from toolkit import Toolkit
import pycountry

fileLocation = '.\\Association_For_The_Prevention_Of_Torture\\News\\'
nameQualifier = 'APT_News'
linkRequest = requests.get('https://www.apt.ch/en/news-on-prevention/?year=all&country=0&theme=0&keyword=&key=false')
linkSoup = BeautifulSoup(linkRequest.content, features='lxml')
for article in linkSoup.find_all(class_='news'):
    link2 = 'https://www.apt.ch/' + article['href']
    title = article.find(class_='title').text
    date = article.find(class_='date').text.replace(',', '')
    country = 'Unknown'
    for place in pycountry.countries:
        if place.name in title:
            country = str(place.name)
    link2Request = requests.get(link2)
    link2Soup = BeautifulSoup(link2Request.content, features='lxml')
    link2Soup = link2Soup.find(class_='content')
    Toolkit.text(fileLocation, nameQualifier, date, country, title, link2Soup)

fileLocation = '.\\Association_For_The_Prevention_Of_Torture\\Annual_Reports\\'
nameQualifier = 'APT_Annual_Report'
linkRequest = requests.get('https://apt.ch/en/categories_res/annual-reports-1/')
linkSoup = BeautifulSoup(linkRequest.content, features='lxml')
for article in linkSoup.find_all(class_='resource-container col-lg-6 col-md-12 col-sm-12'):
    date = article.find('h5').text[-4:]
    link2 = 'https://www.apt.ch/' + article.find('a')['href']
    link2Request = requests.get(link2)
    link2Soup = BeautifulSoup(link2Request.content, features='lxml')
    country = 'Unknown'
    pdf = 'https://apt.ch' + link2Soup.find(class_='resource-container col-md-6 col-xs-12').find('a')['href']
    print(pdf)
    Toolkit.pdf(fileLocation, nameQualifier, country, date, pdf)
