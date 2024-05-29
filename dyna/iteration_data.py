import torchwrap as tw
import torch

class IterationData:
    def __init__(self, nodes, events):
        n_node = len(nodes)
        self.position = torch.Tensor(nodes, device=tw.device).to(tw.numeric_type)
        self.velocity = torch.zeros([n_node, 3], device=tw.device).to(tw.numeric_type)
        self.acceleration = torch.zeros([n_node, 3], device=tw.device).to(tw.numeric_type)
        self.mass = torch.ones([n_node], device=tw.device).to(tw.numeric_type)
