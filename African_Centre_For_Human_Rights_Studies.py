from bs4 import BeautifulSoup
import requests
from WSTK import *

fileLocation = ".//News//Past//"

nameQualifier = "ACHRS_Past_News"
pastNewsPage = WSTK.soupMaker('https://www.acdhrs.org/past-news-events/', class_='the_content_wrapper')
country = 'No Country Specified'
moreArticles = True
while(moreArticles):
    if pastNewsPage.next('p')['href'] is not None:
        article = pastNewsPage.find('p')
        date = article.find('strong').text.strip()
        title = article.find('a').text.strip()
        link = article.find('a')['href']
        articleSoup = WTSK.soupMaker(link, class_='the_content_wrapper')
        textFileName = textNamingConvention(fileLocation, nameQualifier, country, date)
        WTSK.textFileCompiler(title, date, textFileName, articleSoup)
    else:
        article = pastNewsPage.find('p')
        date = article.find('strong').text.strip()
        title = article.next_sibling.find('a').text.strip()
        link = article.next_sibling.find('a')['href']
        articleSoup = WTSK.soupMaker(link, class_='the_content_wrapper')
        textFileName = textNamingConvention(fileLocation, nameQualifier, country, date)
        WTSK.textFileCompiler(title, date, textFileName, articleSoup)




