import pygame, sys
from pygame.locals import *

#Variables
PlayerPos = [64,64]
WindowSize = [320,320]
BackgroundSize = [640, 640]
CameraPos = [0,0]
PlayerSpeed = 32 #Player Speed in pixel per fps
MoveCD = 100 #Cooldown before the Player is able to move again in millisecond
PlayerRotation = 0
Rot = 0

#Init game and screen (window)
pygame.init()
screen = pygame.display.set_mode(WindowSize)

#Sprite Sheet function
def Spritesheet(file,i,j,x=32,y=32):
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
    screen.blit(sprite ,(posX - CameraPos[0], posY - CameraPos[1]))
    #print 'posXY: {} {}'.format(posX, posY)
    #print 'playerpos: {} {}'.format(PlayerPos[0], PlayerPos[1])

#Make the screen display
def Display(fps=60):
    pygame.display.update()
    pygame.time.delay(1000/fps)

#Move Position by a certain Speed with a CD
def Move(Pos, Speed, MoveCD=MoveCD):
        Pos += Speed
        pygame.time.delay(MoveCD)
        return Pos

#Push the player back in the opposite direction of the key pressed. e.g: Player press down and get pushed upward.
def WallCollision():
    if GameKey[pygame.K_DOWN]:
        PlayerPos[1] -= PlayerSpeed
    if GameKey[pygame.K_UP]:
        PlayerPos[1] += PlayerSpeed
    if GameKey[pygame.K_RIGHT]:
        PlayerPos[0] -= PlayerSpeed
    if GameKey[pygame.K_LEFT]:
        PlayerPos[0] += PlayerSpeed

#Create a Background that fills the Room
def Background(sprite,spriteRect):
    for x in range(0,BackgroundSize[0]/32):
        for y in range(0,BackgroundSize[1]/32):
            spriteRect.top = y*32
            screen.blit(sprite,(x*32 - CameraPos[0], y*32 - CameraPos[1]))
        spriteRect.left = x*32
        screen.blit(sprite,(x*32 - CameraPos[0], y*32 - CameraPos[1]))

#Create a layer from the blueprint, can give col argument a non-"yes" value to ignore collsions, can give toCall a non-"WallCollision" value to call an other function
def Layer(sprite,spriteRect,blueprint,char,col='yes',toCall=WallCollision):
    xL = 0
    yL = 0
    for i in blueprint:
        for j in i:
            #End of the Row : set xL back to 0
            if xL == BackgroundSize[0]:
                xL = 0
                yL += 32
            
            if j == char:
                spriteRect.left = xL
                spriteRect.top = yL
                
                if (col == 'yes') & (PlayerPos[0] == xL) & (PlayerPos[1]  == yL):
                    toCall()

                screen.blit(sprite,(xL - CameraPos[0], yL - CameraPos[1]))
            xL += 32

def Rotation(WantedDeg,RotationValue):
    if RotationValue != WantedDeg:
        RotAdd = WantedDeg - RotationValue
        if RotationValue < WantedDeg:
            return RotAdd
        else:
            return -RotAdd

#Import Sprites
Simon, SimonRect = Spritesheet('images/hero.png',0,0)
Wall, WallRect = Spritesheet('images/sprites.png',39,17)
Ground, GroundRect = Spritesheet('images/sprites.png',41,12) 

#The Level 1 Map blueprint: W = Wall, . = nothing
#The Array must be of BackgroundSize[0]/32 x BackgroundSize[1]/32, here: 20x20
Level1 = [
"WWWWWWWWWWWWWWWWWWWW"
"W.....WW...........W"
"W....WW............W"
"W...WW...WWWW......W"
"W...W.......WW.....W"
"W...W........W.....W"
"W...WWWWWW...W.....W"
"W...........WW.....W"
"WWWW......WWW......W"
"W..WWWWWWWW........W"
"W..................W"
"W..................W"
"W...WWWWWWWWWWWWWWWW"
"W..................W"
"W..................W"
"W..................W"
"WWWWWWWWWWWWW......W"
"W..................W"
"W..................W"
"WWWWWWWWWWWWWWWWWWWW"
]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    #Player Mouvement and sprite rotation
    GameKey = pygame.key.get_pressed()
    
    #if rot == 360:
    #    rot = 0

    if GameKey[pygame.K_DOWN]:
        PlayerPos[1] = Move(PlayerPos[1], PlayerSpeed)
        if PlayerRotation != 180:
            Simon = pygame.transform.rotate(Simon, Rotation(180, PlayerRotation))
            PlayerRotation = 180
    
    if GameKey[pygame.K_UP]:
        PlayerPos[1] = Move(PlayerPos[1], -PlayerSpeed)
        if PlayerRotation != 0:
            Simon = pygame.transform.rotate(Simon, Rotation(0, PlayerRotation))
            PlayerRotation = 0

    if GameKey[pygame.K_RIGHT]:
        PlayerPos[0] = Move(PlayerPos[0], PlayerSpeed)
        if PlayerRotation != 90:
            Simon = pygame.transform.rotate(Simon, Rotation(90, PlayerRotation))
            PlayerRotation = 90

    if GameKey[pygame.K_LEFT]:
        PlayerPos[0] = Move(PlayerPos[0], -PlayerSpeed)
        if PlayerRotation != 270:
            Simon = pygame.transform.rotate(Simon, Rotation(270, PlayerRotation))
            PlayerRotation = 270

    #print "After Mouvement", PlayerRotation  

    CameraPos[0] = PlayerPos[0] - 128
    CameraPos[1] = PlayerPos[1] - 128
    
    """ #Manual Camera Mouvements
    if GameKey[pygame.K_s]:
        CameraPos[1] = Move(CameraY, PlayerSpeed)
    if GameKey[pygame.K_z]:
        CameraPos[1] = Move(CameraY, -PlayerSpeed)
    if GameKey[pygame.K_d]:
        CameraPos[0] = Move(CameraX, PlayerSpeed)
    if GameKey[pygame.K_q]:
        CameraPos[0] = Move(CameraX, -PlayerSpeed)
    """
    
    #World Boundaries Check
    while (PlayerPos[0] > BackgroundSize[0] - 32):
        PlayerPos[0] -= PlayerSpeed
    while (PlayerPos[0] < 0):
        PlayerPos[0] += PlayerSpeed
    while (PlayerPos[1] > BackgroundSize[1] - 32):
        PlayerPos[1] -= PlayerSpeed
    while (PlayerPos[1] < 0):
        PlayerPos[1] += PlayerSpeed
   
    # print "DEBUG"
    screen.fill(0x000000)
    Background(Ground,GroundRect)
    Layer(Wall,WallRect, Level1, "W")
    Player(Simon, SimonRect, PlayerPos[0], PlayerPos[1])
    Display()
