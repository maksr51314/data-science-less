text = 'aaa bb cc aaa bb'

w = {}

def word_gen():
    word = ''
    while True:
        try:

            char = yield
            if char == ' ':
                return word
            word += char
        except ValueError:
            return word

def word_counter():
    while True:
        wg = word_gen()
        # next(wg)
        word = yield from wg
        if word not in w:
            w[word] = 1
        else:
            w[word] += 1

wc = word_counter()
next(wc)
for char in text:
    wc.send(char)

print(w)