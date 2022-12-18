import numpy as np

class Bullet:
    def __init__(self, position, command):
        self.speed = 8
        self.position = np.array([position[0]-13, position[1]-10, position[0]+12, position[1]+10])
        self.state = None

    def move(self):
        self.position[0] += self.speed
        self.position[2] += self.speed
            
    def collision_check(self, enemys):
        for enemy in enemys:
            collision = self.overlap(enemy.position)
            
            if collision:
                enemy.state = 'die'
                self.state = 'hit'

    def overlap(self, other_position):
        top = max(self.position[1], other_position[1])
        bottom = min(self.position[3], other_position[3])
        left = max(self.position[0], other_position[0])
        right = min(self.position[2], other_position[2])

        if bottom > top and left < right:
            return True
            
        else:
            return False