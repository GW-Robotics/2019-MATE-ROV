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
    # 0: A
    # 1: B
    # 2: X
    # 3: Y
    # 4: L1
    # 5: R1
    # 6: BACK
    # 7: START
    # 8: L3
    # 9: R3
    for i in range(buttons):
        button = joystick.get_button(i)
        curr_vals.append(button)
        
    hats = joystick.get_numhats()
    # Value comes back in a tuple (x, y) from with values -1, 0, or 1
    # x: L/R
    # y: D/U
    for i in range(hats):
        hat = joystick.get_hat(i)
        curr_vals.append(hat[0])
        curr_vals.append(hat[1])

    return curr_vals

# Main loop
button_vals = [0]*16
the_joystick = pygame.joystick.Joystick(0)
the_joystick.init()
# while True:
for i in range(10000):
    
    # EVENT PROCESSING STEP
    for event in pygame.event.get(): # User did something
        if event.type in input_type: #if event was an input
            print("input!!!11!")
    
    print(query_values(the_joystick))

# End pygame
pygame.quit ()