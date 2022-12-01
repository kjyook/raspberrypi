from PIL import Image, ImageDraw, ImageFont
import time
import random
import cv2 as cv
import numpy as np
from colorsys import hsv_to_rgb
from Joystick import Joystick
from Character import Character
from Obstacle import Obstacle

def main():
    #my_character = Image.open() #Todo! -> upload png file
    joystick = Joystick()
    my_image = Image.new("RGB", (joystick.width, joystick.height))
    my_draw = ImageDraw.Draw(my_image)
    my_draw.rectangle((0, 0, joystick.width, joystick.height), fill=(255, 0, 0, 100))
    joystick.disp.image(my_image)
    # 잔상이 남지 않는 코드 & 대각선 이동 가능
    my_circle = Character(50, joystick.height)
    my_draw.rectangle((0, 0, joystick.width, joystick.height), fill = (255, 255, 255, 100))
    enemy_1 = Obstacle((230,30))

    while True:
        command = {'move': False, 'up_pressed': False , 'down_pressed': False, 'left_pressed': False, 'right_pressed': False}
        
        if not joystick.button_U.value:  # up pressed
            command['up_pressed'] = True
            command['move'] = True

        if not joystick.button_D.value:  # down pressed
            command['down_pressed'] = True
            command['move'] = True

        if not joystick.button_L.value:  # left pressed
            command['left_pressed'] = True
            command['move'] = True

        if not joystick.button_R.value:  # right pressed
            command['right_pressed'] = True
            command['move'] = True

        my_circle.move(command)
        enemy_1.move()

        my_draw.rectangle((0, 0, joystick.width, joystick.height), fill = (255, 255, 255, 100))
        my_draw.ellipse(tuple(my_circle.position), outline = my_circle.outline, fill = (0, 0, 0))
        
        my_draw.ellipse(tuple(enemy_1.position), outline = enemy_1.outline, fill = (255, 0, 0))
        
        joystick.disp.image(my_image)

        

if __name__ == '__main__':
    main()