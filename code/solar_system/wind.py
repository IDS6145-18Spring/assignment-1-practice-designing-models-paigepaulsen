import math


class wind():
    '''this is the wind'''

    def __init__(self, s):
        '''Intializes the wind'''
        self.s = speed  
        self.s = 1 # the speed of the wind is usually gentle

    def Blow(self):
        '''Sometimes the wind gets stronger and dangerous'''
        self.s = 25
        print ("the wind could knock over the panels!")