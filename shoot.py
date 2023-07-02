import pygame
import  sys

pygame.init()

FPS = 60
Y_RES = 720
X_RES = 1320
X_POS = 10
Y_POS = 490
Y_GRAV = 1
JUMP_HEIGHT = 18
Y_VELOC = JUMP_HEIGHT

jumping = False 

Clock = pygame.time.Clock
Screen = pygame.display.set_mode((X_RES, Y_RES))
pygame.display.set_caption("cockcockcock")

background = pygame.image.load("bg.png")

char_left = pygame.image.load("gun_guy_left.png")
char = pygame.image.load("gun_guy.png")
char_left_bang = pygame.image.load("gun_guy_left_bang.png")
char_bang = pygame.image.load("gun_guy_bang.png")
char_crouch = pygame.image.load("gun_guy_crouch.png")

if X_POS >= 1280:
    print("cock")

while True:
    for EVENT in pygame.event.get():
        if EVENT.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    Screen.blit(background, (0,0))
    Screen.blit(char, (X_POS,Y_POS))
    
    if jumping:
        Y_POS -= Y_VELOC
        Y_VELOC -= Y_GRAV
        if Y_VELOC < -JUMP_HEIGHT:
            jumping = False
            Y_VELOC = JUMP_HEIGHT
    
    keys_input = pygame.key.get_pressed()
    
    if keys_input[pygame.K_ESCAPE]:
        pygame.QUIT
        sys.exit()
    if keys_input[pygame.K_d]:
        X_POS += 5
    if keys_input[pygame.K_a]:
        Screen.blit(char_left, (X_POS, Y_POS))
        X_POS -= 5
    if keys_input[pygame.K_w]:
        jumping = True
    if keys_input[pygame.K_s]:
        Screen.blit(char_crouch,(X_POS,Y_POS))
    if keys_input[pygame.K_j]:
        Screen.blit(char_left_bang,(X_POS,Y_POS))
    if keys_input[pygame.K_l]:
        Screen.blit(char_bang,(X_POS,Y_POS))

    if X_POS < 0:
        X_POS = 0
    if Y_POS <0:
        Y_POS = 0
    if X_POS > X_RES - 96:
        X_POS = X_RES - 96
    if Y_POS > Y_RES - 139:
        Y_POS = Y_RES - 139
    


        
    pygame.display.update()
    
Clock.tick(FPS)