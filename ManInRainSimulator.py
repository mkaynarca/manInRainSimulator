
from Rain import *
from Man import *


class ManInRainSimulator:
    def __init__(self):
        self.rain_config = None
        self.man_config = None
        self.current_time = 0.000
        self.delta_time = 0.001
        self.man = None
        self.rain = None

    def configure(self):
        pass

    def start(self):
        pass

    def step(self):
        self.man.move(self.delta_time)
        self.rain.move(self.delta_time)
        self.man.check_intersection(self.rain)