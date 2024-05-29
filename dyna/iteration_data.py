import torchwrap as tw
import torch

class IterationData:
    def __init__(self, nodes, events):
        n_node = len(nodes)
        self.position = torch.Tensor(nodes, dtype=tw.numeric_type, device=tw.device)
        self.velocity = torch.zeros([n_node, 3], dtype=tw.numeric_type, device=tw.device)
        self.acceleration = torch.zeros([n_node, 3], dtype=tw.numeric_type, device=tw.device)
        self.mass = torch.ones([n_node], dtype=tw.numeric_type, device=tw.device)
