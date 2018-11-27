# Ranking Sentences for Extractive Summarization with Recurrent Neural Networks

**Architecture: Bidirectional Gated Recurrent Unit**

## Problem formulation

* The first layer of the RNN runs at the word level, and computes hidden state representations at each word position sequentially, based on the current word embeddings and the previous hidden state. We also use another RNN at the word level that runs backwards from the last word to the first, and
we refer to the pair of forward and backward RNNs as a bidirectional RNN. 

* Similarly, we have a  bi-directional RNN that runs at the sentence-level and accepts
the average-pooled, concatenated hidden states of the bi-directional word-level RNNs as input.

* The hidden states of the second layer RNN encode the representations of the sentences in the document. The representation of the entire document is then modeled as a non-linear transformation of the average pooling of the concatenated hidden states of the bi-directional sentence-level RNN.

* For classification, each sentence is revisited sequentially in a second pass, where a logistic layer makes a binary decision as to whether that sentence belongs to the summary, as shown below.

## Reference

* Link to the <a href='https://arxiv.org/pdf/1611.04230.pdf'>paper</a>.


