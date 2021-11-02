from pathlib import Path
import imageio
from wordcloud import WordCloud, STOPWORDS
#import nltk
#from nltk.corpus import stopwords

text = Path('book of John Text.txt').read_text()

#stop_word = nltk.corpus.stopwords.words('english')

more_stops = ['thy, ye, verily, thee, hath, say, thou, art, shall']

#stop_word.extend(more_stops)

STOPWORDS.add('thy')

mask_image = imageio.imread('mask_heart.png')

#wordcloud = WordCloud(stopwords=stop_word, colormap='prism', mask=mask_image, background_color='black')

wordcloud = WordCloud(stopwords=STOPWORDS, colormap='prism', mask=mask_image, background_color='black')

wordcloud = wordcloud.generate(text)

wordcloud = wordcloud.to_file('book of John Text heart.png')

print('done')