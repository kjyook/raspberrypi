import numpy as np

class Finish:
    
    def __init__(self, spawn_position):
        self.position = np.array([spawn_position[0] - 25, spawn_position[1] - 25, spawn_position[0] + 25, spawn_position[1] + 25])
        self.state = 'alive'
        self.speed = 3

    def move(self, command = None):
        if command['move'] != False:
            if command['left_pressed']:
                self.speed = 2
            
            if command['right_pressed']:
                self.speed = 4

        self.position[0] -= self.speed
        self.position[2] -= self.speed