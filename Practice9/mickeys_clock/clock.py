import pygame
def rotate_hands(surface,angle,center):
    rotated_surface = pygame.transer.rotate(surface,-angle)
    new_rect = rotated_surface.get_rect(center=center)
    return rotated_surface,new_rect
