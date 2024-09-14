import pygame
from enemy import Enemy
from player import Player

pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

running = True
dt = 0
dist = 0
maxEnemy = 8
enemies = [Enemy(screen) for i in range(maxEnemy)]
myPlayer = Player(screen)

def Spawn_enemies():
    for enemy in enemies:
        enemy.CreateEnemy()
        enemy.FindPlayer(myPlayer.player_pos)
        enemy.MoveToPlayer(myPlayer.player_pos,myPlayer.player_size)
        
        
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("gray")
    pygame.draw.rect(screen, (247, 218, 200), pygame.Rect(0,((screen.get_height() / 4) * 3),screen.get_width(),screen.get_height()))
    
    myPlayer.CreatePlayer()
    Spawn_enemies()
 
    keys = pygame.key.get_pressed()
    myPlayer.PlayerMovement(keys,dt)
    

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()