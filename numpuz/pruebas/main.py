import pygame
 
pygame.init()
width=350
height=400
screen = pygame.display.set_mode( (width, height ) )
pygame.display.set_caption('clicked on image')
redSquare = pygame.image.load("number-2.png")
redSquar = pygame.image.load("number-1.png")
 
x = 20; # x coordnate of image
y = 30; # y coordinate of image
 
running = True
while (running):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Set the x, y postions of the mouse click
            xc, yc = event.pos
            if xc >= x and xc <= x+64 and yc >= y and yc <= y+64:
                x += 10
                screen.blit(redSquare,(x,y))
                print(2)
            elif xc >= 100 and xc <= 164 and yc >= 100 and yc <= 164:
                print(1)
    screen.blit(redSquare ,  ( x,y)) # paint to screen
    screen.blit(redSquar , ( 100,100)) # paint to screen
    pygame.display.update()
#loop over, quite pygame

pygame.quit()