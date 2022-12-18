from PIL import Image, ImageDraw, ImageFont
import time
import random
from colorsys import hsv_to_rgb
from Joystick import Joystick
from Character import Character
from Obstacle import Obstacle
from Bullet import Bullet
from Item import Item
from Finish import Finish
import threading


def main():

    def make_object():
        sample_list = [25, 73, 121, 169, 215]
        spawn_list = random.sample(sample_list,2)

        temp_enemy = Obstacle((230,spawn_list[0]))
        enemy_list.append(temp_enemy)

        temp_item = Item((230,spawn_list[1]))
        item_list.append(temp_item)

        threading.Timer(2.5,make_object).start()

    def end_game():
        if score < 85:
            my_image.paste(image_die,(0,0))
            joystick.disp.image(my_image)
            quit()  #점수 기준치 미달시 게임 패배
        else:
            temp_finish = Finish((230,115))
            finish_list.append(temp_finish)

#게임 승리!

    #my_character = Image.open() #Todo! -> upload png file
    joystick = Joystick()
    my_image = Image.new("RGBA", (joystick.width, joystick.height))

    image_charcter = Image.open("/home/kau-esw/TA-ESW/gameProject/dk_deft.png")
    background = Image.open("/home/kau-esw/TA-ESW/gameProject/background.png")
    image_enemy = Image.open("/home/kau-esw/TA-ESW/gameProject/enemy.png")
    image_bullet = Image.open("/home/kau-esw/TA-ESW/gameProject/bullet.png")
    image_item = Image.open("/home/kau-esw/TA-ESW/gameProject/item.png")
    image_finish = Image.open("/home/kau-esw/TA-ESW/gameProject/goldkey.png")
    image_win = Image.open("/home/kau-esw/TA-ESW/gameProject/win_game.png")
    image_die = Image.open("/home/kau-esw/TA-ESW/gameProject/end_game.png")

    my_character = Character(50, joystick.height)
    
    enemy_list = []
    item_list = []
    bullet_list = []
    finish_list = []
    score = 0

    make_object()
    threading.Timer(61.5,end_game).start()

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

        if not joystick.button_B.value:
            if my_character.bullet > 0:
                bullet = Bullet(my_character.center, command)
                bullet_list.append(bullet)     #누르면 총알 나가게 할까요 여기서?
                my_character.bullet -= 1
                print("bullet shout",my_character.bullet)
                time.sleep(0.05)
            else:
                print("no bullet")


        for bullet in bullet_list:
            bullet.collision_check(enemy_list)
            bullet.move()

            if bullet.position[0] >= 240:
                bullet_list.remove(bullet)

            if bullet.position[0] < 240 and bullet.state == 'hit':
                score += 5
                print(score)
                bullet_list.remove(bullet)

        for finish in finish_list:
            finish.move(command)
            my_character.collision_check(finish)

        for enemy in enemy_list:
            enemy.move(command)
            my_character.collision_check(enemy)

            if enemy.position[2] <= 0:
                enemy.state = 'die'

            if enemy.state == 'die':
                score += 1
                print(score)
                enemy_list.remove(enemy)


        for item in item_list:
            item.move(command)
            my_character.collision_check(item)

            if item.position[2] <= 0:
                item.state = 'die'

            if item.state == 'die':
                item_list.remove(item)

        if my_character.alive == 'die':
            print("you die")
            my_image.paste(image_die,(0,0))
            joystick.disp.image(my_image)
            quit()

        if my_character.alive == 'win':
            my_image.paste(image_win,(0,0))
            joystick.disp.image(my_image)
            quit()

        my_character.move(command)

        my_image.paste(background,(0,0))
        
        for enemy in enemy_list:
            my_image.paste(image_enemy,(int(enemy.position[0]), int(enemy.position[1])))

        for item in item_list:
            my_image.paste(image_item,(int(item.position[0]), int(item.position[1])))
        
        for bullet in bullet_list:
            my_image.paste(image_bullet,(int(bullet.position[0]), int(bullet.position[1])))

        for finish in finish_list:
            my_image.paste(image_finish,(int(finish.position[0]), int(finish.position[1])))

        my_image.paste(image_charcter,(int(my_character.position[0]), int(my_character.position[1])))

        joystick.disp.image(my_image)


if __name__ == '__main__':
    main()