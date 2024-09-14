import pygame
import random

class Bullet:
    def __init__(self,screen,player_position):
        self.screen = screen
        self.bullet_size = 30
        self.bullet_position = player_position
        self.speed = 10  
        
    def CreateEnemy(self):
        pygame.draw.circle(self.screen,"red",self.bullet_position,self.bullet_size)
        
    def MoveToPlayer(self,player_position,player_size):    
        distance = player_position.distance_to(self.bullet_position) - (player_size + self.bullet_size)
        
        if(distance >= 0):
            direction = (player_position - self.bullet_position).normalize()
            self.bullet_position += direction * self.speed