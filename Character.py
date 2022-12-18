import numpy as np
from Item import Item
from Obstacle import Obstacle
from Finish import Finish

class Character:
    def __init__(self, width, height):
        self.alive = 'alive'
        self.position = np.array([width/2 - 20, height/2 - 20, width/2 + 20, height/2 + 20])
        self.center = np.array([(self.position[0] + self.position[2]) / 2, (self.position[1] + self.position[3]) / 2])
        self.bullet = 0

    def move(self,command = None):
        if command['move'] == True:
            if command['up_pressed']:     # moverspeed만큼이 아닌 라인만큼 이동
                self.position[1] -= 5
                self.position[3] -= 5
            
            if command['down_pressed']:
                self.position[1] += 5
                self.position[3] += 5

        self.center = np.array([(self.position[0] + self.position[2]) / 2, (self.position[1] + self.position[3]) / 2]) 


    def collision_check(self, object):
        if object.state == 'alive':
            collision = self.overlap(object.position)

            if collision:
                object.state = 'die'
            
                if isinstance(object, Item):
                    self.bullet += 1

                if isinstance(object,Obstacle):
                    self.alive = 'die'

                if isinstance(object, Finish):
                    self.alive = 'win'

        
    
    def overlap(self, object_position):
        top = max(self.position[1], object_position[1])
        bottom = min(self.position[3], object_position[3])
        left = max(self.position[0], object_position[0])
        right = min(self.position[2], object_position[2])

        if bottom > top and left < right:
            print("makd rec")
            return True
            
        else:
            return False