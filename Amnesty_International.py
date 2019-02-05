from bs4 import BeautifulSoup
import requests
import os
import WSTK
# filenames_dict = {}
fileLocation = ".\\Amnesty_International\\news\\"
nameQualifier = "Amnesty_News"

# def namingConvention(fileLocation, nameQualifier, country, date):
# 	dateForFileName = date.replace(' ','_')
# 	countryForFileName = country.replace(' ','_')
# 	filename = fileLocation + nameQualifier + "_" + countryForFileName + "_" + dateForFileName + ".txt"
# 	if filename in filenames_dict:
# 		filenames_dict[filename] = filenames_dict[filename] + 1
# 	else:
# 		filenames_dict[filename] = 1
# 	count = filenames_dict[filename]
# 	if count >= 2:
# 		filename = fileLocation + nameQualifier + "_" + countryForFileName + "_" + dateForFileName + "_" + str(count) + ".txt"
# 	return filename

# def namingCleanUp():
# 	for file in os.listdir(fileLocation):
# 		if file.endswith('_2.txt'):
# 			changefile = file[:-6]
# 			newfile = fileLocation + changefile + '_1.txt'
# 			oldfile = fileLocation + changefile + '.txt'
# 			os.rename(oldfile, newfile)

for x in range(1,6):
	r = requests.get('https://www.amnesty.org/en/latest/news/?contentType=2561&sort=date&p=' + str(x))
	soup = BeautifulSoup(r.content, features='lxml')

	for article in soup.find_all('article', class_='search-item'):
		content = article.find('div', class_='search-item__content--half')

		title = content.h1.text.strip()
		date = content.time.text.strip()
		country = ""
		if content.p == None:
			country = "No Area Found"
		else:
			country = content.p.text.strip()

		filename = WSTK.namingConvention(fileLocation, nameQualifier, country, date)

		link = article.find('a', class_='search-item__link')['href']
		link = "https://www.amnesty.org" + link
		s = requests.get(link)
		linksoup = BeautifulSoup(s.content, features='lxml')
		linkcontent = linksoup.find('div', class_='wysiwyg')

		with open(filename, 'w') as file:
			file.write(title + '\n')
			file.write(date + '\n')
			for para in linkcontent.find_all('p'):
				p_has_class = para.has_attr("class")
				if p_has_class and para["class"][0] != "share__title":
					file.write(para.text)
				elif not p_has_class:
					file.write(para.text)

namingCleanUp(fileLocation)
