import pygame,sys
from pygame.locals import *


pygame.init()

size = width,height= 320,240
screen =  pygame.display.set_mode(size)

speed = 4
ypos = 0
xpos = 0
bg=0x998877

def spritesheet(file,i,j): #i and j are the location from 0 to N, e.g.: simon is i=4 (5th row) and j=2 (3rd vertial column)

        sheet = pygame.image.load(file)
        sprite0 = sheet.subsurface(i*32,j*32,32,32)
        sprite0rect = sprite0.get_rect()
        return sprite0,sprite0rect

simon, simonRect = spritesheet('sprites.png',4,2)

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    key = pygame.key.get_pressed()
    if key[pygame.K_UP]:ypos-=speed
    if key[pygame.K_DOWN]:ypos+=speed
    if key[pygame.K_RIGHT]:xpos+=speed
    if key[pygame.K_LEFT]:xpos-=speed

    simonRect.left=xpos
    simonRect.top=ypos

    print 'xpos:{} ypos:{}'.format(xpos,ypos)

    screen.fill(bg)
    screen.blit(simon,simonRect)
    pygame.display.flip()
    pygame.time.delay(1000/50)
 
