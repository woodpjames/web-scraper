# This Looks Awful. Need to go back and use toolkit I made

from bs4 import BeautifulSoup
import requests
import os

filenames_dict = {}

def namingConvention(fileLocation, nameQualifier, country, date):
    dateForFileName = date.replace(' ','_')
    countryForFileName = country.replace(' ','_')
    # print("test")
    filename = fileLocation + nameQualifier + "_" + countryForFileName + "_" + dateForFileName
    if filename in filenames_dict:
        filenames_dict[filename] = filenames_dict[filename] + 1
    else:
        filenames_dict[filename] = 1
    count = filenames_dict[filename]
    if count >= 2:
        filename = fileLocation + nameQualifier + "_" + countryForFileName + "_" + dateForFileName + "_" + str(count)
    return filename

def namingCleanUp(fileLocation):
    for file in os.listdir(fileLocation):
        if file.endswith('_2.txt'):
            changefile = file[:-6]
            newfile = fileLocation + changefile + '_1.txt'
            oldfile = fileLocation + changefile + '.txt'
            os.rename(oldfile, newfile)

#MMD_Reports
fileLocation = ".\\AL-HAQ\\Monitoring_and_Documents\\MDD_Reports\\"
nameQualifier = "AL-HAQ_MDD_Reports"
date = "Unlisted"
country = "Palestine"
for x in range(1,4):
    y = (x*12) - 12
    r = requests.get("http://www.alhaq.org/documentation/mdd-reports?start=" + str(y))
    soup = BeautifulSoup(r.content, features='lxml')

    for article in soup.find_all('div', class_='itemContainer itemContainerLast'):
        titleAndLinkContent = article.find(class_='catItemTitle')
        link = 'http://www.alhaq.org' + titleAndLinkContent.find('a')['href']
        title = titleAndLinkContent.text.strip()
        s = requests.get(link)
        linksoup = BeautifulSoup(s.content, features='lxml')
        linkcontent = linksoup.find('div', class_='itemFullText')
        filename = namingConvention(fileLocation, nameQualifier, country, date)
        filenametxt = filename + '.txt'
        with open(filenametxt, 'w') as file:
            file.write(title + '\n')
            file.write(date + '\n')
            try:
                for para in linkcontent.find_all('p'):
                    file.write(para.text.strip())
            except Exception:
                pass

        pdfContent = article.find(class_ = 'catItemAttachments')
        try:
            pdf = 'http://www.alhaq.org' + pdfContent.find('a')['href']
            getpdf = requests.get(pdf)
            filenamepdf = filename + '.pdf'
            with open(filenamepdf, 'wb') as file:
                file.write(getpdf.content)
        except Exception:
            pass

#Fieldworker_Affidavits
fileLocation = ".\\AL-HAQ\\Monitoring_and_Documents\\Fieldworker_Affidavits\\"
nameQualifier = "Fieldworker_Affidavits"
country = "Palestine"
r = requests.get("http://www.alhaq.org/documentation/fieldworkers-affidavits")
soup = BeautifulSoup(r.content, features='lxml')
for library in soup.find_all('div', class_='subCategoryContainer'):
    pagesLeft = True
    y = 0
    while pagesLeft:
        link = 'http://www.alhaq.org/' + library.find('a', class_='subCategoryMore')['href'] + '?start=' + str(y)
        linkpage = requests.get(link)
        linkpagesoup = BeautifulSoup(linkpage.content, features='lxml')
        y = y + 14
        if(linkpagesoup.find(class_= 'catItemTitle') == None):
            pagesLeft = False
        else:
            for article in linkpagesoup.find_all(class_='catItemTitle'):
                title = article.text.strip()
                date = title[-4:]
                aphi = 'http://www.alhaq.org/' + article.find('a')['href']
                aphirequest = requests.get(aphi)
                aphisoup = BeautifulSoup(aphirequest.content, features='lxml')
                aphitext = aphisoup.find('div', class_='itemFullText')
                filenametxt = namingConvention(fileLocation, nameQualifier, country, date) + (".txt")
                with open(filenametxt, 'w') as file:
                    file.write(title + '\n')
                    file.write(date + '\n')
                    for para in aphitext.find_all('p'):
                        try:
                            file.write(para.text.strip())
                        except Exception:
                            pass

