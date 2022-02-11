
from Cube import *
from time import sleep


class PlainCubeSimulator:
    def __init__(self):
        self.current_time = 0.000
        self.delta_time = 0.001
        self.step_time = 1
        self.cube = Cube(0, 0, 1, 1, 0)

    def start(self):
        i = 0
        while True:
            print('Positions at Epoch', i)
            self.step()
            i += 1
            sleep(self.step_time)

    def step(self):
        self.cube.move(self.delta_time)
        self.current_time += self.delta_time
