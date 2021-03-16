# Run-Away
#Game were there is a red ball as a player that is trying to not touch the white balls.
import pygame
from random import randint
import random
import sys
import math
import os
import time
# IF TRUE WILL DISPLAY INSTRUCTIONS
new = False
# SIZE OF SCREEN
# if changed the game will change to adapt to the size
# CHANGE X ONLY
# Game is best played when x is 600

size_x = 700 # CHANGE THIS NUMBER ONLY 

# X IS 600 MINIMUM
# DONT TOUCH THESE THEY GO WIITH LINES ABOVE
if size_x < 600:
    size_x = 600
size_y = size_x/1.5


# variables
# Frames Per Second
fps = 60

# Starting x and y position for Balls
x = 1
y = 1

# zero for pos
zero = 0

# Timer for calculating when a new ball is added
timer = 0
winning_timer = 2000

# time is used to cheack if you are moving
time = 0

# How many enemies are present on screen
enemy_counter = 2
enemy_knoledge = 2

# Colors for the game
RED = (255,0,0)
WHITE = (255,255,255)
BLACK = (0,0,0)

# Defining the screen
screen_area = size_x * size_y
screen = pygame.display.set_mode((int(size_x), int(size_y)))
pygame.display.set_caption("Survive")

#player size
player_size = screen_area/15000

# ball size
ball_size = screen_area/24000

# how long before new ball is releaced
new_ball_time = 250

# How fast player can move
player_speed = screen_area/60000

# Speed of ball
speed_1 = screen_area/60000 #4
speed_2 = screen_area/30000 #8 
speed_3 = screen_area/120000 #1
speed_4 = screen_area/30000 #8 

# Scoring variables
score = 0
game_beging = True
high_score = 0
start_game = False
game_start = False

# Starting Lines
if new:
    print ("YOU USE THE WASD KEYS TO MOVE ONLY WHEN THE FIRST BALLS IS SENT OUT")
    print ("TO CHOOSE A DIFFICULTY PRESS G = EASY OR H = HARD")
    print ("AFTER PRESSING A DIFFICULTY WAIT A FEW SECONDS AND THE FIRST TWO BALL WILL BE SENT OUT")
    print ("IF YOU DIE PRESS E TO PLAY AGAIN OR YOU CAN PRESS SPACE AT ANYTIME TO END THE GAME")
    print ("HAVE FUN")
# ending lines
move_play = "YOU NEED TO MOVE TO PLAY"
collide_ball = "PLAYER HAS COLLIDED WITH BALL"
space_play = "SPACE BAR WAS PRESSED"

# How long player survived about
seconds = 0

# Game diffuculty when true = hard, false = easy
hard = False

# Player's ability to move
movement = False
collitions = False 

# Clock
clock = pygame.time.Clock()

# setting run as True to run the game
run = True



# Class for the main character
class Player(object):

    def __init__(self, x, y):
        # Setting pos of the player
        
        self.x = size_x - player_size
        self.y = 0
        
        self.rect = pygame.Rect(self.x, self.y, player_size, player_size)
    def move(self):
        global time, run, movement, hard, score, start_game, timer, move_play
        
        key = pygame.key.get_pressed()
        # Movement of the player
        # time makes sure player is moving
        # if player does not move game will stop
        # can only move when movement is True
        if movement:
            time += 1
            if key[pygame.K_s] and self.y < size_y - player_size:
                time = 0
                self.y += player_speed
            if key[pygame.K_w] and self.y >= zero:
                time = 0
                self.y -= player_speed
            if key[pygame.K_a] and self.x >= zero:
                time = 0
                self.x -= player_speed
            if key[pygame.K_d] and self.x < size_x - player_size:
                time = 0 
                self.x += player_speed
            if hard:
                if time > 100:
                    time = 0
                    # printing your high score and how long you survived to acheive the high score
                    print (move_play)

                    # stop player from moving
                    movement = False
            
                    # reseting the score
                    score = 0
                    start_game = 0
                    timer = 0

                    # reseting pos of all obj
                    time_to_play_again()
                

    def draw(self):
        # drawing rect for player
        self.rect = pygame.Rect(self.x, self.y, player_size, player_size)
        

# ball class
class Ball(pygame.sprite.Sprite):
    # Ball class defing movement and colition of ball
    
    def __init__(self, x, y):
        global speed_1, speed_2, speed_3, speed_4
        # setting pos of the ball
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, ball_size, ball_size)

        # setting x and y velocity of the ball
        self.velocity = [randint(int(speed_1),int(speed_2)),randint(int(speed_3),int(speed_4))]

        
    def update(self):
        # ball moving around the screen
        
        self.x += self.velocity[0]
        self.y += self.velocity[1]
        
    def collition_with_walls(self):
        # Check if the ball is bouncing against any of the 4 walls
        if self.x >= size_x - ball_size:
            self.velocity[0] = -self.velocity[0]
        if self.x <= zero:
            self.velocity[0] = -self.velocity[0]
        if self.y >= size_y - ball_size:
            self.velocity[1] = -self.velocity[1]
        if self.y <= zero:
            self.velocity[1] = -self.velocity[1]
    def draw(self):
        # drawing our ball
        self.rect = pygame.Rect(self.x, self.y, ball_size,ball_size)


       
# classes are being defined 
player = Player(50,50)
ball = Ball(x,y)
ball_2 = Ball(x,y)
ball_3= Ball(x,y)
ball_4 = Ball(x,y)
ball_5 = Ball(x,y)
ball_6 = Ball(x,y)
ball_7 = Ball(x,y)
ball_8 = Ball(x,y)
ball_9 = Ball(x,y)
ball_10 = Ball(x,y)
pygame.init()

