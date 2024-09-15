import pygame
import random
import math


class Enemy:
    def __init__(self,screen):
        self.screen = screen
        self.enemy_size = 30
        self.enemy_pos = pygame.Vector2(random.uniform(0,self.screen.get_width()),random.uniform(((self.screen.get_height() / 4) * 3), self.screen.get_height()))
        self.speed = 2  
        self.color = (random.uniform(0,255),random.uniform(0,255),random.uniform(0,255))
        self.enemyHP = 1
        self.isDead = False

    def CreateEnemy(self):
        pygame.draw.circle(self.screen,self.color,self.enemy_pos,self.enemy_size)
        
    def FindPlayer(self,player_position):
        pygame.draw.line(self.screen, self.color, self.enemy_pos, player_position, width=1)
        
    def MoveToPlayer(self,player_position,player_size):    
        distance = player_position.distance_to(self.enemy_pos) - (player_size + self.enemy_size)
        
        if(distance >= 0):
            direction = (player_position - self.enemy_pos).normalize()
            self.enemy_pos += direction * self.speed
        
    def Update(self):
        if(self.enemyHP <= 0):
            self.Respawn()
    
    def GetHit(self):
        self.enemyHP -= 1
        
    def Respawn(self):
        self.enemy_pos = pygame.Vector2(random.uniform(0,self.screen.get_width()),random.uniform(((self.screen.get_height() / 4) * 3), self.screen.get_height()))
        self.enemyHP = 1