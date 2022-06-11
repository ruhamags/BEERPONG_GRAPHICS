import numpy as np
import pygame
from pygame.locals import *
from random import randint


display = [800, 600]



pygame.display.set_caption('Beer pong')
pong = pygame.image.load('images.jpg')
x, y = (0, 400)





first_cup = pygame.image.load("cup.jpg")
second_cup = pygame.image.load("cup.jpg")
third_cup = pygame.image.load("cup.jpg")
fourth_cup = pygame.image.load("cup.jpg")
fifth_cup = pygame.image.load("cup.jpg")

first_cup_width = 35
first_cup_pos_x = 0
first_cup_pos_y = 600


second_cup_width = 35
second_cup_pos_x = 350
second_cup_pos_y = 600



third_cup_width = 35
third_cup_pos_x = 550
third_cup_pos_y = 600


fourth_cup_width = 35
fourth_cup_pos_x = 850
fourth_cup_pos_y = 600

white = (255, 255, 255)





def main():
    pygame.init()
    window = pygame.display.set_mode(display)

    while True:

        window.blit(pong, (x, y))
        window.blit(first_cup, (first_cup_pos_x, first_cup_pos_y))
        window.blit(second_cup, (second_cup_pos_x, second_cup_pos_y))
        window.blit(third_cup, (third_cup_pos_x, third_cup_pos_y))
        window.blit(fourth_cup, (fourth_cup_pos_x, fourth_cup_pos_y))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


main()