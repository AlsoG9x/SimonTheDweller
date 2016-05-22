import pygame,sys,os
from pygame.locals import *

""" CONSTANTS """
size = width,height= 320,240
speed = 4
ypos = 32
xpos = 32
bg=0x998877

os.environ["SDL_VIDEO_CENTERED"] = "1"
pygame.init()

screen =  pygame.display.set_mode(size)


#Sprite Sheet function
def spritesheet(file,i,j):
#i and j are the location from 0 to N, e.g.: simon is i=4 (5th row) and j=2 (3rd column)
        sheet = pygame.image.load(file)
        sprite0 = sheet.subsurface(i*32,j*32,32,32)
        sprite0rect = sprite0.get_rect()
        return sprite0,sprite0rect

#Importing sprites from the Spritesheet
simon, simonRect = spritesheet('sprites.png',4,2)
block, blockRect = spritesheet('sprites.png',39,17)


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    #Player Mouvement Inputs
    key = pygame.key.get_pressed()
    if key[pygame.K_UP]|key[pygame.K_z]:ypos-=speed
    if key[pygame.K_DOWN]|key[pygame.K_s]:ypos+=speed
    if key[pygame.K_RIGHT]|key[pygame.K_d]:xpos+=speed
    if key[pygame.K_LEFT]|key[pygame.K_q]:xpos-=speed
    
    #World Boundaries
    while (xpos > width-32):
        xpos -= 1
    while (xpos < 0):
        xpos += +1
    
    while (ypos > height-32):
        ypos -= 1
    while (ypos < 0):
        ypos += 1
    
    #Set the player postion
    simonRect.left=xpos
    simonRect.top=ypos
    
    #Debug line
    print 'xpos:{} ypos:{}'.format(xpos,ypos)
    
    #Display and update everything
    screen.fill(bg)
    screen.blit(simon,simonRect)
    screen.blit(block,blockRect)
    pygame.display.update()
    pygame.time.delay(1000/50)
 
