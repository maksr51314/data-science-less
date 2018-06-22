import nltk
nltk.download('punkt')

with open('text.txt') as f:
    text = f.read()

# print(text)
#
words = nltk.word_tokenize(text)
# print(len(set(words)))
#
#
# sentences = nltk.sent_tokenize(text)
# print(sentences)
#
# print(len(words) / len(sentences))

print(words[300:330])

ss = nltk.SnowballStemmer('russian')
print([ss.stem(w) for w in words[300:330]])
# print([word.lower() for word in words[100:200]])
#
# t = nltk.Text(words)
# print(t.concordance('большой'))
# print(t.similar('большой'))
