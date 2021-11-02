#from pathlib import Path
import imageio
from wordcloud import WordCloud
from operator import itemgetter
from textblob import TextBlob
import nltk
from nltk.corpus import stopwords
import wordcloud

stop_words = stopwords.words("english")

more_stops = ['thy, ye, verily, thee, hath, say, thou, art, shall']

stop_words += more_stops

text = TextBlob(('book of John Text.txt').read_text())

noun = []

noun += text.noun_phrases

items = text.word_counts.items()

clean_items = [word for word in items if word[0] in noun and word[0] not in stop_words]

sorted_list = sorted(clean_items, key=itemgetter(1), reverse=True) 

top_sorted = str(sorted_list[:15])

print(top_sorted)

top15 = ' '

for i in top_sorted:
    top15 += i[0]
    top15 += ''
print(top15)

mask_image = imageio.imread('mask_heart.png')

wordcloud = WordCloud(colormap='prism', mask=mask_image, background_color='black')
wordcloud = wordcloud.generate(top15)
wordcloud = wordcloud.to_file('book of John Text heart.png')
