import networkx as nx
from tokenizer import tokenized
import matplotlib.pyplot as plt
from collections import defaultdict

def ngrams(input_list,n):
     return zip(*[input_list[i:] for i in range(n)])

# print("Please enter the grams size for this problem:")
# x = int(input())

x = 10       # size of ngrams is a Hyper parameter to be tuned

grams = []

for input_list in tokenized:
    grams.append(list(ngrams(input_list,x)))

# print(grams)

tags = []

for arr in grams:
    for gram in arr:
        # print(gram)
        temp = []
        for i in range(x):
            sent_tags = gram[i].strip().split("_")
            temp.append(sent_tags)
        tags.append(temp)

# print(tags[0])

edges_list = []
word_id_mapping = {}
id_word_mapping = {}
count = 0

keyword_tags = defaultdict(lambda: 0)
keyword_tags['JJ'] = 1
keyword_tags['JJR'] = 1
keyword_tags['JJS'] = 1
keyword_tags['NN'] = 1
keyword_tags['NNS'] = 1
keyword_tags['NNP'] = 1
keyword_tags['NNPS'] = 1
keyword_tags['RB'] = 1
keyword_tags['RBR'] = 1
keyword_tags['RBS'] = 1
keyword_tags['VB'] = 1
keyword_tags['VBD'] = 1
keyword_tags['VBG'] = 1
keyword_tags['VBN'] = 1
keyword_tags['VBP'] = 1
keyword_tags['VBZ'] = 1

for gram in tags:
    for i in range(x):
        for j in range(x):
            if keyword_tags[gram[i][1]] and keyword_tags[gram[j][1]]:
                
                if gram[i][0].lower() not in word_id_mapping:
                    word_id_mapping[gram[i][0].lower()] = count
                    id_word_mapping[count] = gram[i][0].lower()
                    count += 1
                
                if gram[j][0].lower() not in word_id_mapping:
                    word_id_mapping[gram[j][0].lower()] = count
                    id_word_mapping[count] = gram[j][0].lower()
                    count += 1

                edge = []
                edge.append(word_id_mapping[gram[i][0].lower()])
                edge.append(word_id_mapping[gram[j][0].lower()])
                edges_list.append(edge)

# print(edges_list)

G = nx.Graph()

for edge in edges_list:
    #print(edge[0][0],edge[1][0])
    G.add_node(edge[0])
    G.add_node(edge[1])
    G.add_edge(edge[0],edge[1])

# print(G.nodes(),G.edges())
plt.ion()
plt.show()

nx.draw(G)
plt.draw()
plt.pause(0.5)

all_nodes = G.nodes()

# print("Set damping factor (0-1), normally 0.85")

# d = float(input())

d = 0.85    # Damping factor is another hyperparamter to be tuned.

word_scores = nx.pagerank(G,d)

# print(word_scores)

f = open('wordscores.txt', 'w')

s = [(k, word_scores[k]) for k in sorted(word_scores, key=word_scores.get, reverse=True)]
for k, word_scores[k] in s:
    v = word_scores[k]
    w = id_word_mapping[k]
    # print(w,v)
    f.write("%s %.18f\n" % (w,v))

# f.close()