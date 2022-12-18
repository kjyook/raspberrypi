import numpy as np

class Item:
    def __init__(self, spawn_position):
        self.state = 'alive'
        self.position = np.array([spawn_position[0] - 15, spawn_position[1] - 15, spawn_position[0] + 15, spawn_position[1] + 15])
        self.speed = 3

    def move(self, command = None):
        if command['move'] != False:
            if command['left_pressed']:
                self.speed = 2
            
            if command['right_pressed']:
                self.speed = 4

        self.position[0] -= self.speed
        self.position[2] -= self.speed