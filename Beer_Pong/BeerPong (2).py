import pygame
from random import randint
import math

pygame.init()
display = [800, 800]
clock = pygame.time.Clock()
window = pygame.display.set_mode(display)
ball = pygame.image.load('ball.png')
ball = pygame.transform.scale(ball, (30, 30))   # to control the size of the ball

x = 800/2   # starting x position for ball
y = 0   # starting y position for ball
radius = 100
position_x = x + 30
position_y = y + 30

black = (0, 0, 0)
white = (255, 255, 255)

score=0
global playing
playing = False
valocity = [randint(4, 8), randint(-8, 8)]

# cups
first_cup = pygame.image.load("cup.png")
first_cup = pygame.transform.scale(first_cup, (100, 100))
first_cup_width = 35
first_cup_pos_x = 0
first_cup_pos_y = 600
first_cup_speed = 0

second_cup = pygame.image.load("cup.png")
second_cup = pygame.transform.scale(first_cup, (100, 100))
second_cup_width = 35
second_cup_pos_x = 380
second_cup_pos_y = 600
second_cup_speed = 0

third_cup = pygame.image.load("cup.png")
third_cup = pygame.transform.scale(first_cup, (100, 100))

third_cup_width = 35
third_cup_pos_x = 600
third_cup_pos_y = 600
third_cup_speed = 0

fourth_cup = pygame.image.load("cup.png")
fourth_cup = pygame.transform.scale(first_cup, (100, 100))
fourth_cup_width = 35
fourth_cup_pos_x = 850
fourth_cup_pos_y = 600
fourth_cup_speed = 0

fifth_cup = pygame.image.load("cup.png")
fifth_cup = pygame.transform.scale(first_cup, (100, 100))
fifth_cup_width = 35
fifth_cup_pos_x = 180
fifth_cup_pos_y = 600
fifth_cup_speed = 0




#colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

play = True
speed=8
clock = pygame.time.Clock()
gameStarted=False
def check():

    global play
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        elif event.type == pygame.KEYDOWN:
            global x,y, first_cup_pos_x, second_cup_pos_x, third_cup_pos_x, fourth_cup_pos_x,gameStarted,score
            if event.key == pygame.K_UP:
                    gameStarted = True
                    score=0
            elif event.key == pygame.K_RIGHT:
                x += 10
            elif event.key == pygame.K_LEFT:
                x -= 10
            for i in range(601):
                    if gameStarted:
                        y = y+i
                        if y >= 600:
                            y = 0


def ballSpeed(increase):
    global speed, y
    if y > 0:
        if increase:
            speed += 0.0001

def GameOver():

    global score,gameStarted,speed
    # speed = 0

    gameStarted=False
    font = pygame.font.Font(None,100)
    text = font.render(str("Game Over"), 100, red)
    window.blit(text, (260,350))



def display():

    global x, y, first_cup_pos_x, second_cup_pos_x, third_cup_pos_x, fourth_cup_pos_x, fifth_cup_pos_x, score, speed

    if score < 0:
        GameOver()

    if score <= 10:
        ballSpeed(False)

    elif score < 20:
        ballSpeed(False)

    elif score > 30:
        ballSpeed(True)
    elif score < 5:
        ballSpeed(False)
    if y <= 600 and gameStarted:
        y += speed
    else:
        y = 0

    # to move the cups in the x direction continuously
    if first_cup_pos_x < 800:
        first_cup_pos_x = first_cup_pos_x + 1
    else:
        first_cup_pos_x = 0
    if second_cup_pos_x < 800:
        second_cup_pos_x = second_cup_pos_x + 1
    else:
        second_cup_pos_x = 0
    if third_cup_pos_x < 800:
        third_cup_pos_x = third_cup_pos_x + 1
    else:
        third_cup_pos_x = 0
    if fourth_cup_pos_x < 800:
        fourth_cup_pos_x = fourth_cup_pos_x + 1
    else:
        fourth_cup_pos_x = 0
    if fifth_cup_pos_x < 800:
        fifth_cup_pos_x = fifth_cup_pos_x + 1
    else:
        fifth_cup_pos_x = 0
    window.blit(ball, (x, y))
    window.blit(first_cup, (first_cup_pos_x, first_cup_pos_y))
    window.blit(second_cup, (second_cup_pos_x, second_cup_pos_y))
    window.blit(third_cup, (third_cup_pos_x, third_cup_pos_y))
    window.blit(fourth_cup, (fourth_cup_pos_x, fourth_cup_pos_y))
    window.blit(fifth_cup, (fifth_cup_pos_x, fifth_cup_pos_y))

# to display the score on our screen

    font = pygame.font.Font(None, 74)
    text = font.render(str("Score :"), 1, black)
    window.blit(text, (150, 10))
    text = font.render(str(score), 1, black)
    window.blit(text, (320, 10))
# to check the score displayed
    if y >= 590:
        if (math.fabs(first_cup_pos_x - x) < 50 or math.fabs(second_cup_pos_x - x) < 50 or math.fabs(
                third_cup_pos_x - x) < 50 or math.fabs(fourth_cup_pos_x - x) < 50 or math.fabs(
                fifth_cup_pos_x - x) < 50):
            score += 1

        else:
            score -= 1


def main():
    while play:
        window.fill(white)
        check()
        display()
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
main()