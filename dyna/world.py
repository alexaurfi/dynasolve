from iteration_data import IterationData
from typing import List 
from interations import Interaction


class World:
    def __init__(self, integration_scheme, nodes, interactions : List[Interaction]):
        self.iterations = []
        self.integration_scheme = integration_scheme
        for i in range(self.integration_scheme.requiredTimeLength()):
            self.iterations.append(IterationData(nodes, interactions))
        self.interactions = interactions
        for inter in self.interactions:
            inter.initialize(self.iterations[-1])


    def iterate(self, dt):
        self.iterations = self.iterations[1:] + self.iterations[:1]
        self.iterations[-1].acceleration[:,:] = 0.0
        self.iterations[-1].velocity[:,:] = 0.0
        for inter in self.interactions:
            inter.compute_acceleration(self.iterations[-2], self.iterations[-1])
        self.integration_scheme.step(self.iterations, dt)
        for inter in self.interactions:
            inter.project(self.iterations[-1])
