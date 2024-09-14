import pygame
import math

class Player:
    def __init__(self,screen):
        self.screen = screen
        self.player_size = 30
        self.player_pos = pygame.Vector2(self.screen.get_width() / 2, self.screen.get_height() / 3)

    def CreatePlayer(self):
        pygame.draw.circle(self.screen,"green", self.player_pos,self.player_size)
        
    def PlayerMovement(self,keys, dt):
        move_direction = pygame.math.Vector2(0,0)
        
        if keys[pygame.K_w]:
            move_direction.y = -1
        if keys[pygame.K_s]:
            move_direction.y =1
        if keys[pygame.K_a]:
            move_direction.x = -1
        if keys[pygame.K_d]:
            move_direction.x =1
            
        if move_direction.length() > 0:
            move_direction = move_direction.normalize()
            
        self.player_pos += move_direction * 300 * dt
            
        
    