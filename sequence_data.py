import torch
from torch.utils.data import Dataset


class SequenceDataset(Dataset):
    def __init__(self, x, y, sequence_length=4):
        self.sequence_length = sequence_length
        self.y = y
        self.X = x

    def __len__(self):
        return self.X.shape[0]

    def __getitem__(self, i):
        if i >= self.sequence_length - 1:
            i_start = i - self.sequence_length + 1
            x = self.X[i_start:(i + 1), :]
        else:
            padding = self.X[0].repeat(self.sequence_length - i - 1, 1)
            x = self.X[0:(i + 1), :]
            x = torch.cat((padding, x), 0)

        return x, self.y[i]
