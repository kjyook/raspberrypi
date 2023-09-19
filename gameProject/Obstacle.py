import numpy as np
import time

class Obstacle:
    def __init__(self, spawn_position):
        self.state = 'alive'
        self.position = np.array([spawn_position[0] - 25, spawn_position[1] - 25, spawn_position[0] + 25, spawn_position[1] + 25])
        self.speed = 3

    def move(self, command = None):
        if command['move'] != False:
            if command['left_pressed']:
                self.speed = 2
            
            if command['right_pressed']:
                self.speed = 4

        self.position[0] -= self.speed
        self.position[2] -= self.speed

    def collision_check(self, character):
        collision = self.overlap(self.position, character.position)

        if collision:
            character.alive = 'die'
            self.state = 'hit'

    def overlap(self, enemy_position, character_position):
        return character_position[0] > enemy_position[0] and character_position[1] > enemy_position[1] \
            and character_position[2] < enemy_position[2] and character_position[3] < enemy_position[3]
