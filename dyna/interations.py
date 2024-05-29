from iteration_data import IterationData
import torchwrap as tw
import torch

class Interaction:
    def __init__(self):
        pass

    def initialize(self, iteration_data : IterationData):
        pass

    def compute_acceleration(self, current_state : IterationData, next_state : IterationData):
        pass

    def project(self, next_state : IterationData):
        pass


class Acceleration(Interaction):
    def __init__(self, x : float, y : float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def compute_acceleration(self, current_state : IterationData, next_state : IterationData):
        next_state.acceleration[:,0] += self.x
        next_state.acceleration[:,1] += self.y
        next_state.acceleration[:,2] += self.z


class Fixed(Interaction):
    def __init__(self, indexes : torch.Tensor):
        self.indexes = indexes

    def project(self, next_state : IterationData):
        next_state.position[self.indexes,0] = 0.0
        next_state.position[self.indexes,1] = 0.0
        next_state.position[self.indexes,2] = 0.0

class Spring(Interaction):
    def __init__(self, idx_A : torch.Tensor, idx_B : torch.tensor, stiffness : float):
        self.idx_A = idx_A
        self.idx_B = idx_B
        self.stiffness = stiffness


    def initialize(self, iteration_data : IterationData):
        dx = iteration_data[self.idx_B,:] - iteration_data[self.idx_A,:]
        self.L0 = torch.norm(dx, dim=1)

    def compute_acceleration(self,current_state : IterationData, next_state : IterationData):
        dx = current_state[self.idx_B,:] - current_state[self.idx_A,:]
        L = torch.norm(dx, dim=1)
        dir = dx/L
        dL = L - self.L0
        F = -dL*self.stiffness*dir
        next_state.acceleration[self.idx_A] += F/current_state.mass[self.idx_A]
        next_state.acceleration[self.idx_B] -= F/current_state.mass[self.idx_B]


class AirFriction(Interaction):
    def __init__(self, coefficient : float):
        self.coef = coefficient

    def compute_acceleration(self,current_state : IterationData, next_state : IterationData):
        next_state.acceleration -= current_state.velocity*self.coef