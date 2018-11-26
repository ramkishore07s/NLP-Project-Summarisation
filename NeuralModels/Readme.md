# Ranking Sentences for Extractive Summarization with Reinforcement Learning

**Architecture: Encoder-Decoder**

## Problem formulation

* In the decoder, each unit of decoder corresponds to a 
sentence in the document. The decision made by the decoder at any time-step (the score given to each sentence) depends on its current hidden state and the 
current sentence.
* Now, given that the decoder makes a decision at each time step based only on its current state and current input (read observation)
 , this can be stated like a classical MDP problem.
* So all the decoder needs to have is a policy to make decisions in each state and input.
* So based on the set of decisions the network makes, we can give a reward to the network.
* The reward is the ROUGE score of the summary selected by the network.
* More specifically, lets say we consider top n (n is a constant) sentences to be part of the summary, always. Then the reward to the 
network will be the ROUGE score of the n sentences with the abstract summary.

## Algorithm

* Link to the <a href='http://www-anw.cs.umass.edu/~barto/courses/cs687/williams92simple.pdf'>paper</a>.
* We use this algorithm to map reward to loss function.
* Then we train the network like any other deep neural network.


      
   
