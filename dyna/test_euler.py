import unittest 

import world as wd
import interations as inter
import integration_scheme as integ


class TestEulerScheme(unittest.TestCase):
    def test_basic_integration(self):
        pass
    
    def test_pendulum(self):
        integration_scheme = integ.EulerScheme()
        interactions = []
        nodes = [[0.0,0.0,0.0] , [1.0,0.0,0.0]]
        interactions.append(inter.Acceleration(0,-1.0,0.0))
        interactions.append(inter.Spring([0],[1], 20.0))
        interactions.append(inter.AirFriction(1.0))
        interactions.append(inter.Fixed([0]))
        world = wd.World(integration_scheme, nodes, interactions)

        
        for i in range(0,50):
            for j in range(0,20):
                world.iterate(0.01)
        print(world.iterations[-2].position)
        print(world.iterations[-1].position)
        assert abs( world.iterations[-1].position[0,0] ) < 0.0001
        assert abs( world.iterations[-1].position[0,1] ) < 0.0001
        assert abs( world.iterations[-1].position[1,0]  - 0.0061) < 0.0001
        assert abs( world.iterations[-1].position[1,1]  + 1.05) < 0.0001


if __name__ == '__main__':
    unittest.main()