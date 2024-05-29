import iteration_data as itdata
from typing import List 

class EulerScheme:
    def __init__(self):
        pass

    def requiredTimeLength(self) -> int:
        return 2
    
    def step(self, time_steps : List[itdata.IterationData], dt : float ):
        time_steps[-1].velocity = time_steps[0].velocity + time_steps[0].acceleration*dt
        time_steps[-1].position = time_steps[0].position + time_steps[0].velocity*dt
        
