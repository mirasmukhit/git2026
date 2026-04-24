while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    now = datetime.datetime.now()
    seconds = now.second
    minutes = now.minute

    minute_angle = minutes*6
    second_angle = seconds*6

    screen.blit(bg,(0,0))

    min_surf , min_rect = rotate_hands(right_hand_img,minute_angle,center_pos)
    screen.blit(min_surf,min_rect)
    sec_surf,sec_rect = rotate_hands(left_hand_img,second_angle,center_pos)
    screen.blit(sec_surf,sec_rect)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()