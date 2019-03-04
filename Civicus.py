import requests
from bs4 import BeautifulSoup
from toolkit import Toolkit
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# News
fileLocation = '.\\Civil_Society_Watch\\News\\'
nameQualifier = 'CSW_News'
pageNumber = 0
bull = True
listofTitles = []
listofDates = []
listofHREFS = []
driver = webdriver.Firefox()
driver.get('https://www.civicus.org/index.php/media-center/news')
wait = WebDriverWait(driver, 25)
bull = True
while bull:
    try:
        element = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='mnw-total-items']")))
        time.sleep(5)
        element.click()
        time.sleep(15)
    except Exception:
        bull = False
        pass
html = driver.page_source
linkSoup = BeautifulSoup(html, features='lxml')
# print(linkSoup.prettify())
for i, page in enumerate(linkSoup.find_all(class_="mnwall-title")):
    if i%2 == 0:
        listofHREFS.append(page.find('a')['href'])
        listofTitles.append(page.find('a').text.strip())
        # print(page.find('a').text.strip())
for page in linkSoup.find_all(class_="mnwall-date"):
    listofDates.append(page.text.strip())
    # print(page)
x = 0
while x<300:
    print(listofDates[x])
    print(listofTitles[x])
    x = x + 1

x = 0
for link in listofHREFS:
    pageRequest = requests.get('https://www.civicus.org' + link)
    print('https://www.civicus.org' + link)
    soup = BeautifulSoup(pageRequest.content, features='lxml').find(itemprop="articleBody")
    title = listofTitles[x]
    date = listofDates[x]
    country = 'unknown'
    Toolkit.text(fileLocation, nameQualifier, date, country, title, soup)
    x = x+1

# # Reports and Publications
# fileLocation = '.\\Civil_Society_Watch\\Reports_and_Publications\\'
# nameQualifier = 'CSW_Reports_and_Publications'
# pageNumber = 0
# bull = True
# listofTitles = []
# listofDates = []
# listofHREFS = []
# driver = webdriver.Firefox()
# driver.get('https://www.civicus.org/index.php/media-center/reports-publications')
# wait = WebDriverWait(driver, 10)
# bull = True
# while bull:
#     try:
#         element = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='mnw-total-items']")))
#         element.click()
#     except Exception:
#         bull = False
#         pass
# html = driver.page_source
# linkSoup = BeautifulSoup(html, features='lxml')
# print(linkSoup.prettify())
# for page in linkSoup.find_all(class_="mnwall-title"):
#     listofHREFS.append(page.find('a')['href'])
#     listofTitles.append(page.find('a').text.strip())
# for page in linkSoup.find_all(class_="mnwall-date"):
#     listofDates.append(page.text.strip())
# x = 0
# for link in listofHREFS:
#     pageRequest = requests.get('https://www.civicus.org' + link)
#     print('https://www.civicus.org' + link)
#     soup = BeautifulSoup(pageRequest.content, features='lxml').find(itemprop="articleBody")
#     title = listofTitles[x]
#     date = listofDates[x]
#     country = 'unknown'
#     Toolkit.text(fileLocation, nameQualifier, date, country, title, soup)
#     x = x+1
