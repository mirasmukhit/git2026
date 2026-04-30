import pygame
pygame.init()
WIDTH,HEIGHT = 800,900
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Snake")
done = False
while not done:
    for event in pygame.event.get():
        print(event.type)
        if event.type == pygame.QUIT:
            done = True

pygame.quit()
