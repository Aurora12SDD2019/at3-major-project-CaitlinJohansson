""" La side scrolla: Foundation is intended to be a form of sidescroller or platformer
that has the player jumping from platform to platform
This is still the early stage therefore this is known as:
Foundation: 14
Basic gameplay as of now involves: pressing the screen to move
Having a butchered sprite of ya boi polygon
Having a scoreboard of the current highest score and your score, no more
Having a very disabled platform
Music from Destiny 2, 'Zero Hour' (all rights belong with Bungie and their studios)
Featuring:
Ya Boi Polygon (butchered edition)
The Void (background)
And The Stillness of No Colour (featured as the platforms)
"""

__author__ = "Caitlin.Johansson"
__license__ = "GPL"
__version__ = "1.0.1"
__email__ = "Caitlin.Johansson@education.nsw.com.au"
__status__ = "Alpha"

#dependencies
import pygame as P # accesses pygame files
import sys  # to communicate with windows
import random as R #access for random probabilities
from mods import *


# pygame setup - only runs once
P.init()  # starts the game engine
clock = P.time.Clock()  # creates clock to limit frames per second
loopRate = 50  # sets max speed of main loop
SCREENSIZE = SCREENWIDTH, SCREENHEIGHT = 900, 550  # sets size of screen/window
Screen = P.display.set_mode(SCREENSIZE)  # creates window and game screen
Touch = P.MOUSEBUTTONDOWN #touching screen
P_Array = [] #creating an empty array for the number count of the platforms
#music set up, since the chosen song has different phases, it would make it interesting for the player
P.display.set_caption('42 Jump!')
P.mixer.music.load('media/Whisper.mp3') #All rights and credit to Destiny 2 and its creators over at Bungie
P.mixer.music.play(-1) #this is to allow the music to play throughout the entirety of te game until closed
#setting up the score counter
Score = 0
#open and read the high scores to store high score values
H_S_File = open('media\H_Score.txt', 'r')
H_Score = H_S_File.read() #read it
H_S_File.close() #close it
#make string value ints
#need to ensure the file isn't empty
try:
    H_Score = int(H_Score)
except ValueError: #if empty then there would be an error
    H_Score = 0
    
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
End_G = False #controlling the game over screen

# game loop - runs loopRate times a second!
while play:  # game loop - note:  everything in this loop is indented one tab
    now = P.time.get_ticks() #time of program in mil-sec
    
    for event in P.event.get():  # get user interaction events
        if event.type == P.QUIT:  # tests if window's X (close) has been clicked
            play = False  # causes exit of game loop
       
        # your code starts here ######
        if event.type == Touch:
            #Sprite_Polygon.Jump() #testing the feature to click to jump
            Sprite_Polygon.moveTowards(event.pos)
            Score += 1 #debug statemnt to find old high score
            
        Screen.fill(GREEN)
        Platform().R_A_Random()
        Sprite_Polygon.show()
        
        
            
        if End_G:
           Text_End = P.font.Font(None,66)
           Score_Size_X, Score_Size_Y = Text_End.size("Your Score: {}".format(Score))
           Score_Text = Text_End.render("Your Score: {}".format(Score),1, BLUE, WHITE)
           Screen.blit(Score_Text, [(SCREENWIDTH - Score_Size_X)/2, -100+(SCREENHEIGHT - Score_Size_Y)/2])
           H_Score_X,H_Score_Y = Text_End.size("The current high score: {}".format(H_Score))        
           Score_Text = Text_End.render("The current high score: {}".format(H_Score),1,BLUE, WHITE)
           Screen.blit(Score_Text,[(SCREENWIDTH - H_Score_X)/2, (SCREENHEIGHT - H_Score_Y)/2])
        else:
            Sprite_Polygon.Gravity()
            if not Screen.get_rect().contains(Sprite_Polygon.rectangle): #if he hits the boarders of the screen it ends
                End_G = True
            for platform in P_Array:
                platform.show()
                #to see if ya boi hits/lands on the platforms
                if (platform.colliderect(Sprite_Polygon.rectangle) and Sprite_Polygon.downwards):
                    Sprite_Polygon.vx = Platform.vx
                    Sprite_Polygon.landed = True           

            
    # your code ends here #######
    P.display.flip()  # makes any changes visible on the screen
    clock.tick(loopRate)  # limits game to frame per second, FPS value

# out of game loop #
if Score > H_Score:
    H_Score = Score
    H_Score = open('media\H_Score.txt', 'w')
    H_Score.write("{}".format(H_Score))
    H_Score.close()
    print("You have a new high score!")
print("Thanks for playing")  # notifies user the game has ended
print("The current high score is {}".format(H_Score))
print("You crossed {} platform(s).".format(Score))
"""Debug statement"""
P.quit()   # stops the game engine
sys.exit()  # close operating system window