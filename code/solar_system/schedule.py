import math


class schedule():
    '''this is the schedule'''

    def __init__(self, oa, om, oe, name):
        '''initializes the schedule'''
        self.oa = optimum_altitude #where N to S is the panel pointing?  
        self.om = morning_angle #where the panel points E to W in the morning hours
        self.oe = evening_angle #where the panel points E to W in the afternoon hours
        self.name = name

        '''At different times of year, the panel needs to change the altitute it points at to better follow the sun'''
        optimum_altitude = 45 #this should change but that's pretty hard