#Weekly Focus
fileLocation = ".\\AL-HAQ\\Monitoring_and_Documents\\Weekly_Focus\\"
nameQualifier = "Weekly_Focus"
country = "Palestine"
pagenum = 0
for x in range (0, 11):
    r = requests.get("http://www.alhaq.org/documentation/weekly-focuses?start=" + str(pagenum))
    soup = BeautifulSoup(r.content, features = 'lxml')
    content = soup.find('table')
    for article in content.find_all('tr', { 'class': ['sectiontableentry1','sectiontableentry2'] }):
        title = article.find_next('td').find_next('td').text.strip()
        date = article.find_next('td').find_next('td').find_next('td').text.strip().replace('/','_')
        page = "http://www.alhaq.org/" + article.find('a')['href']
        pagerequest = requests.get(page)
        pagesoup = BeautifulSoup(pagerequest.content, features = "lxml")
        pagecontent = pagesoup.find(class_ ='newsitem_text')
        filenametxt = namingConvention(fileLocation, nameQualifier, country, date) + (".txt")
        with open(filenametxt, 'w') as file:
            file.write(title + '\n')
            file.write(date + '\n')
            for para in pagecontent.find_all('p'):
                file.write(para.text.strip())
    pagenum = pagenum + 30

#Reflections_From_The_Gaza_Strip
fileLocation = ".\\AL-HAQ\\Monitoring_and_Documents\\Reflections_From_The_Gaza_Strip\\"
nameQualifier = "Reflections_From_The_Gaza_Strip"
country = "Gaza_Strip"
page = 0
for x in range (0, 2):
    r = requests.get("http://www.alhaq.org/documentation/reflections-from-the-gaza-strip?start=0" + str(page))
    soup = BeautifulSoup(r.content, features = 'lxml')
    for article in soup(class_="news_item_c"):
        title = article.find(class_='title').text.strip()
        date = article.find(class_="createdate").text.strip()
        link = "http://www.alhaq.org/" + article.find('a')['href']
        linkrequest = requests.get(link)
        linksoup = BeautifulSoup(linkrequest.content, features = "lxml")
        linkcontent = linksoup.find(class_="newsitem_text")
        filenametxt = namingConvention(fileLocation, nameQualifier, country, date) + (".txt")
        filenametxt = filenametxt.replace(":","_")
        print(filenametxt)
        with open(filenametxt, 'w') as file:
            file.write(title + '\n')
            file.write(date + '\n')
            for para in linkcontent.find_all('p'):
                file.write(para.text.strip())

    page = page + 5

#Field_Updates_2015
fileLocation = ".\\AL-HAQ\\Monitoring_and_Documents\\Field_Updates_2015\\"
nameQualifier = "Field_Updates_2015"
country = "Palestine"
page = 0
for x in range (0,2):
    r = requests.get("http://www.alhaq.org/documentation/field-updates-2015?start=" + str(page))
    soup = BeautifulSoup(r.content, features='lxml')
    for article in soup.find_all('tr', { 'class': ['sectiontableentry1','sectiontableentry2'] }):
        title = article.find_next('td').find_next('td').text.strip()
        date = article.find_next('td').find_next('td').find_next('td').text.strip().replace('/','_')
        stuff = "http://www.alhaq.org/" + article.find('a')['href']
        pagerequest = requests.get(stuff)
        pagesoup = BeautifulSoup(pagerequest.content, features = "lxml")
        pagecontent = pagesoup.find(class_ ='newsitem_text')
        filenametxt = namingConvention(fileLocation, nameQualifier, country, date) + (".txt")
        with open(filenametxt, 'w') as file:
            file.write(title + '\n')
            file.write(date + '\n')
            for para in pagecontent.find_all('p'):
                file.write(para.text.strip())
        page = page + 5

#Publications
fileLocation = ".\\AL-HAQ\\Publications\\Large_Scale_Publications\\"
nameQualifier = "Publications"
country = "Palestine"
r = requests.get("http://www.alhaq.org/publications/publications-index")
soup = BeautifulSoup(r.content, features='lxml')
for article in soup.find_all(class_="category"):
    pagesLeft = True
    pagecount = 1
    while pagesLeft:
        page = 'http://www.alhaq.org' + article.find('a')['href'] + "/" + str(pagecount)
        print(page)
        pagerequest = requests.get(page)
        pagesoup = BeautifulSoup(pagerequest.content, features='lxml')
        check = pagesoup.find(class_="pos-title")
        if check is None:
            pagesLeft = False
        else:
            for pagecontent in pagesoup.find_all(class_="pos-title"):
                title = pagecontent.find(class_="pos-title")
                link = 'http://www.alhaq.org' + pagecontent.find('a')['href']
                linkrequest = requests.get(link)
                linksoup = BeautifulSoup(linkrequest.content, features='lxml')
                pdfContent = linksoup.find(class_="pos-specification")
                try:
                    pdf = 'http://www.alhaq.org' + pdfContent.find('a')['href']
                    date = 'needToFindDate'
                    getpdf = requests.get(pdf)
                    filename = namingConvention(fileLocation, nameQualifier, country, date)
                    filenamepdf = filename + '.pdf'
                    with open(filenamepdf, 'wb') as file:
                        file.write(getpdf.content)
                except:
                    pass
        pagecount = pagecount + 1