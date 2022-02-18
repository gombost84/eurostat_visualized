
from bs4 import BeautifulSoup
import re

with open('bulklist2.xml', 'r', encoding = 'utf-8') as f:

	soup = BeautifulSoup(f, 'lxml')

	for x in soup.find_all(re.compile(r'nt:.'), {'language': 'fr'}):
		x.decompose()

	for x in soup.find_all(re.compile(r'nt:.'), {'language': 'de'}):
		x.decompose()

	for x in soup.find_all(re.compile(r'nt:.'), {'format': 'html'}):
		x.decompose()

	for x in soup.find_all(re.compile(r'nt:.'), {'format': 'sdmx'}):
		x.decompose()

	with open('file.xml', 'w+', encoding = 'utf-8') as file:
		file.write(str(soup))