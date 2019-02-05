import os
import requests
from bs4 import BeautifulSoup

fileNamesDict = {}


class WSTK:

    # Used to make a 'soup' faster and more simply
    @staticmethod
    def soupMaker(link, htmlMarkers):
        linkRequest = requests.get(link)
        linkSoup = BeautifulSoup(linkRequest.content, features='lxml')
        linkContent = linkSoup.find(htmlMarkers)
        return linkContent

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

    # Used to compile text files faster
    @staticmethod
    def textFileCompiler(title, date, textFileName, soup):
        with open(textFileName, 'w') as file:
            file.write(title + '\n')
            file.write(date + '\n')
            try:
                for para in soup.find_all('p'):
                    file.write(para.text.strip())
            except Exception:
                pass

    # Used to compile PDFs faster
    @staticmethod
    def pdfFileCompiler(pdfFileName, pdf):
        getpdf = requests.get(pdf)
        with open(pdfFileName, 'wb') as file:
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

    # Will create a table describing files and there match of title to
    @staticmethod
    def tableMaker():
        print("Under Construction")
