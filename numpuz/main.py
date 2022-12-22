import pygame
from Board import Number

def map_click(x, y):
    pass
    



pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("img/numpuzCopia")
icon = pygame.image.load("img/fondo.png")

pygame.display.set_icon(icon)
running = True
quadrant = {1: (272, 272), 2: (336,272), 3: (400, 272), 4: (464, 272), 
            5: (272,336), 6: (336,336), 7: (400,336), 8: (464,336),
            9: (272, 400), 10: (336, 400), 11: (400, 400), 12: (464, 400),
            13: (272, 464), 14: (336, 464), 15: (400, 464), 16: (464, 464)}
numbers = [Number(pygame.image.load(f"img/number-{i}.png"), i) for i in range(1,17)]


screen.fill((202,229,186))

for number in numbers:
    screen.blit(number.value, quadrant[number.quadrant])

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if numbers[2].value.get_rect().collidepoint(x,y):
                quadrant = 2
                print(quadrant)
           
           
    
    pygame.display.update()







