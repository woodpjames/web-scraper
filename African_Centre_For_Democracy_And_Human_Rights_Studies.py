from bs4 import BeautifulSoup
import requests
from newsplease import NewsPlease
from toolkit import Toolkit
import pycountry
import urllib


# Past
fileLocation = '.\\African_Centre_For_Democracy_And_Human_Rights_Studies\\News\\Past\\'
nameQualifier = 'ACHRS_Past'
linkRequest = requests.get('https://www.acdhrs.org/past-news-events/')
linkSoup = BeautifulSoup(linkRequest.content, features='lxml')
NewsPage = linkSoup.find(class_='content_wrapper clearfix')
NewsPageHrefs = []
linesInString = NewsPage.text.strip().splitlines()
linesInString = list(filter(None, linesInString))
dateIndex = 1
for a in NewsPage.find_all('a', href=True):
    NewsPageHrefs.append(a['href'])
for linkFromList in NewsPageHrefs:
    date = linesInString[dateIndex]
    title = linesInString[dateIndex + 1]
    try:
        article = NewsPlease.from_url(linkFromList)
        text = article.text
        countryName = 'Unknown'
        soupRequest = requests.get(linkFromList)
        soup = BeautifulSoup(soupRequest.content, features='lxml')
        for country in pycountry.countries:
            if country.name in text:
                countryName = str(country.name)
        textFileName = Toolkit.textNamingConvention(fileLocation, nameQualifier, countryName, date)
        Toolkit.textFileCompiler(title, date, textFileName, soup)
    except Exception:  # urllib.error.HTTPError or urllib.error.URLError or socket.gaierror:
        print('Exception was thrown.')
        pass
    dateIndex = dateIndex + 2

# Upcoming
fileLocation = '.\\African_Centre_For_Democracy_And_Human_Rights_Studies\\News\\Upcoming\\'
nameQualifier = 'ACHRS_Upcoming'
linkRequest = requests.get('https://www.acdhrs.org/upcoming/')
linkSoup = BeautifulSoup(linkRequest.content, features='lxml')
NewsPage = linkSoup.find(class_='content_wrapper clearfix')
NewsPageHrefs = []
linesInString = NewsPage.text.strip().splitlines()
linesInString = list(filter(None, linesInString))
dateIndex = 1
for a in NewsPage.find_all('a', href=True):
    NewsPageHrefs.append(a['href'])
for linkFromList in NewsPageHrefs:
    date = linesInString[dateIndex]
    title = linesInString[dateIndex + 1]
    try:
        article = NewsPlease.from_url(linkFromList)
        text = article.text
        countryName = 'Unknown'
        soupRequest = requests.get(linkFromList)
        soup = BeautifulSoup(soupRequest.content, features='lxml')
        for country in pycountry.countries:
            if country.name in text:
                countryName = str(country.name)
        textFileName = Toolkit.textNamingConvention(fileLocation, nameQualifier, countryName, date)
        Toolkit.textFileCompiler(title, date, textFileName, soup)
    except Exception:  # urllib.error.HTTPError or urllib.error.URLError or socket.gaierror:
        print("Exception was thrown.")
        pass
    dateIndex = dateIndex + 2

