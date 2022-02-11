
from Rain import *
from Cube import *
from time import sleep


class CubeInRainSimulator:
    def __init__(self):
        self.current_time = 0.000
        self.delta_time = 0.001
        self.step_time = 1
        self.cube = Cube(
            x_pos=0,
            y_pos=0,
            size=1,
            x_vel=1,
            y_vel=0
        )
        self.plane = (0, 100)
        self.rain = Rain(
            max_height=40,
            mu=0.1,
            sigma=0.02,
            x_vel=1,
            y_vel=1,
            plane=self.plane
        )


    def configure(self):
        pass

    def start(self):
        i = 0
        while True:
            print('Positions at Epoch', i)
            self.step()
            i += 1
            sleep(self.step_time)

    def step(self):
        self.cube.move(self.delta_time)
        self.rain.move(self.delta_time)
        self.cube.check_intersection(self.rain)