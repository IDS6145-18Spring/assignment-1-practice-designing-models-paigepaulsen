import math


class panels():
    '''this is the solar panels'''

    def __init__(self, a, m, e, t):
        '''Intializes the wind'''
        self.a = altitude #where N to S is the panel pointing?  
        self.m = morning_angle #where the panel points E to W in the morning hours
        self.e = evening_angle #where the panel points E to W in the afternoon hours
        self.t = time_exposed #how long is the panel exposed to sun

    def ChangeAlt(self):
        '''At different times of year, the panel changes the altitute it points at to better follow the sun'''
        self.a = 