# Forum Reports
# Not Sure What Going on With Last Article
fileLocation = '.\\African_Centre_For_Democracy_And_Human_Rights_Studies\\Blog\\Forum_Reports\\'
nameQualifier = 'ACHRS_Blog_Forum_Reports'
pageNum = 0
moreLinks = True
while moreLinks is True:
    pageNum = pageNum + 1
    linkRequest = requests.get('https://www.acdhrs.org/category/documentation/forum-reports/page/' + str(pageNum) + '/')
    linkSoup = BeautifulSoup(linkRequest.content, features='lxml')
    NewsPage = linkSoup.find(class_='posts_group lm_wrapper masonry tiles col-3 isotope')
    NewsPageDates = []
    NewsPageTitles = []
    if NewsPage is None:
        moreLinks = False
    else:
        for dateInfo in NewsPage.find_all('div', class_='date_label'):
            NewsPageDates.append(dateInfo.text.strip())
        for titleInfo in NewsPage.find_all(class_='entry-title'):
            NewsPageTitles.append(titleInfo.text.strip())
        dateIndex = 0
        titleIndex = 0
        NewsPageHrefs = []
        for a in NewsPage.find_all('a', href=True):
            NewsPageHrefs.append(a['href'])
        for linkFromList in NewsPageHrefs:
            # try:
            date = NewsPageDates[dateIndex]
            title = NewsPageTitles[titleIndex]
            article = NewsPlease.from_url(linkFromList)
            request = requests.get(linkFromList)
            soup = BeautifulSoup(request.content, features='lxml')
            soup = soup.find(class_='post-wrapper-content')
            text = soup.text
            countryName = 'Unknown'
            soupRequest = requests.get(linkFromList)
            soup = BeautifulSoup(soupRequest.content, features='lxml')
            for country in pycountry.countries:
                if country.name in text:
                    countryName = str(country.name)
            textFileName = Toolkit.textNamingConvention(fileLocation, nameQualifier, countryName, date)
            Toolkit.textFileCompiler(title, date, textFileName, soup)
            dateIndex = dateIndex+1
            titleIndex = titleIndex+1


# Resolutions
fileLocation = '.\\African_Centre_For_Democracy_And_Human_Rights_Studies\\Blog\\Resolutions\\'
nameQualifier = 'ACHRS_Blog_Resolutions'
pageNum = 0
moreLinks = True
while moreLinks is True:
    pageNum = pageNum + 1
    linkRequest = requests.get('https://www.acdhrs.org/category/documentation/resolutions/page/' + str(pageNum) + '/')
    print(linkRequest)
    linkSoup = BeautifulSoup(linkRequest.content, features='lxml')
    NewsPage = linkSoup.find(class_='posts_group lm_wrapper masonry tiles col-3 isotope')
    NewsPageDates = []
    NewsPageTitles = []
    if NewsPage is None:
        moreLinks = False
    else:
        try:
            for dateInfo in NewsPage.find_all('div', class_='date_label'):
                NewsPageDates.append(dateInfo.text.strip())
            for titleInfo in NewsPage.find_all(class_='entry-title'):
                NewsPageTitles.append(titleInfo.text.strip())
            print(NewsPageDates)
            print(NewsPageTitles)
            dateIndex = 0
            titleIndex = 0
            NewsPageHrefs = []
            for a in NewsPage.find_all('a', href=True):
                NewsPageHrefs.append(a['href'])
            print(NewsPageHrefs)
            for linkFromList in NewsPageHrefs:
                date = NewsPageDates[dateIndex]
                title = NewsPageTitles[titleIndex]
                article = NewsPlease.from_url(linkFromList)
                request = requests.get(linkFromList)
                soup = BeautifulSoup(request.content, features='lxml')
                soup = soup.find(class_='post-wrapper-content')
                text = soup.text
                countryName = 'Unknown'
                soupRequest = requests.get(linkFromList)
                soup = BeautifulSoup(soupRequest.content, features='lxml')
                for country in pycountry.countries:
                    if country.name in text:
                        countryName = str(country.name)
                textFileName = Toolkit.textNamingConvention(fileLocation, nameQualifier, countryName, date)
                Toolkit.textFileCompiler(title, date, textFileName, soup)
                dateIndex = dateIndex + 1
                titleIndex = titleIndex + 1
        except UnicodeEncodeError:
            pass

