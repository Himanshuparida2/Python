import requests
response=requests.get('https://www.python.org')
response.content #gives back the Page's HTML
from bs4 import BeautifulSoup
soup=BeautifulSoup(response.content,'html5lib')
text=soup.get_text(strip=True)
from textblob import TextBlob
textblob=TextBlob(text)
TextWords=textblob.words
from nltk.corpus import stopwords
stop=stopwords.words('english')
words=[word for word in TextWords if word not in stop]
print(words)
