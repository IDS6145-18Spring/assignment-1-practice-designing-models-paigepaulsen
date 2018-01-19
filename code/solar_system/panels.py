import math


class panels():
    '''this is the solar panels'''

    def __init__(self, a, s, w, ):
        '''Intializes the panels. Panels are pointing due south to optimize sun'''
        self.a = altitude #where N to S is the panel pointing? 
        self.s = sunny #Is it sunny out? should reference back to the sun.py file
        self.w = windy #is it windy or not? Should reference back to the wind.py file

    def Shelter():
        if wind.speed >= 25 # is this how i ask it to look at a variable in a different class?
            #skip to next timestep 
        else
            return None # I want it to stop if it's too windy, but keep going if it's below 25

    def ChangeAlt(self):
        '''At different times of year, the panel changes the altitute it points at to better follow the sun'''
        self.a = schedule.optimum_altitude
        return self.a
        print str(self.a)

    def ReadSun():
        self.s = sun.power #should ask schedule if sunny or not
