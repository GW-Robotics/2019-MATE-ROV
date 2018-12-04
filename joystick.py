import pygame


def init_joystick():

    # Initialize pygame
    pygame.init()

    #Initialize joysticks
    pygame.joystick.init()

    # Acceptable events to query the controller
    input_type = [pygame.JOYAXISMOTION, pygame.JOYBALLMOTION, pygame.JOYBUTTONDOWN, pygame.JOYBUTTONUP, pygame.JOYHATMOTION]

    the_joystick = pygame.joystick.Joystick(0)
    the_joystick.init()

    return the_joystick, input_type


def query_values(joystick):

    curr_vals = []

    axes = joystick.get_numaxes()
    # Values go from -1 to 1
    # 0: LStick L/R
    # 1: LStcik U/D
    # 2: R2/L2
    # 3: RStick U/D
    # 4: RStick L/R
    for i in range(axes):
        axis = joystick.get_axis(i)
        curr_vals.append(axis)
        
    buttons = joystick.get_numbuttons()
    # Values are 0 or 1
    # 5: A
    # 6: B
    # 7: X
    # 8: Y
    # 9: L1
    # 10: R1
    # 11: BACK
    # 12: START
    # 13: L3
    # 14: R3
    for i in range(buttons):
        button = joystick.get_button(i)
        curr_vals.append(button)
        
    hats = joystick.get_numhats()
    # Value comes back in a tuple (x, y) from with values -1, 0, or 1
    # 15: L/R
    # 16: D/U
    for i in range(hats):
        hat = joystick.get_hat(i)
        curr_vals.append(hat[0])
        curr_vals.append(hat[1])

    return curr_vals

# Main loop
the_joystick, input_type = init_joystick()

for i in range(10000):
    
    # EVENT PROCESSING STEP
    for event in pygame.event.get(): # User did something
        if event.type in input_type: #if event was an input
            print("input!!!11!")
    
    print(query_values(the_joystick))

# End pygame
pygame.quit ()