import os
import requests
import xlsxwriter
from bs4 import BeautifulSoup

fileNamesDict = {}


class Toolkit:

    # Used to name and compile text files
    @staticmethod
    def text(fileLocation: object, nameQualifier: object, date: object, country: object, title: object, soup: object) -> object:
        dateForFileName = date.replace(' ', '_')
        countryForFileName = country.replace(' ', '_')
        textFileName = fileLocation + nameQualifier + "_" + countryForFileName + "_" + dateForFileName + ".txt"
        if textFileName in fileNamesDict:
            fileNamesDict[textFileName] = fileNamesDict[textFileName] + 1
        else:
            fileNamesDict[textFileName] = 1
        count = fileNamesDict[textFileName]
        if count >= 2:
            textFileName = fileLocation + nameQualifier + "_" + countryForFileName + "_" + dateForFileName + "_" + str(
                count) + ".txt"
        with open(textFileName, 'w', encoding='utf-8') as file:
            file.write(title + '\n')
            file.write(date + '\n')
            for para in soup.find_all('p'):
                file.write(para.text.strip())

    # This is a project to combine PDF Naming Convention & PDF Content
    @staticmethod
    def pdf(fileLocation, nameQualifier, country, date, pdf):
        dateForFileName = date.replace(' ', '_').replace(',', '_').replace('__', '_')
        countryForFileName = country.replace(' ', '_')
        filename = fileLocation + nameQualifier + "_" + countryForFileName + "_" + dateForFileName + ".pdf"
        if filename in fileNamesDict:
            fileNamesDict[filename] = fileNamesDict[filename] + 1
        else:
            fileNamesDict[filename] = 1
        count = fileNamesDict[filename]
        if count >= 2:
            filename = fileLocation + nameQualifier + "_" + countryForFileName + "_" + dateForFileName + "_" + str(
                count) + ".pdf"
        getpdf = requests.get(pdf)
        with open(filename, 'wb') as file:
            file.write(getpdf.content)

    # Cleans Up File Names
    @staticmethod
    def namingCleanUp(fileLocation):
        for file in os.listdir(fileLocation):
            if file.endswith('_2.txt' or '_2.pdf'):
                pdfOrText = file[-6:]
                changeFile = file[:-6]
                if pdfOrText is "_2.txt":
                    newFile = fileLocation + changeFile + '_1.txt'
                    oldFile = fileLocation + changeFile + '.txt'
                    os.rename(oldFile, newFile)
                elif pdfOrText is "_2.pdf":
                    newFile = fileLocation + changeFile + '_1.pdf'
                    oldFile = fileLocation + changeFile + '.pdf'
                    os.rename(oldFile, newFile)

    # The following methods are works in progress. They have yet to be complete
    # This text compiler aims to be universal for PDFs, Text files, ect. I also would like to make cleanup integrated
    @staticmethod
    def compiler(fileLocation, nameQualifier, date, country, soup=None, text=None, title=None, pdf=None):
        dateForFileName = date.replace(' ', '_')
        countryForFileName = country.replace(' ', '_')
        if pdf is not "N/A":
            fileName = fileLocation + nameQualifier + "_" + countryForFileName + "_" + dateForFileName + ".pdf"
            if fileName in fileNamesDict:
                fileNamesDict[fileName] = fileNamesDict[fileName] + 1
            else:
                fileNamesDict[fileName] = 1
            count = fileNamesDict[fileName]
            if count >= 2:
                fileName = fileLocation + nameQualifier + "_" + countryForFileName + "_" + dateForFileName + "_" + str(
                    count) + ".pdf"
        elif soup is not None or text is not None:
            fileName = fileLocation + nameQualifier + "_" + countryForFileName + "_" + dateForFileName + ".txt"
            if fileName in fileNamesDict:
                fileNamesDict[fileName] = fileNamesDict[fileName] + 1
            else:
                fileNamesDict[fileName] = 1
            count = fileNamesDict[fileName]
            if count >= 2:
                fileName = fileLocation + nameQualifier + "_" + countryForFileName + "_" + dateForFileName + "_" + str(
                    count) + ".pdf"
            with open(fileName, 'w') as file:
                file.write(title + '\n')
                file.write(date + '\n')
                if soup is not None:
                    for para in soup.find_all('p'):
                        file.write(para.text.strip())
                elif text is not None:
                    file.write(text)
        else:
            raise Exception("You did not enter a soup, text, title, or pdf into the argument.")

    # Will be used to loop through pages and return a list of pages to the user for quick use
    @staticmethod
    def pageHREF(website, stopId, stopIdContent, initializer=1, increment=1):
        pageHrefList = []
        bull = True
        num = initializer
        while bull:
            linkRequest = requests.get(website + num + '/')
            linkSoup = BeautifulSoup(linkRequest.content, features='lxml')
            if linkSoup.find(stopID=stopIdContent) is not None:
                pageHrefList.append(website + num + '/')
                num = num + increment
            else:
                bull = False
        return pageHrefList

    # Used to make a 'soup' faster and more simply
    @staticmethod
    def soupMaker(link, htmlMarker, htmlMarkerContent):
        linkRequest = requests.get(link)
        linkSoup = BeautifulSoup(linkRequest.content, features='lxml')
        linkContent = linkSoup.find(htmlMarker=htmlMarkerContent)
        return linkContent

    # Will create a table describing files and there match of title to
    @staticmethod
    def tableMaker(directory, nameQualifier):
        workbook = xlsxwriter.Workbook(nameQualifier)
        worksheet = workbook.add_worksheet()
        worksheet.write('A1', 'Title of File')
        worksheet.write('B1', 'Title in File')
        worksheet.write('C1', 'Matching? (1 for Yes, 0 for No)')
        rowNum = 1
        for fileName in os.listdir(directory):
            rowNum = rowNum + 1
            openFile = open(fileName, 'r')
            worksheet.write('A' + str(rowNum), fileName)
            worksheet.write('B' + str(rowNum), openFile.readline(2))
            if worksheet.cell('A', rowNum) is worksheet.cell('B', rowNum):
                worksheet.write('C' + str(rowNum), 1)
            elif worksheet.cell('A', rowNum) is not worksheet.cell('B', rowNum):
                worksheet.write('C' + str(rowNum), 0)

    # All the old methods that are no longer in use will be found down here. Kept around for older programs
    # Used to make a text file name according to naming convention
    @staticmethod
    def textNamingConvention(fileLocation, nameQualifier, country, date):
        dateForFileName = date.replace(' ', '_')
        countryForFileName = country.replace(' ', '_')
        filename = fileLocation + nameQualifier + "_" + countryForFileName + "_" + dateForFileName + ".txt"
        if filename in fileNamesDict:
            fileNamesDict[filename] = fileNamesDict[filename] + 1
        else:
            fileNamesDict[filename] = 1
        count = fileNamesDict[filename]
        if count >= 2:
            filename = fileLocation + nameQualifier + "_" + countryForFileName + "_" + dateForFileName + "_" + str(
                count) + ".txt"
        return filename

    # Used to compile text files faster
    @staticmethod
    def textFileCompiler(title, date, textFileName, soup):
        with open(textFileName, 'w') as file:
            file.write(title + '\n')
            file.write(date + '\n')
            for para in soup.find_all('p'):
                file.write(para.text.strip())

    # Used to make a pdf file name according to naming convention
    @staticmethod
    def pdfNamingConvention(fileLocation, nameQualifier, country, date):
        dateForFileName = date.replace(' ', '_')
        countryForFileName = country.replace(' ', '_')
        filename = fileLocation + nameQualifier + "_" + countryForFileName + "_" + dateForFileName + ".pdf"
        if filename in fileNamesDict:
            fileNamesDict[filename] = fileNamesDict[filename] + 1
        else:
            fileNamesDict[filename] = 1
        count = fileNamesDict[filename]
        if count >= 2:
            filename = fileLocation + nameQualifier + "_" + countryForFileName + "_" + dateForFileName + "_" + str(
                count) + ".pdf"
        return filename

    # Used to compile PDFs faster
    @staticmethod
    def pdfFileCompiler(pdfFileName, pdf):
        getpdf = requests.get(pdf)
        with open(pdfFileName, 'wb') as file:
            file.write(getpdf.content)
