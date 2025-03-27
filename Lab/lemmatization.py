from textblob import TextBlob
import nltk
nltk.download("punkt")
sample_text=TextBlob("Natural Language Processing enables machines to understand and process human languages. It is a fascinating field with numerous applications, such as chatbots and language translation.")
for i in sample_text.words:
        print(i,i.stem())
        print(i,i.lemmatize())
sample_text.sentences
