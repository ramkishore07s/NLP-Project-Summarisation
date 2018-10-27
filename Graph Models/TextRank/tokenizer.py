import nltk

f = open("tagged.txt", "r")

data = f.readlines();

# print(data)

tokenized = []

for i in data:
    # t = nltk.word_tokenize(i)
    t = i.split(" ")
    tokenized.append(t)

# print(tokenized)