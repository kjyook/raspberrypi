import numpy as np

moveSpeed = 5

class Character:
    def __init__(self, width, height):
        self.appearance = 'circle'  #과연 내 캐릭터의 모양도 circle?
        self.state = None
        #24 는 각각의 사이즈 마다 바뀔 수 있게 수정 할 수 도 있음
        self.position = np.array([width/2 -24, height/2 - 2, width/2 +24, height/2 + 24])
        self.center = np.array([(self.position[0] + self.position[2]) / 2, (self.position[1] + self.position[3]) / 2])
        self.outline = "#FFFFFF"    #outline -> black

    def move(self,command = None):

        if command['move'] == False:
            self.state = None
            self.outline = "#FFFFFF"    #outline -> black
            moveSpeed = 5

        else:
            self.state = 'move'
            self.outline = "#FF0000"    #outline -> red

            if command == 'up_pressed':     # moverspeed만큼이 아닌 라인만큼 이동
                self.position[1] += 5
                self.position[3] += 5
            
            if command == 'down_pressed':
                self.position[1] -= 5
                self.position[3] -= 5
            
            if command == 'right_pressed':
                moveSpeed += 1
                
            if command == 'left_pressed':
                moveSpeed -= 1
        self.center = np.array([(self.position[0] + self.position[2]) / 2, (self.position[1] + self.position[3]) / 2]) 