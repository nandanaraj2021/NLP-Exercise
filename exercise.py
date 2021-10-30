from pathlib import Path
import imageio
from wordcloud import WordCloud
import pandas as pd

text = Path('book of John Text.txt').read_text()

more_stops = ['thy, ye, verily, thee, hath, say, thou, art, shall']

mask_image = imageio.imread('mask_heart.png')

wordcloud = WordCloud(stopwords=more_stops, colormap='prism', mask=mask_image, background_color='black')

wordcloud = wordcloud.generate(text)

wordcloud = wordcloud.to_file('book of John Text heart.png')

print('done')