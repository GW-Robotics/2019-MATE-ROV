import pygame

# Initialize pygame
pygame.init()

#Initialize joysticks
pygame.joystick.init()

# Acceptable events to query the controller
input_type = [pygame.JOYAXISMOTION, pygame.JOYBALLMOTION, pygame.JOYBUTTONDOWN, pygame.JOYBUTTONUP, pygame.JOYHATMOTION]

# Get count of joysticks
joystick_count = pygame.joystick.get_count()

# Alert user if more than 1
if(joystick_count > 1):
    print("More than 1 joystick found.")

def query_values(joystick):    
    # Usually axis run in pairs, up/down for one, and left/right for
    # the other.
    axes = joystick.get_numaxes()
    print("Number of axes: " + str(axes))
    
    for i in range(axes):
        axis = joystick.get_axis(i)
        print("Axis "+str(i)+" value: "+str(axis))
        
        
    # buttons = joystick.get_numbuttons()
    # print("Number of buttons: {}".format(buttons) )
        

    # for i in range( buttons ):
    #     button = joystick.get_button( i )
    #     print("Button {:>2} value: {}".format(i,button) )
        
        
    # # Hat switch. All or nothing for direction, not like joysticks.
    # # Value comes back in an array.
    # hats = joystick.get_numhats()
    # print("Number of hats: {}".format(hats) )
        

    # for i in range( hats ):
    #     hat = joystick.get_hat( i )
    #     print("Hat {} value: {}".format(i, str(hat)) )

# Main loop
button_vals = [0]*16
for i in range(10000):

    the_joystick = pygame.joystick.Joystick(0)
    the_joystick.init()
    query_values(the_joystick)
    
    # EVENT PROCESSING STEP
    for event in pygame.event.get(): # User did something
        if event.type in input_type: #if event was an input
            print("input lol")

# End pygame
pygame.quit ()