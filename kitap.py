import requests
from bs4 import BeautifulSoup
import re

kitapUrl = "http://www.kitapyurdu.com/index.php?route=product/search&filter_name=Steve%20Jobs%20Walter%20Isaacson"

r  = requests.get(kitapUrl)
soup = BeautifulSoup(r.text, 'html.parser')

yorumLink = soup.findAll('div', attrs={"id":"product-table"})
for y in yorumLink:
	a = re.findall(r"http\S+", str(y))
	print(a[1])
