import pygame

def check_events(player) -> dict[str, bool]:
    # check to see if any events occured since the last time through the game loop
    
    event_data = {"game_on" : True}
    for event in pygame.event.get():
    
        # Check to see what event it was
        if event.type == pygame.QUIT:
            event_data["game_on"] = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                # the user pressed the down arrow
                print("Down")
                player.y += 20
             
            elif event.key == pygame.K_UP:
                # the user pressed the up arrow
                print("Up")
                player.y -= 20
              
            elif event.key == pygame.K_RIGHT:
                # the user pressed the right arrow
                print("Right")
                player.x += 20
             
            elif event.key == pygame.K_LEFT:
                # the user pressed the left arrow
                player.x -= 20
    return event_data
