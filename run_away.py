# Run-Away
Game were there is a red ball as a player that is trying to not touch the white balls.
import pygame
from random import randint
import random
import sys
import math
import os

# variables
# Frames Per Second
fps = 60
# Starting x and y position for Balls
x = 1
y = 1
# Timer for calculating when a new ball is added
timer = 0
winning_timer = 0
# time is used to cheack if you are moving
time = 0
# How many enemies are present on screen
enemy_counter = 2
enemy_knoledge = 2
# How fast player can move
player_speed = 4
# Colors for the game
RED = (255,0,0)
WHITE = (255,255,255)
BLACK = (0,0,0)
# Defining the screen
size = (600, 400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Survive")
# Scoring variables
score = 0
high_score = 0
start_game = False
game_start = False
# how long player survived about
seconds = 0

# game diffuculty
hard = False

# player's ability to move
movement = False

#clock
clock = pygame.time.Clock()

# setting run as True to run the game
run = True



# Class for the main character
class Player(object):

    def __init__(self, x, y):
        # Setting pos of the player
        
        self.x = 584
        self.y = 0
        
        self.rect = pygame.Rect(self.x, self.y, 16, 16)
    def move(self):
        global time, run, movement, hard, score, start_game, timer
        
        key = pygame.key.get_pressed()
        # Movement of the player
        # time makes sure player is moving
        # if player does not move game will stop
        # can only move when movement is True
        if movement:
            time += 1
            if key[pygame.K_s] and self.y < 384:
                time = 0
                self.y += player_speed
            if key[pygame.K_w] and self.y > 16:
                time = 0
                self.y -= player_speed
            if key[pygame.K_a] and self.x > 0:
                time = 0
                self.x -= player_speed
            if key[pygame.K_d] and self.x < 584:
                time = 0 
                self.x += player_speed
            if hard:
                if time > 100:
                    time = 0
                    # printing your high score and how long you survived to acheive the high score
                    print ("YOU NEED TO MOVE TO PLAY")

                    #stop player from moving
                    movement = False
            
                    #reseting the score
                    score = 0
                    start_game = 0
                    timer = 0

                    #reseting pos of all obj
                    time_to_play_again()
                

    def draw(self):
        # drawing rect for player
        self.rect = pygame.Rect(self.x, self.y, 16,16)
        

# ball class
class Ball(pygame.sprite.Sprite):
    # Ball class defing movement and colition of ball
    
    def __init__(self, x, y):
        # setting pos of the ball
        self.x = x
        self.y = y

        self.rect = pygame.Rect(self.x, self.y, 10, 10)

        # setting x and y velocity of the ball
        self.velocity = [randint(4,8),randint(1,8)]

        
    def update(self):
        # ball moving around the screen
        
        self.x += self.velocity[0]
        self.y += self.velocity[1]
        
    def collition_with_walls(self):
        
        #Check if the ball is bouncing against any of the 4 walls
        if self.x>=590:
            self.velocity[0] = -self.velocity[0]
        if self.x<=0:
            self.velocity[0] = -self.velocity[0]
        if self.y>390:
            self.velocity[1] = -self.velocity[1]
        if self.y<0:
            self.velocity[1] = -self.velocity[1]
    def draw(self):
        #drawing our ball
        self.rect = pygame.Rect(self.x, self.y, 10,10)

       
#classes are being defined 
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

#functions for the game 


def collition():
    global run, enemy_counter, enemy_knoledge, times_played, score, timer, score_game, movement, seconds, start_game, hard, game_start
    # cheacking collition between ball and player
    if pygame.sprite.collide_rect(ball,player) or pygame.sprite.collide_rect(ball_2,player) or pygame.sprite.collide_rect(ball_3, player) or pygame.sprite.collide_rect(ball_4,player) or pygame.sprite.collide_rect(ball_5,player)or pygame.sprite.collide_rect(ball_6,player) or pygame.sprite.collide_rect(ball_7,player) or pygame.sprite.collide_rect(ball_8,player) or pygame.sprite.collide_rect(ball_9,player) or pygame.sprite.collide_rect(ball_10,player):

        #telling how many balls were present at death
        print ("YOU SURVIVED WITH " + str(enemy_knoledge - 1) + " ENEMIES")
        movement = False
        
        #reseting the score
        score = 0
        start_game = 0
        timer = 0

        #reseting pos of all obj
        time_to_play_again()
    
    key = pygame.key.get_pressed()
    
    # if space is pressed the game will stop and show your high score
    if key[pygame.K_SPACE]:
        run = False
        # printing your high score and how long you survived to acheive the high score
        print ("YOUR HIGH SCORE WAS " + str(high_score))
        seconds = round(high_score/60)
        print ("YOU SURVIVED ABOUT " + str(seconds) + " SECONDS OR EXACTLY " + str(high_score/60) + " seconds")

    # help know how many balls can be on screen 
    if enemy_counter > enemy_knoledge:
        enemy_knoledge += 1

    #setting diffuculty to hard
    if key[pygame.K_h]:
        hard = True
        game_start = True

    #setting diffuculty to easy

    if key[pygame.K_g]:
        hard = False
        game_start = True
        

def whitch_ball(obj):
    # drawing all balls on screen
    obj.draw()
    obj.collition_with_walls()
    obj.update()
    pygame.draw.rect(screen, WHITE, obj)
def set_ball_pos(pos):
    # sets pos of balls when 
    pos.x = 30
    pos.y = 30
    pos.velocity = [randint(4,8),randint(1,8)]

def time_to_play_again():
    # resetting all balls to there previuse pos to start the game again
    
    global enemy_knoledge, enemy_counter
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
    player.x = 500
    player.y = 30

# while loop to run the game

while run:
    # setiing fps
    clock.tick(fps)
    
    # cheking if you have a high score
    if score > high_score:
        high_score = score

    # calling function for collition
    collition()

    #using timer to cheack if a ball should be made
    if game_start:
        timer += 1
    
    if timer > 250:
        movement = True
        enemy_counter += 1
        start_game = True
        timer = 0
    
    # when your score begins to increase
    if start_game:
        score += 1

    if score >= 2500:
        seconds = round(high_score/60)
        print ("YOU WIN WITH A HIGHT SCORE OF " + str(score) + " FINISHING IN JUST ABOUT" + str(seconds) + " SECONDS")
        run = False
        
        
    #stop the code
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        if e.type == pygame.K_ESCAPE:
            run = False

    
    # calling player class functions
    player.move()
    player.draw()
 
    pygame.display.flip()
    
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

        
    
    
    
