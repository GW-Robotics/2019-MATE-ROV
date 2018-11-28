import pygame

pygame.init()

#Initialize joysticks
pygame.joystick.init()

button_vals = [0]*16

input_type = [pygame.JOYAXISMOTION, pygame.JOYBALLMOTION, pygame.JOYBUTTONDOWN, pygame.JOYBUTTONUP, pygame.JOYHATMOTION]

# Get count of joysticks
joystick_count = pygame.joystick.get_count()

#Main loop
for hello in range(10000):

    # For each joystick:
    for i in range(joystick_count):
        curr_joystick = pygame.joystick.Joystick(i)
        curr_joystick.init()
        query_values(curr_joystick)
    
    # EVENT PROCESSING STEP
    for event in pygame.event.get(): # User did something
        if event.type in input_type: #if event was an input
            print("input lol")

def query_values(joystick):    
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