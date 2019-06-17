""" La mods"""

__author__ = "Caitlin.Johansson"
__license__ = "GPL"
__version__ = "1.0.1"
__email__ = "Caitlin.Johansson@education.nsw.com.au"
__status__ = "Alpha"


""" revision notes:


"""

#import statements for any dependencies
import pygame as P
import random as R

#modules - write your modules here using the templates below
class Polygon(object):
    """Summary of polygon, my boi: the sprite

    Attributes:
        image: who dat boi is
        location: where dat boi is (coodinates, window)
        
        self.window = window
        self.position = where the sprite of my boi will be
        self.image = loading up my boi polygon
        self.x = where my boi is on the x axis
        self.y = where my boi is on the y axis
        self.rectangle = makes my boi have a rectangular hitbox
        self.vx = the velocity of which my boi can go on the x axis
        self.vy = the velocity of which my boi can go on the y axis
        self.a = acceleration or gravity if you will
        self.landed = identifying whether or not my boi is on something
        self.downwards = identifying whether or not my boi is going down
        temp_center = aquiring the temperary value of the center of my boi
    """

    def __init__(self, window):
        """Inits my boi polygon image n location.
        Establishes the: window
        OG spawning position
        Spawning the image of ya boi
        Create a base velocity speed if moved
        Makes dat boi's shape a rectangle for the ez hitbox
        Allows program to acknowledge if dat boi is/isnt on the ground
        Allows program to acknowledge if dat boi is/isnt falling to death
        """
        self.change_x = 0
        self.change_y = 0
        self.window = window
        self.position = [100, 100]
        self.image = P.image.load('media/YA BOI POLYGON Perfected.png').convert()
        self.x = 100 
        self.y = 100
        self.vx = 1 
        self.vy = 1
        self.rectangle = self.image.get_rect()
        self.landed = False
        self.downwards = True
        
    def show(self):
        """Shows my boi by allowing him to exist on screen"""
        self.window.blit(self.image, self.rectangle)
        
    def moveTowards(self, position):
        """Makes my boi move to where you press
        while having a stable orbit to not be flung out of existance
        """
        self.landed = False
        mouse_x = position[0]
        mouse_y = position[1]
        self.vx = (mouse_x - self.rectangle.centerx)/33
        self.vy = (mouse_y - self.rectangle.centery)/33
        
    """
    An attempt to try another way on getting the collision effects to work
    over-complicated version:
    The main issue resided in self.level.platform_list which apparently
    had no attributes in relation to being in the ()'s:
    def update(self):
        self.change_x = 0
        self.change_y = 0
        self.level = None
        self.Gravity()
        self.rectangle.x += self.change_x
        block_Hit_List = P.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_Hit_List:
            if self.change_x > 0:
                self.rectangle.right = block.rect.left
            elif self.change_x < 0:
                self.rectangle.left = block.rect.right
        self.rectangle_y += self.change_y
        block_Hit_List = P.sprite.spritecollide(self, self.level.platform_list, False)
        for block in block_Hit_List:
            if self.change_y > 0:
                self.rectangle.bottom = block.rect.top
            elif self.change_y < 0:
                self.rectangle.top = block.rect.bottom
            self.change_y = 0
    """                
    def Gravity(self):
        #speed = [1, 1]
        grav = 0.1
        #speed[1] += grav
        if not self.landed:
            temp_center = self.rectangle.center #temp store of centre value
            self.rectangle = self.rectangle.move(self.vx, self.vy)
            self.vy += grav #accelerate downwards
            if self.rectangle.center[1] > temp_center[1]:
                self.downwards = True
            else:
                self.downwards = False
        else:
            self.rectangle = self.rectangle.move(-self.vx, 0)
    """
    An atempt at another form of movement via clicks/taps
    To jump upon mousebuttondown instead of moving
    (Was planned on adding buttons for sideway movements):
    def Jump(self):
        self.change_x = 0
        self.change_y = 0
        self.level = None
        self.rectangle.y += 2
        P_Hit_List = P.sprite.spritecollide(self, self.level.platform_list, False)
        self.rectangle.y -= 2
        if len(P_Hit_List) > 0 or self.rect.bottom >= SCREENHEIGHT:
            self.change_y = -10
    """
class Platform(object):
    """The class that'll spawn in the platform to be stood upon my dat boi'
    This reincludes the colours of white, black, red, yellow, blue and green
    Also reincludes screensize and screen to allow definitions for rect
    Includes colour coded/related rect to be defined to be added
    Creates an array to 'allow' the rectangles to spawn in at a random order
    (Randomness is not working)
    Which is then supposed to allow the randomness to pick which to spawn in
    """
        
    def R_A_Random(self, max_vx=5):
        """This allows the choice of a
        'random' shaped/coloured rectangle/platform to spawn in
        To define the basics for the main stuff for the platforms
        To create colour
        To create the screen's size
        To create the rectangles aka platforms
        """
        self.vx = R.randrange(1,max_vx) #define the collision for the main code
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        RED = (255, 0, 0)
        YELLOW = (255, 255, 0)
        GREEN = (0, 255, 0)
        BLUE = (0, 0, 255)
        #define the colours
        SCREENSIZE = SCREENWIDTH, SCREENHEIGHT = 900, 550  # sets size of screen/window
        Screen = P.display.set_mode(SCREENSIZE)  # creates window and game screen
        #define the screen sizes for the rectangles to be drawn
        R_rect = P.draw.rect(Screen, RED, (380, 200, 200, 20), 4)
        B_rect = P.draw.rect(Screen, BLUE, (400, 400, 200, 20), 7)
        Y_rect = P.draw.rect(Screen, YELLOW, (650, 450, 200, 20), 3)
        G_rect = P.draw.rect(Screen, GREEN, (100, 280, 200, 20), 4)
        #define the coloured and shaped rectangles for platforms
        Rect_Array = [R_rect, B_rect, Y_rect, G_rect] #create the array for the random choice of which to spawn
        self.rect = R.choice(Rect_Array) #the command that allows the random choice
        
"""
A part of the attempt at getting a different form of collision to exist:
class Level(object):
    def update(self):
        self.platform_list = P.sprite.Group()
        self.platform_list.update()
    def draw(self, Screen):
        SCREENSIZE = SCREENWIDTH, SCREENHEIGHT = 900, 550  # sets size of screen/window
        Screen = P.display.set_mode(SCREENSIZE)  # creates window and game screen
        #redefine for it to draw on the platform list
        self.platform_list = P.sprite.Group()
        self.platform_list.draw(screen)
"""