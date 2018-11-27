import torch as torch
import torch.nn as nn
from torch.autograd import Variable
from torch.nn import Parameter

class SummaRuNNer(nn.Module):
    def __init__(self, **kwargs):
        super(SummaRuNNer, self).__init__()

        self.vocab_size = kwargs['vocab_size']
        self.embedding_dim = kwargs['embedding_dim']
        self.position_size = kwargs['position_size']
        self.position_dim = kwargs['position_dim']
        self.word_input_size = kwargs['word_input_size']
        self.sent_input_size = kwargs['sent_input_size']
        self.word_GRU_hidden_units = kwargs['word_GRU_hidden_units']
        self.sent_GRU_hidden_units = kwargs['sent_GRU_hidden_units']
        
        self.word_embedding = nn.Embedding(self.vocab_size, self.embedding_dim)
        self.word_embedding.weight.data.copy_(torch.from_numpy(kwargs['pretrained_embedding']))
        self.position_embedding = nn.Embedding(self.position_size, self.position_dim)

        self.word_GRU = nn.GRU(
            input_size = self.word_input_size,
            hidden_size = self.word_GRU_hidden_units,
            batch_first = True,
            bidirectional = True)
            
        self.sent_GRU = nn.GRU(
            input_size = self.sent_input_size,
            hidden_size = self.sent_GRU_hidden_units,
            batch_first = True,
            bidirectional = True)
        
        self.tanh = nn.Tanh()
        self.sigmoid = nn.Sigmoid()
    
        self.fc1 = nn.Linear(400, 100)
        self.fc2 = nn.Linear(400, 100)
        
        self.Wc = Parameter(torch.randn(1, 100))
        self.Ws = Parameter(torch.randn(100, 100))
        self.Wr = Parameter(torch.randn(100, 100))
        self.Wp = Parameter(torch.randn(1, 50))
        self.b = Parameter(torch.randn(1))

    def _avg_pooling(self, x, sequence_length):
        result = []
        for index, data in enumerate(x):
            avg_pooling = torch.mean(data[:sequence_length[index][0], :], dim = 0)
            result.append(avg_pooling)
        return torch.cat(result, dim = 0) 
     
    def forward(self, x):
        sequence_length = torch.sum(torch.sign(x), dim = 1).data
        sequence_num = sequence_length.size()[0]

        word_features = self.word_embedding(x)
        word_outputs, _ = self.word_GRU(word_features)

        sent_features = self._avg_pooling(word_outputs, sequence_length)
        sent_outputs, _ = self.sent_GRU(sent_features.view(1, -1, self.sent_input_size))

        doc_features = self._avg_pooling(sent_outputs, [[x.size(0)]])
        doc = torch.transpose(self.tanh(self.fc1(doc_features)), 0, 1)

        outputs = []
        sent_outputs = sent_outputs.view(-1, 2 * self.sent_GRU_hidden_units)
        
        s = Variable(torch.zeros(100, 1)).cuda()
        
        for position, sent_hidden in enumerate(sent_outputs):
            h = torch.transpose(self.tanh(self.fc2(sent_hidden.view(1, -1))), 0, 1)
            position_index = Variable(torch.LongTensor([[position]])).cuda()
            p = self.position_embedding(position_index).view(-1, 1)
            
            content = torch.mm(self.Wc, h)
            salience = torch.mm(torch.mm(h.view(1, -1), self.Ws), doc)
            novelty = -1 * torch.mm(torch.mm(h.view(1, -1), self.Wr), self.tanh(s))
            position = torch.mm(self.Wp, p)
            bias = self.b
            Prob = self.sigmoid(content + salience + novelty + position + bias)
            s = s + torch.mm(h, Prob)
            outputs.append(Prob)
        
        return torch.cat(outputs, dim = 0) 
