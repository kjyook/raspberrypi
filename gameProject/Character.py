import numpy as np

class Character:
    def __init__(self, width, height):
        self.appearance = 'circle'
        self.state = None
        #20은 내가 조정할 수 있는 크기
        self.position = np.array([width/2 - 20, height/2 - 20, width/2 + 20, height/2 + 20])
        # 총알 발사를 위한 캐릭터 중앙 점 추가
        self.center = np.array([(self.position[0] + self.position[2]) / 2, (self.position[1] + self.position[3]) / 2])
        self.outline = "#FFFFFF"

    def move(self,command = None):
        if command['move'] == False:
            self.state = None
            self.outline = "#FFFFFF"    #outline -> black

        else:
            self.state = 'move'
            self.outline = "#FF0000"    #outline -> red

            if command['up_pressed']:     # moverspeed만큼이 아닌 라인만큼 이동
                self.position[1] -= 5
                self.position[3] -= 5
            
            if command['down_pressed']:
                self.position[1] += 5
                self.position[3] += 5
            
            if command['right_pressed']:
                return
                
            if command['left_pressed']:
                return

        self.center = np.array([(self.position[0] + self.position[2]) / 2, (self.position[1] + self.position[3]) / 2]) 