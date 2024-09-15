import pygame
import math
import enemy

class Bullet:
    def __init__(self,screen,pos,direction):
        self.screen = screen
        self.bullet_size = 10
        self.bullet_position = pygame.Vector2(0,0)
        self.speed = 1500  
        
        self.pos = list(pos)
        self.direction = self.normalize(direction)
        self.isHitEnemy = False
        
    def normalize(self, direction):
        magnitude = math.hypot(direction[0], direction[1])
        if magnitude == 0:
            return [0, 0]
        return [direction[0] / magnitude, direction[1] / magnitude]
        
    def Update(self,dt):
        self.bullet_position = pygame.math.Vector2(self.pos[0],self.pos[1])
        self.pos[0] += self.direction[0] * self.speed * dt
        self.pos[1] += self.direction[1] * self.speed * dt
        
    def is_off_screen(self):
        return self.pos[0] < 0 or self.pos[0] > self.screen.get_width() or self.pos[1] < 0 or self.pos[1] > self.screen.get_height()
    
    def HitEnemy(self):
         self.isHitEnemy = True
    
    def draw(self,screen):
        pygame.draw.circle(screen,"red",(int(self.pos[0]), int(self.pos[1])),self.bullet_size)
        
    def FindEnemies(self,enemy_position,enemy_size,targetEnemy):
        distance = self.bullet_position.distance_to(enemy_position) - (enemy_size + self.bullet_size)
        if(distance <= 0):
            self.HitEnemy()
            targetEnemy.GetHit()
            