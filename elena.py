from collections import defaultdict
from wordcloud import WordCloud


text = open('text.txt').read()

alphanumeric = ""

for character in text:
    if character == ' ' or character == '\n':
        alphanumeric += ' '
    elif character.isalnum():
        alphanumeric += character

texts = alphanumeric.split()
m = defaultdict(int)

for t in texts:
    m[t.lower()] += 1

# for key, value in sorted(m.items(), key=lambda item: item[1]):
    # print(f'{key}:{value}')

wc = WordCloud(font_path='./NotoSansKR-Light.otf', background_color="white")
wc = wc.generate_from_frequencies(m)
wc.to_file('test.jpg')
