import pygame, sys
from pygame.locals import *

#Variables
PlayerPos = [64,64]
WindowSize = [640,640]
PlayerSpeed = 32 #Player Speed in pixel per fps
MoveCD = 100 #Cooldown before the Player is able to move again in millisecond

#Init game and screen (window)
pygame.init()
screen = pygame.display.set_mode(WindowSize)

#Sprite Sheet function
def Spritesheet(file,i,j,x,y):
    sheet = pygame.image.load(file)
    sprite = sheet.subsurface(i*32,j*32,x,y)
    spriteRect = sprite.get_rect()
    return sprite,spriteRect
    #i and j are the location from 0 to N, e.g.: simon is i=4 (5th row) and j=2 (3rd column). x and y are the size we want to select e.g.: 32x32 => x=32 y )32

#Player function
def Player(sprite,spriteRect,posX,posY):
    spriteRect.left = posX
    spriteRect.top = posY
    PlayerPos = [posX, posY]
    screen.blit(sprite,spriteRect)
    #print 'posXY: {} {}'.format(posX, posY)
    #print 'playerpos: {} {}'.format(PlayerPos[0], PlayerPos[1])

#Make the screen display
def Display(fps):
    pygame.display.update()
    pygame.time.delay(1000/fps)

#Move Position by a certain Speed with a CD
def Move(Pos,Speed,MoveCD):
        Pos += Speed
        pygame.time.delay(MoveCD)
        return Pos

def Background(sprite,spriteRect):
    for x in range(0,WindowSize[0]/32):
        for y in range(0,WindowSize[1]/32):
            spriteRect.top = y*32
            screen.blit(sprite,spriteRect)
        spriteRect.left = x*32
        screen.blit(sprite,spriteRect)

def Layer(sprite,spriteRect,blueprint,char):
    xL = 0
    yL = 0
    for i in blueprint:
        for j in i:
            if xL == WindowSize[0]:
                xL = 0
                yL += 32
            if j == char:
                spriteRect.left = xL
                spriteRect.top = yL
                screen.blit(sprite,spriteRect)
            xL += 32

#Import Sprites
Simon, SimonRect = Spritesheet('images/sprites.png',4,2,32,32)
Wall, WallRect = Spritesheet('images/sprites.png',39,17,32,32)
Ground, GroundRect = Spritesheet('images/sprites.png',41,12,32,32) 

Level1 = [
"WWWWWWWWWWWWWWWWWWWW"
"W......W..W..W.....W"
"W...WWWW...........W"
"W...W..............W"
"W...W..............W"
"W...W..............W"
"W...W..............W"
"W..................W"
"WWWWW..............W"
"W..................W"
"W..................W"
"W..................W"
"W..................W"
"W..................W"
"W..................W"
"W..................W"
"W..................W"
"W..................W"
"W..................W"
"W..................W"
"WWWWWWWWWWWWWWWWWWWW"
]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    #Player Mouvement
    GameKey = pygame.key.get_pressed()
    
    if GameKey[pygame.K_DOWN]:
        PlayerPos[1] = Move(PlayerPos[1], PlayerSpeed, MoveCD)
    if GameKey[pygame.K_UP]:
        PlayerPos[1] = Move(PlayerPos[1], -PlayerSpeed, MoveCD)
    if GameKey[pygame.K_RIGHT]:
        PlayerPos[0] = Move(PlayerPos[0], PlayerSpeed, MoveCD)
    if GameKey[pygame.K_LEFT]:
        PlayerPos[0] = Move(PlayerPos[0], -PlayerSpeed, MoveCD)

    #World Boundaries Check
    while (PlayerPos[0] > WindowSize[0] - 32):
        PlayerPos[0] -= PlayerSpeed
    while (PlayerPos[0] < 0):
        PlayerPos[0] += PlayerSpeed
    while (PlayerPos[1] > WindowSize[1] - 32):
        PlayerPos[1] -= PlayerSpeed
    while (PlayerPos[1] < 0):
        PlayerPos[1] += PlayerSpeed
    
    Background(Ground,GroundRect)
    Layer(Wall,WallRect, Level1,"W")
    Player(Simon, SimonRect, PlayerPos[0], PlayerPos[1])
    Display(60)
