import numpy as np

class Obstacle:
    def __init__(self, spawn_position):
        self.appearance = 'circle'
        self.state = 'alive'
        self.position = np.array([spawn_position[0] - 25, spawn_position[1] - 25, spawn_position[0] + 25, spawn_position[1] + 25])
        self.center = np.array([(self.position[0] + self.position[2]) / 2, (self.position[1] + self.position[3]) / 2])
        self.outline = "#00FF00"

    def move(self):
        while(self.position[3]<240):
            self.position[1] += 5
            self.position[3] += 5