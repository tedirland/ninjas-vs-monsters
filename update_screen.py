
### This function is responsible for updating the screen


def update_screen(screen, player, background):
    '''This function updates objects on the screen'''
    
    background.draw_bg(screen)
    player.move_player(screen)
    