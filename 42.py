""" La side scrolla: Foundation is intended to be a form of sidescroller or platformer
that has the player jumping from platform to platform
This is still the early stage therefore this is known as:
Foundation: 28
Basic gameplay as of now involves: pressing the screen to move
Having a butchered sprite of ya boi polygon
Having a scoreboard list of the highest scores
Having a very disabled platform
Music from Destiny 2, 'Green Room' from the mission commonly refered to as the 'Whisper of the Worm mission' (all rights belong with Bungie and their studios)
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

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

P.init()  # starts the game engine
clock = P.time.Clock()  # creates clock to limit frames per second
loopRate = 50  # sets max speed of main loop
SCREENSIZE = SCREENWIDTH, SCREENHEIGHT = 900, 550  # sets size of screen/window
Screen = P.display.set_mode(SCREENSIZE)  # creates window and game screen
Touch = P.MOUSEBUTTONDOWN #touching screen
P_Array = P.sprite.Group() #creating an empty array for the number count of the platforms
#Pl_Array = []
#music set up, since the chosen song has different phases, it would make it interesting for the player
color_array = [RED, BLUE, YELLOW, GREEN]
for c in color_array:
    P_Array.add(Block(Screen, c))
    
block_rate = 3000  # time in millisecs between adding platforms
block_last_added = 0 #last time a platforms was added to the P_array
P.display.set_caption('42 Jump!')
P.mixer.music.load('media/Whisper.mp3') #All rights and credit to Destiny 2 and its creators over at Bungie
P.mixer.music.play(+100) #this is to allow the music to play throughout the entirety of te game until closed
#setting up the score counter
Score = 0
leader_board = LeaderBoard()
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
    

#create my boi
Sprite_Polygon = Polygon(Screen)

intro = Intro(Screen)

play = True  # controls whether to keep playing
End_G = False #controlling the game over screen
score_checked = False
Helping = True

# game loop - runs loopRate times a second!
while play:  # game loop - note:  everything in this loop is indented one tab

    
    now = P.time.get_ticks() #time of program in mil-sec
    
    for event in P.event.get():  # get user interaction events
        if event.type == P.QUIT:  # tests if window's X (close) has been clicked
            play = False  # causes exit of game loop
       
        # your code starts here ######
        #if event.type == Touch:
            #Helping = False
            
        if event.type == Touch:
            #Sprite_Polygon.Jump() #testing the feature to click to jump
            if Helping:
                Helping = False
            else:
                Sprite_Polygon.moveTowards(event.pos)
                Sprite_Polygon.landed = False

        
    if Helping:
        intro.show()
        
    elif End_G:      
        y_offset = -350
        font_over = P.font.Font(None,60)
        score_x,score_y = font_over.size("Your score: {}".format(Score))        
        score_text = font_over.render("Your score: {}".format(Score),1,RED, BLUE)
        Screen.blit(score_text,[(SCREENWIDTH - score_x)/2, y_offset+(SCREENHEIGHT - score_y)/2])
    
        if not score_checked:
            if leader_board.check(Score) == True:
                print("We have a new high score bois!")
                leader_board.update(Score)
            score_checked = True
    
        font_over = P.font.Font(None,40)
        y_offset += 100
        for l in leader_board.leaders:
            score_x,score_y = font_over.size("{}   {}".format(l[1], l[0]))        
            score_text = font_over.render("{}   {}".format(l[1], l[0]),1,RED, BLUE)
            Screen.blit(score_text,[(SCREENWIDTH - score_x)/2, y_offset+(SCREENHEIGHT - score_y)/2])
            y_offset += 50
        
        final_screen = True
    
    else:
        Screen.fill(BLACK)
        #Platform().R_A_Random(Screen)        
        Sprite_Polygon.show()
        Sprite_Polygon.Gravity()
        if not Screen.get_rect().contains(Sprite_Polygon.rect): #if he hits the boarders of the screen it ends
            End_G = True
        for platform in P_Array:
            platform.move()
            platform.show()
            
            #check to see if it is off the screen
            if platform.rect.x < -platform.rect.width:
                P_Array.remove(platform)
                

        #see if it is time to add a platform
        if (now - block_last_added > block_rate): #time to add a platform
            P_Array.add(Block(Screen,R.choice(color_array)))
            block_last_added = now
            block_rate -= 3
            print("{} platforms in play".format(len(P_Array)))
            
       
        #to see if ya boi hits/lands on the platforms
        collide_platforms = P.sprite.spritecollide(Sprite_Polygon, P_Array, False)
        
        for p in collide_platforms:
            sr = Sprite_Polygon.rect
            pr = p.rect
            bleed = 6
            #print("{} {} {} {}".format(sr.top, sr.bottom, sr.left, sr.right))
            #print("{} {} {} {}".format(pr.top, pr.bottom, pr.left, pr.right))
                  
            
            # is ya boi above the platform
            if sr.bottom <= pr.top + bleed: # remember we count from the top of the screen
                #print('above')
                Sprite_Polygon.vx = p.vx
                if Sprite_Polygon.landed == False:
                    Sprite_Polygon.landed = True
                    Score += 1
                #Score += 1 #debug statemnt to find old high score
            elif sr.top >= pr.bottom - bleed: #check to see if underneath
                sr = sr.move(0,bleed) #remove any overlap
                Sprite_Polygon.vy += Sprite_Polygon.vy #ya boi bounces down
            elif sr.right <= pr.left + bleed: #check to see if on the left
                sr = sr.move(-bleed,0) #remove any overlap
                Sprite_Polygon.vx = -Sprite_Polygon.vx - p.vx #ya boi bounces left
                
            elif sr.left >= pr.left - bleed: #check to see if on the right:
                sr = sr.move(bleed,0) #remove any overlap
                Sprite_Polygon.vx = -Sprite_Polygon.vx + p.vx #ya boi bounces right
            else:
                print("who knows")
                               
        
    # your code ends here #######
    P.display.flip()  # makes any changes visible on the screen
    clock.tick(loopRate)  # limits game to frame per second, FPS value

# out of game loop #
print(Score)
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