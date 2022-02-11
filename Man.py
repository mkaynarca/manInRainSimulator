
from Object import *

class Man(Object):
    def __init__(self):
        self.shape = None

    def move(self):
        self.shape.move()