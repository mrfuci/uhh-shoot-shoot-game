import pygame
import  sys

pygame.init()

FPS = 60
RES = (1280,720)
X_POS = 10
Y_POS = 490

Clock = pygame.time.Clock
Screen = pygame.display.set_mode(RES)
pygame.display.set_caption("cockcockcock")

background = pygame.image.load("bg.png")
char = pygame.image.load("gun_guy.png")

while True:
    for EVENT in pygame.event.get():
        if EVENT.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    keys_input = pygame.key.get_pressed()
    
    if keys_input[pygame.K_ESCAPE]:
        pygame.QUIT
        sys.exit()
    if keys_input[pygame.K_d]:
        X_POS += 5
    if keys_input[pygame.K_a]:
        X_POS -= 5
    
    Screen.blit(background, (0,0))
    Screen.blit(char, (X_POS,Y_POS))
    
    
    
    pygame.display.update()
Clock.tick(FPS)