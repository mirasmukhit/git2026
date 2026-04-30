import pygame
pygame.init()
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("MOVENET OF CIRCLE")
COLOR_RED = (255,0,0)
COLOR_BLUE = (0,0,255)
done = False
is_red = True
is_pressed = False
is_up = False
is_down = False
is_left = False
is_right = False
circle_x = 100
circle_y = 100
clock = pygame.time.Clock()
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            is_pressed = True
            if event.key == pygame.K_SPACE:
                is_red = not is_red
            if event.key == pygame.K_UP:
                is_up = True
            if event.key == pygame.K_DOWN:
                is_down = True
            if event.key == pygame.K_LEFT:
                is_left = True
            if event.key == pygame.K_RIGHT:
                is_right = True
        if event.type == pygame.KEYUP:
            is_pressed = False
            is_up = is_down = is_right = is_left = False
    if is_pressed:
        if is_up:
            circle_y -= 1
        if is_down:
            circle_y += 1
        if is_left:
            circle_x -= 1
        if is_right:
            circle_x += 1
    if is_red:
        screen.fill(COLOR_RED)
        pygame.draw.circle(screen,COLOR_BLUE,(circle_x,circle_y),40,4)
    else:
        screen.fill(COLOR_BLUE)
        pygame.draw.circle(screen,COLOR_RED,(circle_x,circle_y),40,4)
    pygame.display.flip()
    clock.tick(120)
pygame.quit()
