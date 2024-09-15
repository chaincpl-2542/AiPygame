import sys
import pygame
from enemy import Enemy
from player import Player
from bullet import Bullet

pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

running = True
dt = 0
dist = 0
maxEnemy = 10
enemies = [Enemy(screen) for i in range(maxEnemy)]
myPlayer = Player(screen)
bullets = []
bulletCD = 0
MaxCD = 15
mouse_pos = pygame.mouse.get_pos()
isShowEnemyLine = False

def Spawn_enemies():
    
    for enemy in enemies:
        if(enemy.isDead == False):
            enemy.CreateEnemy()
            enemy.FindPlayer(myPlayer.player_pos,isShowEnemyLine)
            enemy.MoveToPlayer(myPlayer.player_pos,myPlayer.player_size)
            enemy.Update()
                             
while running:
    
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                if(isShowEnemyLine == True):
                    isShowEnemyLine = False
                else:
                    if(isShowEnemyLine == False):
                        isShowEnemyLine = True

    screen.fill("gray")
    pygame.draw.rect(screen, (247, 218, 200), pygame.Rect(0,((screen.get_height() / 4) * 3),screen.get_width(),screen.get_height()))
    
    myPlayer.CreatePlayer()
    
    Spawn_enemies()
    enemies = [enemy for enemy in enemies if not enemy.isDead]
            
    mouse_pos = pygame.mouse.get_pos()
    pygame.draw.line(screen, "red", myPlayer.player_pos, mouse_pos, width=2)

    if(bulletCD >= MaxCD):
        bulletCD = MaxCD
        
        if pygame.mouse.get_pressed()[0]:
            direction = [mouse_pos[0] - myPlayer.player_pos[0], mouse_pos[1] - myPlayer.player_pos[1]]
            bullets.append(Bullet(screen,myPlayer.player_pos,direction))
        if pygame.mouse.get_pressed()[2]:
            direction = [mouse_pos[0] - myPlayer.player_pos[0], mouse_pos[1] - myPlayer.player_pos[1]]
            bullets.append(Bullet(screen,myPlayer.player_pos,direction))
        
        bulletCD = 0
    else:
        bulletCD += 1
    
    bullets = [bullet for bullet in bullets if not bullet.is_off_screen()]
    bullets = [bullet for bullet in bullets if not bullet.isHitEnemy]
    
    for bullet in bullets:
        if(bullet.isHitEnemy == False):
            bullet.Update(dt)
            bullet.draw(screen)
        
            for enemy in enemies:
                bullet.FindEnemies(enemy.enemy_pos,enemy.enemy_size,enemy)
        
    keys = pygame.key.get_pressed()
    myPlayer.PlayerMovement(keys,dt)
    

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()