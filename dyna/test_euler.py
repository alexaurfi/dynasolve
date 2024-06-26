import unittest 

import world as wd
import interations as inter
import integration_scheme as integ


class TestEulerScheme:
    def test_basic_model(self):
        integration_scheme = integ.EulerScheme()
        interactions = []
        nodes = [[0.0,0.0,0.0] , [1.0,0.0,0.0]]
        interactions.append(inter.Acceleration(0,-1.0,0.0))
        interactions.append(inter.Spring([0],[1], 10.0))
        interactions.append(inter.AirFriction(1.0))
        interactions.append(inter.Fixed([0]))
        world = wd.World(integration_scheme, nodes, interactions)

        for i in range(0,1000):
            world.iterate(0.01)
            print(world.iterations[-1].position)


if __name__ == '__main__':
    unittest.main()