# Joint Statements
fileLocation = '.\\African_Centre_For_Democracy_And_Human_Rights_Studies\\Blog\\Joint_Statements\\'
nameQualifier = 'ACHRS_Blog_Joint_Statements'
pageNum = 0
moreLinks = True
while moreLinks is True:
    pageNum = pageNum + 1
    linkRequest = requests.get('https://www.acdhrs.org/category/documentation/joint-statements/page/' + str(pageNum) + '/')
    linkSoup = BeautifulSoup(linkRequest.content, features='lxml')
    NewsPageDates = []
    NewsPageTitles = []
    NewsPage = linkSoup.find(class_='posts_group lm_wrapper masonry tiles col-3 isotope')
    if NewsPage is None:
        moreLinks = False
    else:
        try:
            for dateInfo in NewsPage.find_all('div', class_='date_label'):
                NewsPageDates.append(dateInfo.text.strip())
            for titleInfo in NewsPage.find_all(class_='entry-title'):
                NewsPageTitles.append(titleInfo.text.strip())
            print(NewsPageDates)
            print(NewsPageTitles)
            dateIndex = 0
            titleIndex = 0
            NewsPageHrefs = []
            for a in NewsPage.find_all('a', href=True):
                NewsPageHrefs.append(a['href'])
            for linkFromList in NewsPageHrefs:
                date = NewsPageDates[dateIndex]
                title = NewsPageTitles[titleIndex]
                article = NewsPlease.from_url(linkFromList)
                request = requests.get(linkFromList)
                soup = BeautifulSoup(request.content, features='lxml')
                soup = soup.find(class_='post-wrapper-content')
                text = soup.text
                countryName = 'Unknown'
                soupRequest = requests.get(linkFromList)
                soup = BeautifulSoup(soupRequest.content, features='lxml')
                for country in pycountry.countries:
                    if country.name in text:
                        countryName = str(country.name)
                textFileName = Toolkit.textNamingConvention(fileLocation, nameQualifier, countryName, date)
                Toolkit.textFileCompiler(title, date, textFileName, soup)
                dateIndex = dateIndex + 1
                titleIndex = titleIndex + 1
        except UnicodeEncodeError:
            pass

# Recommendations
fileLocation = '.\\African_Centre_For_Democracy_And_Human_Rights_Studies\\Blog\\Recommendations\\'
nameQualifier = 'ACHRS_Blog_Recommendations'
pageNum = 0
moreLinks = True
while moreLinks is True:
    pageNum = pageNum + 1
    linkRequest = requests.get('https://www.acdhrs.org/category/documentation/recommendations/page/' + str(pageNum) + '/')
    linkSoup = BeautifulSoup(linkRequest.content, features='lxml')
    NewsPageDates = []
    NewsPageTitles = []
    NewsPage = linkSoup.find(class_='posts_group lm_wrapper masonry tiles col-3 isotope')
    if NewsPage is None:
        moreLinks = False
    else:
        try:
            for dateInfo in NewsPage.find_all('div', class_='date_label'):
                NewsPageDates.append(dateInfo.text.strip())
            for titleInfo in NewsPage.find_all(class_='entry-title'):
                NewsPageTitles.append(titleInfo.text.strip())
            print(NewsPageDates)
            print(NewsPageTitles)
            dateIndex = 0
            titleIndex = 0
            NewsPageHrefs = []
            for a in NewsPage.find_all('a', href=True):
                NewsPageHrefs.append(a['href'])
            for linkFromList in NewsPageHrefs:
                date = NewsPageDates[dateIndex]
                title = NewsPageTitles[titleIndex]
                article = NewsPlease.from_url(linkFromList)
                request = requests.get(linkFromList)
                soup = BeautifulSoup(request.content, features='lxml')
                soup = soup.find(class_='post-wrapper-content')
                text = soup.text
                countryName = 'Unknown'
                soupRequest = requests.get(linkFromList)
                soup = BeautifulSoup(soupRequest.content, features='lxml')
                for country in pycountry.countries:
                    if country.name in text:
                        countryName = str(country.name)
                textFileName = Toolkit.textNamingConvention(fileLocation, nameQualifier, countryName, date)
                Toolkit.textFileCompiler(title, date, textFileName, soup)
                dateIndex = dateIndex + 1
                titleIndex = titleIndex + 1
        except UnicodeEncodeError:
            pass

