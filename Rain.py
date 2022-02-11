
from Object import *
from Shape import *
import random
class Rain(Object):
    def __init__(self, max_height: float, mu: float, sigma:float, x_vel: float, y_vel: float, plane: (int, int)):
        super().__init__()
        self.max_height = max_height
        self.mu = mu
        self.sigma = sigma
        self.x_vel = x_vel
        self.y_vel = y_vel
        self.plane = plane
        self.shape = Shape()

    def generate_particles(self):
        number_of_particles = int((self.plane[1] - self.plane[0])*random.gauss(self.mu, self.sigma))
        particles = list(map(
            lambda _: {
                'data': {
                    'id': 'member',
                    'type': 'point',
                    'x_pos': random.uniform(self.plane[0], self.plane[1]),
                    'y_pos': self.max_height,
                },
                'function': {
                    'id': lambda id, delta: id,
                    'type': lambda type, delta: type,
                    'x_pos': lambda x_pos, delta: x_pos + self.x_vel * delta,
                    'y_pos': lambda y_pos, delta: y_pos + self.y_vel * delta,
                },
            },
            range(number_of_particles)
        ))

        self.shape.add_parts(particles)


    def move(self, delta_time: float):
        self.shape.move(delta_time)
