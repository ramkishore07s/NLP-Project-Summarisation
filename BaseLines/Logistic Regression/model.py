import torch
import torch.nn as nn

class LogisticRegression(nn.Module):
    def __init__(self, no_features=6, no_output=1):
        super(LogisticRegression, self).__init__()
        self.weights = nn.Linear(in_features=6, out_features=1)
        
    def forward(self, input):
        return self.weights(input)