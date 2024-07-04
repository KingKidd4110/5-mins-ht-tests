import pygame

pygame.init()

screen = pygame.display.set_mode((500, 400))

while True:
    for ev in pygame.event.get():
        if ev.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            col = (0, 255, 255)
            pygame.draw.circle(screen, col, pos, 50)
            pygame.display.update()
