import pygame
from Board import Number

def map_click(x, y):
    if 272 <= x <= 336:
        if 272 <= y <= 336:
            return 1
        elif 337 <= y <= 401:
            return 5
        elif 402 <= y <= 466:
            return 9
        elif 467 <= y <= 528:
            return 13
    elif 337 <= x <= 401:
        if 272 <= y <= 336:
            return 2
        elif 337 <= y <= 401:
            return 6
        elif 402 <= y <= 466:
            return 10
        elif 467 <= y <= 528:
            return 14
    elif 402 <= x <= 466:
        if 272 <= y <= 336:
            return 3
        elif 337 <= y <= 401:
            return 7
        elif 402 <= y <= 466:
            return 11
        elif 467 <= y <= 528:
            return 15
    elif 467 <= x <= 528:
        if 272 <= y <= 336:
            return 4
        elif 337 <= y <= 401:
            return 8
        elif 402 <= y <= 466:
            return 12
        elif 467 <= y <= 528:
            return 16

pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("img/numpuzCopia")
icon = pygame.image.load("img/fondo.png")

pygame.display.set_icon(icon)
running = True
quadrant = {1: (272, 272), 2: (337,272), 3: (402, 272), 4: (467, 272),
            5: (272,337), 6: (337,337), 7: (402,337), 8: (467,337),
            9: (272, 402), 10: (337, 402), 11: (402, 402), 12: (467, 402),
            13: (272, 467), 14: (337, 467), 15: (402, 467), 16: (467, 467)}
numbers = [Number(pygame.image.load(f"img/number-{i}.png"), i) for i in range(1,17)]

screen.fill((98, 114, 164))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            section = map_click(x,y)

    for number in numbers:
        screen.blit(number.value, quadrant[number.quadrant])
#    screen.blit(numbers[0].value, quadrant[numbers[0].quadrant])

    pygame.display.update()
