from wordcloud import WordCloud
wordcloud=WordCloud(colormap='prism',background_color='white')
text='Today is a Beautiful Day'
wordcloud=wordcloud.generate(text)
wordcloud=wordcloud.to_file('wordcloud.png')
import matplotlib.pyplot as plt
plt.imshow(wordcloud)
