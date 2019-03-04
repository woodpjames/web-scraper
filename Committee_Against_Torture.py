import requests
from bs4 import BeautifulSoup
from toolkit import Toolkit
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# News
fileLocation = '.\\Committee_Against_Torture\\News'
nameQualifier = 'CAT_News'
pageNumber = 0
bull = True
listofTitles = []
listofDates = []
listofHREFS = []
driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10)
driver.get('https://www.ohchr.org/EN/NewsEvents/Pages/NewsSearch.aspx?NTID=PRS')
while(bull):
    html = driver.page_source
    linkSoup = BeautifulSoup(html, features='lxml').find('table', id='ctl00_PlaceHolderMain_SearchNewsID_gvNewsSearchresult')
    for page in linkSoup.find_all('tr', align='left'):
        print(page.find('a', class_='HPLink'))
        if page.find('a', class_='HPLink') is not None:
            listofHREFS.append(page.find('a', class_='HPLink')['href'])
            listofTitles.append(page.find(style='width:30%;').text)
            listofDates.append(page.find(class_="lblNewsDate").text)
    driver.find_element_by_xpath((By.XPATH, "//a[last()]"))
x = 0
for link in listofHREFS:
    pageRequest = requests.get('https://cejil.org' + link)
    soup = BeautifulSoup(pageRequest.content, features='lxml').find(class_="views-field views-field-body body")
    title = listofTitles[x]
    date = listofDates[x]
    country = 'unknown'
    Toolkit.text(fileLocation, nameQualifier, date, country, title, soup)
    x = x+1