# Articles
fileLocation = '.\\African_Centre_For_Democracy_And_Human_Rights_Studies\\Blog\\Articles\\'
nameQualifier = 'ACHRS_Blog_Articles'
pageNum = 0
moreLinks = True
while moreLinks is True:
    pageNum = pageNum + 1
    linkRequest = requests.get('https://www.acdhrs.org/category/articles/page/' + str(pageNum) + '/')
    linkSoup = BeautifulSoup(linkRequest.content, features='lxml')
    NewsPageDates = []
    NewsPageTitles = []
    NewsPage = linkSoup.find(class_='posts_group lm_wrapper masonry tiles col-3 isotope')
    if NewsPage is None:
        moreLinks = False
    else:
        try:
            for dateInfo in NewsPage.find_all('div', class_='date_label'):
                NewsPageDates.append(dateInfo.text.strip())
            for titleInfo in NewsPage.find_all(class_='entry-title'):
                NewsPageTitles.append(titleInfo.text.strip())
            print(NewsPageDates)
            print(NewsPageTitles)
            dateIndex = 0
            titleIndex = 0
            NewsPageHrefs = []
            for a in NewsPage.find_all('a', href=True):
                NewsPageHrefs.append(a['href'])
            for linkFromList in NewsPageHrefs:
                date = NewsPageDates[dateIndex]
                title = NewsPageTitles[titleIndex]
                article = NewsPlease.from_url(linkFromList)
                request = requests.get(linkFromList)
                soup = BeautifulSoup(request.content, features='lxml')
                soup = soup.find(class_='post-wrapper-content')
                text = soup.text
                countryName = 'Unknown'
                soupRequest = requests.get(linkFromList)
                soup = BeautifulSoup(soupRequest.content, features='lxml')
                for country in pycountry.countries:
                    if country.name in text:
                        countryName = str(country.name)
                textFileName = Toolkit.textNamingConvention(fileLocation, nameQualifier, countryName, date)
                Toolkit.textFileCompiler(title, date, textFileName, soup)
                dateIndex = dateIndex + 1
                titleIndex = titleIndex + 1
        except UnicodeEncodeError:
            pass
# Letters
fileLocation = '.\\African_Centre_For_Democracy_And_Human_Rights_Studies\\Blog\\Letters\\'
nameQualifier = 'ACHRS_Blog_Letters'
pageNum = 0
moreLinks = True
while moreLinks is True:
    pageNum = pageNum + 1
    linkRequest = requests.get('https://www.acdhrs.org/category/documentation/letters/page/' + str(pageNum) + '/')
    linkSoup = BeautifulSoup(linkRequest.content, features='lxml')
    NewsPageDates = []
    NewsPageTitles = []
    NewsPage = linkSoup.find(class_='posts_group lm_wrapper masonry tiles col-3 isotope')
    if NewsPage is None:
        moreLinks = False
    else:
        try:
            for dateInfo in NewsPage.find_all('div', class_='date_label'):
                NewsPageDates.append(dateInfo.text.strip())
            for titleInfo in NewsPage.find_all(class_='entry-title'):
                NewsPageTitles.append(titleInfo.text.strip())
            print(NewsPageDates)
            print(NewsPageTitles)
            dateIndex = 0
            titleIndex = 0
            NewsPageHrefs = []
            for a in NewsPage.find_all('a', href=True):
                NewsPageHrefs.append(a['href'])
            for linkFromList in NewsPageHrefs:
                date = NewsPageDates[dateIndex]
                title = NewsPageTitles[titleIndex]
                article = NewsPlease.from_url(linkFromList)
                request = requests.get(linkFromList)
                soup = BeautifulSoup(request.content, features='lxml')
                soup = soup.find(class_='post-wrapper-content')
                text = soup.text
                countryName = 'Unknown'
                soupRequest = requests.get(linkFromList)
                soup = BeautifulSoup(soupRequest.content, features='lxml')
                for country in pycountry.countries:
                    if country.name in text:
                        countryName = str(country.name)
                textFileName = Toolkit.textNamingConvention(fileLocation, nameQualifier, countryName, date)
                Toolkit.textFileCompiler(title, date, textFileName, soup)
                dateIndex = dateIndex + 1
                titleIndex = titleIndex + 1
        except UnicodeEncodeError:
            pass
