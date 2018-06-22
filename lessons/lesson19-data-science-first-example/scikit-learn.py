import nltk
import sklearn.feature_extraction.text as FE
# nltk.download('punkt')

with open('text.txt') as f:
    text = f.read()

sentences = nltk.sent_tokenize(text)
# print(sentences)

cv = FE.CountVectorizer()

x = cv.fit_transform(sentences)
print(x.toarray())
print(cv.get_feature_names())