import pygame
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("My first game")
colour_red = ((255,0,0))
colour_blue = ((0,0,255))
running = True
is_red = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                is_red = not is_red
    if is_red:
        screen.fill((colour_red))
        pygame.draw.circle(screen,((255,255,255)),(100,100),40)
    else:
        screen.fill((colour_blue))
        pygame.draw.circle(screen,((255,255,0)),(400,300),40)
    
    pygame.display.flip()
pygame.quit()