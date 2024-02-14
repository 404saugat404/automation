import torch
from torch import nn 

class IntentModelClassifier(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(IntentModelClassifier, self).__init__()
        self.LinearLayer = nn.Sequential(
                nn.Linear(input_size, hidden_size),
                nn.ReLU(),
                nn.Linear(hidden_size, hidden_size),
                nn.ReLU(),
                nn.Linear(hidden_size, output_size),
        )

    def forward(self, x):
        x = self.LinearLayer(x)
        return x

