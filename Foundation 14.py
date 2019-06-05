""" La side scrolla """

__author__ = "Caitlin.Johansson"
__license__ = "GPL"
__version__ = "1.0.1"
__email__ = "Caitlin.Johansson@education.nsw.com.au"
__status__ = "Alpha"

#dependencies
import pygame as P # accesses pygame files
import sys  # to communicate with windows
from mods import *


# pygame setup - only runs once
P.init()  # starts the game engine
clock = P.time.Clock()  # creates clock to limit frames per second
loopRate = 60  # sets max speed of main loop
SCREENSIZE = SCREENWIDTH, SCREENHEIGHT = 800, 600  # sets size of screen/window
Screen = P.display.set_mode(SCREENSIZE)  # creates window and game screen
Vec = P.math.Vector2
Grav = Vec(0, 0.3)
Touch = P.MOUSEBUTTONDOWN #touching screen

M_Count = 0
#fileIn = open('media\H_Score.txt', 'r')
#High_S = fileIn.readlines()
#fileIn.close()
"""try:
    fileIn = int(High_S)
except ValueError:
    
"""

#Highest_S = max(High_S)


# set variables for some colours if you wnat them RGB (0-255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#create my boi
Sprite_Polygon = Polygon(Screen)

play = True  # controls whether to keep playing

# game loop - runs loopRate times a second!
while play:  # game loop - note:  everything in this loop is indented one tab

    for event in P.event.get():  # get user interaction events
        if event.type == P.QUIT:  # tests if window's X (close) has been clicked
            play = False  # causes exit of game loop
        
        # your code starts here ######
        if event.type == Touch:
            print('Ow! That hurt!')
            Sprite_Polygon.moveTowards(event.pos)
            M_Count += 1
        

    Screen.fill(RED)
    Sprite_Polygon.show()
    # your code ends here #######
    P.display.flip()  # makes any changes visible on the screen
    clock.tick(loopRate)  # limits game to frame per second, FPS value

# out of game loop #
print("Thanks for playing")  # notifies user the game has ended
print("You pressed the screen {} times".format(M_Count))
"""Debug statement"""
#if M_Count > int(Highest_S):
H_Score = open('media\H_Score.txt', 'w')
H_Score.write(str(M_Count))
H_Score.close()
P.quit()   # stops the game engine
sys.exit()  # close operating system window