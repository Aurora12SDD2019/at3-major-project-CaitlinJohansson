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


# templates
def function_name(arg1, arg2, other_silly_variable=None):
    """Does something amazing.

    a much longer description of the really amazing stuff this function does and how it does it.

    Args:
        arg1: the first argument required by the function.
        arg2: the second argument required by the function.
        other_silly_variable: Another optional variable, that has a much
            longer name than the other args, and which does nothing.

    Returns:
        description of the stuff that is returned by the function.

    Raises:
        AnError: An error occurred running this function.
    """
    pass

class Polygon(object):
    """Summary of polygon, my boi: the sprite

    Attributes:
        image: who dat boi is
        location: where dat boi is (coodinates, window)
    """

    def __init__(self, window):
        """Inits my boi polygon image n location."""
        self.window = window
        self.position = [100, 100]
        self.image = P.image.load('media/YA BOI POLYGON Perfected.png').convert()
        #self.show()
        
    def show(self):
        self.window.blit(self.image, self.position)
        
    def moveTowards(self, position):
        """Makes my boi move to where you press"""
        P_X = self.position[0] #P standing for my boi
        P_Y = self.position[1]
        M_X = position[0] #M standing for mouse/touch
        M_Y = position[1]
        My_X = (M_X - P_X) #My meaning my new positioning
        My_Y = (M_Y - P_Y) #/2 to make the distance half the requested space if wanted
        self.position = [P_X+My_X, P_Y+My_Y]
        #self.show()

class SampleClass(object):
    """Summary of class here.

    Longer class information....

    Attributes:
        likes_spam: A boolean indicating if we like SPAM or not.
        eggs: An integer count of the eggs we have laid.
    """

    def __init__(self, likes_spam=False):
        """Inits SampleClass with blah."""
        self.likes_spam = likes_spam
        self.eggs = 0

    def public_method(self):
        """Performs operation blah."""
        
class Platform(object):
    """la platforma has a colour to show itself has a x and y position can be stood upon may move"""
    def _init_(self, Screen, col):
        """Initiates clss with colour n position"""
        self.x = 700
        self.y = 300
        self.rectangle = P.rect(self.x,self.y,100,20)
        self.colour = col
        
    def show(self):
        """allows platforms to appear"""
        P.draw.rect(self.window, self.colour, self.rectangle)