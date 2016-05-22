import pygame,sys,os
from pygame.locals import *

""" CONSTANTS """
zsh:1: command not found: q
speed = 4
ypos = 32
xpos = 32
bg=0x998877

os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()

screen =  pygame.display.set_mode(size)

def spritesheet(file,i,j): #i and j are the location from 0 to N, e.g.: simon is i=4 (5th row) and j=2 (3rd vertial column)

        sheet = pygame.image.load(file)
        sprite0 = sheet.subsurface(i*32,j*32,32,32)
        sprite0rect = sprite0.get_rect()
        return sprite0,sprite0rect

simon, simonRect = spritesheet('sprites.png',4,2)
block, blockRect = spritesheet('sprites.png',39,17)




level = [
"WWWWWWWWWW"
"W        W"
"W        W"
"W        W"
"W        W"
"W        W"
"W        W"
"WWWWWWWWWW"
        ]




while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    key = pygame.key.get_pressed()
    if key[pygame.K_UP]:ypos-=speed
    if key[pygame.K_DOWN]:ypos+=speed
    if key[pygame.K_RIGHT]:xpos+=speed
    if key[pygame.K_LEFT]:xpos-=speed
    
    while (xpos > width-32):
        xpos -= 1
    while (xpos < 0):
        xpos += +1
    
    while (ypos > height-32):
        ypos -= 1
    while (ypos < 0):
        ypos += 1

    simonRect.left=xpos
    simonRect.top=ypos

    print 'xpos:{} ypos:{}'.format(xpos,ypos)

    screen.fill(bg)
    screen.blit(simon,simonRect)
    screen.blit(block,blockRect)
    pygame.display.update()
    pygame.time.delay(1000/50)
 
