import networkx as nx
import matplotlib.pyplot as plt
import sys
from nltk.tokenize import word_tokenize
import pickle

fname = sys.argv[1]
f = open(fname, "r")

sent_tokenize_list = []

data = f.read()
sent_tokenize_list = data.split('\n')
sent_tokenize_list = sent_tokenize_list[:-1]

f.close()

# print(sent_tokenize_list)

no_of_sents = len(sent_tokenize_list)
# print(no_of_sents)

word_scores = {}

with open("wordscores.txt", "r") as file:
    for line in file:
        line = line.strip("\n")
        line = line.split(" ")
        word_scores[line[0]] = float(line[1])

# print(word_scores)
sent_to_id = {}
count = 0

G = nx.Graph()

for i in range(no_of_sents):
    for j in range(i+1,no_of_sents):
        weight = float(0)

        sent1 = sent_tokenize_list[i]
        sent2 = sent_tokenize_list[j]

        if sent1 not in sent_to_id:
            sent_to_id[sent1] = count
            count += 1

        if sent2 not in sent_to_id:
            sent_to_id[sent2] = count
            count += 1

        G.add_node(sent_to_id[sent1])
        G.add_node(sent_to_id[sent2])

        temp1 = sent1
        temp2 = sent2

        sent1 = word_tokenize(sent1)
        sent2 = word_tokenize(sent2)

        for w1 in sent1:
            for w2 in sent2:
                if w1 == w2:
                    if w1 in word_scores:
                        # print(w1,"-->", i,j)
                        weight = weight + word_scores[w1]
        
        w = weight
        G.add_edge(sent_to_id[temp1],sent_to_id[temp2],weight=w)

nx.draw(G)
plt.show()

sent_scores = nx.pagerank(G,0.85)

id_to_sent = {v: k for k, v in sent_to_id.items()}

# print(id_to_sent)

s = [(k, sent_scores[k]) for k in sorted(sent_scores, key=sent_scores.get, reverse=True)]
for k, sent_scores[k] in s:
    v = sent_scores[k]
    # print(k,v)

# print("\n\n\n final summary \n\n\n")

size = 3

selected = []

for i in range(size):
    sent_id = s[i][0]
    selected.append(sent_id)
    print(sent_id)
    # print(id_to_sent[sent_id],'.')

with open('summary.pkl', 'wb') as f:
    pickle.dump(selected, f)
f.close()