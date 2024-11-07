import pygame

pygame.init()


class Game:
    back_ground_color = (0, 0, 255)

    start_screen = pygame.display.set_mode((900, 700))

    start_screen.fill(back_ground_color)
    pygame.display.flip()
    mijn = True
    while mijn:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                print()
                mijn = False
