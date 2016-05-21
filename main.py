import sys, pygame, time
pygame.init()

size = width, height = 1920, 1080
speed = [2,2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)
char = pygame.image.load("char.bmp")
charRect = char.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    charRect = charRect.move(speed)
    if charRect.left < 0 or charRect.right > width:
        speed[0] = -speed[0]
    if charRect.top < 0 or charRect.bottom > height:
        speed[1] = -speed[1]

    #time.sleep(0.00000001)
    screen.fill(black)
    screen.blit(char, charRect)
    pygame.display.flip()
 
