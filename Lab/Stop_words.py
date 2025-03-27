from textblob import TextBlob
import nltk
nltk.download("stopwords")
from nltk.corpus import stopwords
stops=stopwords.words('english')
text=TextBlob('Today is a beautiful Day')
print(f'Before Removing StopWords : {text}')
text1=[]
for i in text.words:
        if i not in stops:
                text1.append(i)
text1=" ".join(text1)
print(f'After Removing StopWords : {text1}')
