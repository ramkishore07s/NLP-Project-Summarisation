from nltk.tokenize import sent_tokenize
import string
import networkx as nx
import matplotlib.pyplot as plt

def minimum(a,b):
    if a<b:
        return a
    else:
        return b

f = open("sample.txt", "r")

data = f.read();

# print(data)
d1 = data.replace("?", "? ")
d2 = d1.replace('.', '. ')
data = d2.replace('!', '! ')
data = data.replace("\n",' ')

# print(data)

sent_tokenize_list = sent_tokenize(data)
print(sent_tokenize_list)

f = open('sentence.txt','w')

for i in sent_tokenize_list:
    f.write(i)
    f.write("\n")

no_of_sents = len(sent_tokenize_list)

table = data.maketrans('','',string.punctuation)

for i in range(no_of_sents):
    sent_tokenize_list[i] = sent_tokenize_list[i].translate(table)

# print(sent_tokenize_list)

scores = []
word_scores = {}

with open("wordscores.txt", "r") as file:
    for line in file:
        line = line.strip("\n")
        line = line.split(" ")
        word_scores[line[0]] = float(line[1])

print(word_scores)

G = nx.Graph()

for i in range(no_of_sents):
    for j in range(i+1,no_of_sents):
        weight = float(0)

        sent1 = sent_tokenize_list[i]
        sent2 = sent_tokenize_list[j]

        G.add_node(sent1)
        G.add_node(sent2)

        temp1 = sent1
        temp2 = sent2

        sent1 = sent1.split(" ")
        sent2 = sent2.split(" ")

        print(sent1,sent2)

        for w1 in sent1:
            for w2 in sent2:
                if w1 == w2:
                    # print(w1)
                    if w1 in word_scores:
                        print(w1,"-->", i,j)
                        weight = weight + word_scores[w1]
        
        # print(weight)
        w = weight
        G.add_edge(temp1,temp2,weight=w)

nx.draw(G)
plt.show()

sent_scores = nx.pagerank(G,0.85)

print(sent_scores)

print("\n\n\n final scores \n\n\n")

s = [(k, sent_scores[k]) for k in sorted(sent_scores, key=sent_scores.get, reverse=True)]
for k, sent_scores[k] in s:
    v = sent_scores[k]
    print(k,v)

print("\n\n\n final summary \n\n\n")

size = minimum(10,len(s))

for i in range(size):
    print(s[i][0],".")