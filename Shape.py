
from typing import *


class Shape:
    def __init__(self, parts=None):
        if parts is None:
            parts = []
        self.parts = parts

    def add_parts(self, new_parts):
        self.parts += new_parts

    def move(self, delta_time: float):
        for part in self.parts:
            data = part['data']
            function = part['function']
            new_data = {}
            for k, v in data.items():
                new_data[k] = function[k](v, delta_time)

            print('x:', data['x_pos'])
            print('y:', data['y_pos'])

            part['data'] = new_data


