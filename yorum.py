import requests
from bs4 import BeautifulSoup
import re


a = []

kitapUrl = "http://www.kitapyurdu.com/kitap/stefan-zweig-seti-10-kitap/441858.html"

r  = requests.get(kitapUrl)
soup = BeautifulSoup(r.text, 'html.parser')

yorumLink = soup.find('span', attrs={"class":"fr"})
yorumLink = re.findall(r"http\S+", str(yorumLink))
yorumLink = str(yorumLink)[2:-17]
yorumLink = re.sub("amp;", '', yorumLink)
print(yorumLink)



r  = requests.get(yorumLink)
soup = BeautifulSoup(r.text, 'html.parser')

yorum = soup.findAll('div', attrs={"class":"review-text"})
for x in yorum:
	a.append(x.text)
print(a[1])

