
from Object import *
from Shape import *

class Cube(Object):
    def __init__(self, x_pos: float, y_pos: float, size: float, x_vel: float, y_vel: float):
        super().__init__()
        self.shape = Shape(
            [
                {
                    'data': {
                        'id': 'main',
                        'type': 'cube',
                        'dimensions': (size, size),
                        'x_pos': x_pos,
                        'y_pos': y_pos,
                        'x_vel': x_vel,
                        'y_vel': y_vel,
                    },
                    'function': {
                        'id': lambda id, delta: id,
                        'type': lambda type, delta: type,
                        'dimensions': lambda dimensions, delta: dimensions,
                        'x_pos': lambda x_pos, delta: x_pos + x_vel*delta,
                        'y_pos': lambda y_pos, delta: y_pos + y_vel*delta,
                        'x_vel': lambda x_vel, delta: x_vel,
                        'y_vel': lambda y_vel, delta: y_vel
                    },
                }
            ],
        )

    def move(self, delta_time: float):
        self.shape.move(delta_time)
