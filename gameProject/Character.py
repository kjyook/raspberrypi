import numpy as np

moveSpeed = 5

class Character:
    def __init__(self, width, height):
        self.appearance = 'circle'
        self.state = None
        self.position = np.array([width/2 -24, height/2 - 24],[width/2 +24, height/2 + 24])
        self.outline = "#FFFFFF"    #outline -> black

    def move(self,command = None):

        if command == None:
            self.state = None
            self.outline = "#FFFFFF"    #outline -> black
            moveSpeed = 5

        else:
            self.state = 'move'
            self.outline = "#FF0000"    #outline -> red

            if command == 'left_pressed':
                self.position[0] -= moveSpeed
                self.position[2] -= moveSpeed
            
            if command == 'right_pressed':
                self.position[0] += moveSpeed
                self.position[2] += moveSpeed
            
            if command == 'up_pressed':
                moveSpeed = 8
                
            if command == 'down_pressed':
                moveSpeed = 2