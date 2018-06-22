import nltk
import pymorphy2

with open('text.txt') as f:
    text = f.read().lower()

words = nltk.word_tokenize(text)

c = nltk.FreqDist(words)
print(c.most_common(40))

m = pymorphy2.MorphAnalyzer()

meaning = m.parse("пиздець")
print(meaning)