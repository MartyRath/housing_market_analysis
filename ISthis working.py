#df = pd.DataFrame(file)

import requests
from bs4 import BeautifulSoup
r=requests.get('https://www.daft.ie/property-for-sale/ireland/houses')

html_doc=r.text
soup=BeautifulSoup(html_doc, features="html.parser")
#print(soup)
print(soup.title.text)

#print(soup.prettify())
#print(request.status_code)
#print(request.text)