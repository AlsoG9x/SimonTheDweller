import pygame,sys
from pygame.locals import *


pygame.init()

size = width,height= 320,240
screen =  pygame.display.set_mode(size)

speed = 4
ypos = 0
xpos = 0
bg=0x998877

#char = sprite_sheet(16,'sprites.png',pos=(16,0)) 
#charRect = char.get_rect()

char = pygame.image.load("char.bmp")
charRect = char.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    key = pygame.key.get_pressed()
    if key[pygame.K_UP]:ypos-=speed
    if key[pygame.K_DOWN]:ypos+=speed
    if key[pygame.K_RIGHT]:xpos+=speed
    if key[pygame.K_LEFT]:xpos-=speed

    charRect.left=xpos
    charRect.top=ypos

    print 'xpos:{} ypos:{}'.format(xpos,ypos)

    screen.fill(bg)
    screen.blit(char,charRect)
    pygame.display.flip()
    pygame.time.delay(1000/50)
 