# functions for the game 

def collition():
    global run, enemy_counter, enemy_knoledge, times_played, score, timer, score_game, movement, seconds, start_game, hard, game_start, collitions, collide_ball
    # cheacking collition between ball and player
    
    if pygame.sprite.collide_rect(ball,player) or pygame.sprite.collide_rect(ball_2,player) or pygame.sprite.collide_rect(ball_3, player) or pygame.sprite.collide_rect(ball_4,player) or pygame.sprite.collide_rect(ball_5,player)or pygame.sprite.collide_rect(ball_6,player) or pygame.sprite.collide_rect(ball_7,player) or pygame.sprite.collide_rect(ball_8,player) or pygame.sprite.collide_rect(ball_9,player) or pygame.sprite.collide_rect(ball_10,player):
        print (collide_ball)
        
        # telling how many balls were present at death
        print ("YOU SURVIVED WITH " + str(enemy_knoledge - 1) + " ENEMIES")
        movement = False
        collitions = False
        game_start = False
        
        # reseting the score
        score = 0
        start_game = 0
        timer = 0

        # reseting pos of all obj
        time_to_play_again()

def game_starting():
    global run, enemy_counter, enemy_knoledge, times_played, score, timer, score_game, movement, seconds, start_game, hard, game_start, collitions, game_beging
    
    key = pygame.key.get_pressed()
    
    # if space is pressed the game will stop and show your high score
    if key[pygame.K_SPACE]:
        print (space_play)
        collitions = False
        run = False
        # printing your high score and how long you survived to acheive the high score
        print ("YOUR HIGH SCORE WAS " + str(high_score))
        seconds = round(high_score/60)
        print ("YOU SURVIVED ABOUT " + str(seconds) + " SECONDS OR EXACTLY " + str(high_score/60) + " seconds")
    
    if key[pygame.K_e]:
        # collitions = True
        game_start = True

    # help know how many balls can be on screen 
    if enemy_counter > enemy_knoledge:
        enemy_knoledge += 1

    # change game difficulty mid game
    if key[pygame.K_c]:
        game_beging = Truef


    if game_beging:

        # setting diffuculty to hard
        if key[pygame.K_h]:
            hard = True
            game_start = True
            game_beging = False

        # setting diffuculty to easy
        if key[pygame.K_g]:
            hard = False
            game_start = True
            game_beging = False
        

def whitch_ball(obj):
    # drawing all balls on screen
    obj.draw()
    obj.collition_with_walls()
    obj.update()
    pygame.draw.rect(screen, WHITE, obj)
def set_ball_pos(pos):
    global speed_1, speed_2, speed_3, speed_4
    # sets pos of balls when
    pos.x = 1
    pos.y = 1
    pos.velocity = [randint(int(speed_1),int(speed_2)),randint(int(speed_3),int(speed_4))]

def time_to_play_again():
    # resetting all balls to there previuse pos to start the game again
    global enemy_knoledge, enemy_counter, ball, ball_2, ball_3, ball_4, ball_5, ball_6, ball_7, ball_8, ball_9, ball_10, size_x, player_size, player_size
    set_ball_pos(ball)
    set_ball_pos(ball_2)
    set_ball_pos(ball_3)
    set_ball_pos(ball_4)
    set_ball_pos(ball_5)
    set_ball_pos(ball_6)
    set_ball_pos(ball_7)
    set_ball_pos(ball_8)
    set_ball_pos(ball_9)
    set_ball_pos(ball_10)
            
    enemy_knoledge = 2
    enemy_counter = 2
    player.x = size_x - player_size
    player.y = zero

# while loop to run the game

while run:
    
    # setiing fps
    clock.tick(fps)
    
    # cheking if you have a high score
    if score > high_score:
        high_score = score
    
    game_starting()


    # using timer to cheack if a ball should be made
    if game_start:
        timer += 1
    
    if timer > new_ball_time:
        movement = True
        enemy_counter += 1
        start_game = True
        timer = 0
        collitions = True 
    
    # when your score begins to increase
    if start_game:
        score += 1

    if score >= winning_timer:
        seconds = round(high_score/fps)
        print ("YOU WIN WITH A HIGHT SCORE OF " + str(score) + " FINISHING IN JUST ABOUT " + str(seconds) + " SECONDS")
        run = False
        
        
    # stop the code
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        if e.type == pygame.K_ESCAPE:
            run = False

    
    # calling player class functions
    player.move()
    player.draw()
 
    pygame.display.flip()
    
    # calling function for collition

    if collitions:
        collition()
    
    # making the backround color
    screen.fill(BLACK)

    # drawing player on the screen
    pygame.draw.rect(screen, RED, player)

    # drawing balls on the screen 
    if enemy_knoledge > 2:
        whitch_ball(ball)
        whitch_ball(ball_2)
        if enemy_knoledge > 3:
            whitch_ball(ball_3)
        if enemy_knoledge > 4:
            whitch_ball(ball_4)
        if enemy_knoledge > 5:
            whitch_ball(ball_5)
        if enemy_knoledge > 6:
            whitch_ball(ball_6)
        if enemy_knoledge > 7:
            whitch_ball(ball_7)
        if enemy_knoledge > 8:
            whitch_ball(ball_8)
        if enemy_knoledge > 9:
            whitch_ball(ball_9)
        if enemy_knoledge > 10:
            whitch_ball(ball_10)


