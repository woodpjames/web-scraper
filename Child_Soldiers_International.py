import requests
from bs4 import BeautifulSoup
from toolkit import Toolkit
import pycountry
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Press Releases
fileLocation = '.\\Child_Soldiers_International\\News\\Press_Releases\\'
nameQualifier = 'CSI_Press_Releases'
pageNumber = 0
listofTitles = []
listofDates = []
listofHREFS = []
driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10)
driver.get('https://www.child-soldiers.org/Pages/News/Category/press-releases')
bull = True
while bull:
    try:
        driver.find_element_by_css_selector('a.cc-btn.cc-dismiss').click()
    except Exception:
        bull = False
        pass
bull = True
while bull:
    try:
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='button loadMore']")))
        element.click()
    except Exception:
        bull = False
        pass
html = driver.page_source
linkSoup = BeautifulSoup(html, features='lxml').find(class_='content listContent')
driver.close()
print(linkSoup.prettify())
for page in linkSoup.find_all(class_="listedPostText"):
    listofHREFS.append(page.find('a')['href'])
    listofTitles.append(page.find('a').text)
for page in linkSoup.find_all('time'):
    listofDates.append(page.text)
x = 0
for link in listofHREFS:
    pageRequest = requests.get('https://www.child-soldiers.org/' + link)
    soup = BeautifulSoup(pageRequest.content, features='lxml').find(class_="content postContent newsContent")
    title = listofTitles[x]
    date = listofDates[x]
    country = 'unknown'
    Toolkit.text(fileLocation, nameQualifier, date, country, title, soup)
    x = x+1

# In the Media
fileLocation = '.\\Child_Soldiers_International\\News\\In_the_Media\\'
nameQualifier = 'CSI_In_the_Media'
pageNumber = 0
bull = True
listofTitles = []
listofDates = []
listofHREFS = []
driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10)
driver.get('https://www.child-soldiers.org/Pages/News/Category/in-the-media')
bull = True
while bull:
    try:
        driver.find_element_by_css_selector('a.cc-btn.cc-dismiss').click()
    except Exception:
        bull = False
        pass
print('here')
bull = True
while bull:
    try:
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='button loadMore']")))
        element.click()
    except Exception:
        bull = False
        pass
html = driver.page_source
linkSoup = BeautifulSoup(html, features='lxml').find(class_='content listContent')
driver.close()
print(linkSoup.prettify())
for page in linkSoup.find_all(class_="listedPostText"):
    listofHREFS.append(page.find('a')['href'])
    listofTitles.append(page.find('a').text)
for page in linkSoup.find_all('time'):
    listofDates.append(page.text)
x = 0
for link in listofHREFS:
    pageRequest = requests.get('https://www.child-soldiers.org/' + link)
    soup = BeautifulSoup(pageRequest.content, features='lxml').find(class_="content postContent newsContent")
    title = listofTitles[x]
    date = listofDates[x]
    country = 'unknown'
    Toolkit.text(fileLocation, nameQualifier, date, country, title, soup)
    x = x+1

# Blogs & Insights
fileLocation = '.\\Child_Soldiers_International\\News\\Blog_&_Insights\\'
nameQualifier = 'CSI_Blog_&_Insights'
pageNumber = 0
bull = True
listofTitles = []
listofDates = []
listofHREFS = []
driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10)
driver.get('https://www.child-soldiers.org/Pages/News/Category/blog')
bull = True
while bull:
    try:
        driver.find_element_by_css_selector('a.cc-btn.cc-dismiss').click()
    except Exception:
        bull = False
        pass
print('here')
bull = True
while bull:
    try:
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='button loadMore']")))
        element.click()
    except Exception:
        bull = False
        pass
html = driver.page_source
linkSoup = BeautifulSoup(html, features='lxml').find(class_='content listContent')
driver.close()
print(linkSoup.prettify())
for page in linkSoup.find_all(class_="listedPostText"):
    listofHREFS.append(page.find('a')['href'])
    listofTitles.append(page.find('a').text)
for page in linkSoup.find_all('time'):
    listofDates.append(page.text)
x = 0
for link in listofHREFS:
    pageRequest = requests.get('https://www.child-soldiers.org/' + link)
    soup = BeautifulSoup(pageRequest.content, features='lxml').find(class_="content postContent newsContent")
    title = listofTitles[x]
    date = listofDates[x]
    country = 'unknown'
    Toolkit.text(fileLocation, nameQualifier, date, country, title, soup)
    x = x+1

# Resources
fileLocation = '.\\Child_Soldiers_International\\Resources\\'
nameQualifier = 'CSI_Resources'
pageNumber = 0
bull = True
listofTitles = []
listofDates = []
listofHREFS = []
driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10)
driver.get('https://www.child-soldiers.org/pages/shop/department/all')
bull = True
while bull:
    try:
        driver.find_element_by_css_selector('a.cc-btn.cc-dismiss').click()
    except Exception:
        bull = False
        pass
bull = True
y = 0
print('here')
while bull:
    try:
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='button loadMore']")))
        driver.find_element_by_xpath("//a[@class='button loadMore']").click()
    except Exception:
        print(Exception)
        bull = False
        pass
html = driver.page_source
linkSoup = BeautifulSoup(html, features='lxml').find(class_='content listContent')
driver.close()
print(linkSoup.prettify())
for page in linkSoup.find_all(class_="listedProductText"):
    listofHREFS.append(page.find('a')['href'])
    listofTitles.append(page.find('a').text)
x = 0
for link in listofHREFS:
    pageRequest = requests.get('https://www.child-soldiers.org/' + link)
    pdf = BeautifulSoup(pageRequest.content, features='lxml').find(class_='content productDescription').find('a')['href']
    print(pdf[0:6])
    if pdf[0:6] != 'https:' or pdf[0:6] != 'http:/':
        print('Im here')
        pdf = 'https://www.child-soldiers.org' + pdf
    print(pdf)
    title = listofTitles[x]
    date = 'unknown'
    country = 'unknown'
    for place in pycountry.countries:
        if place.name in title:
            country = str(place.name)
    Toolkit.pdf(fileLocation, nameQualifier, country, date, pdf)
    x = x+1
