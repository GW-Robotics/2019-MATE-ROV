import pygame

pygame.init()

#Loop until the user clicks the close button.
done = False

#Initialize joysticks
pygame.joystick.init()

#Main loop
while not done:
    
    # EVENT PROCESSING STEP
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop

    # Get count of joysticks
    joystick_count = pygame.joystick.get_count()
    print("Joysticks: "+str(joystick_count))
    
    # For each joystick:
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
        
        # Usually axis run in pairs, up/down for one, and left/right for
        # the other.
        axes = joystick.get_numaxes()
        print("Number of axes: {}".format(axes))
        
        for i in range(axes):
            axis = joystick.get_axis( i )
            print("Axis {} value: {:>6.3f}".format(i, axis) )
         
            
        buttons = joystick.get_numbuttons()
        print("Number of buttons: {}".format(buttons) )
         

        for i in range( buttons ):
            button = joystick.get_button( i )
            print("Button {:>2} value: {}".format(i,button) )
         
            
        # Hat switch. All or nothing for direction, not like joysticks.
        # Value comes back in an array.
        hats = joystick.get_numhats()
        print("Number of hats: {}".format(hats) )
         

        for i in range( hats ):
            hat = joystick.get_hat( i )
            print("Hat {} value: {}".format(i, str(hat)) )


    
# Close the window and quit.
# If you forget this line, the program will 'hang'
# on exit if running from IDLE.
pygame.quit ()