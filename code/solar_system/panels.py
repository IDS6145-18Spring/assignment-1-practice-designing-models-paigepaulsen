import math


class panels():
    '''this is the solar panels'''

    def __init__(self, a, s, e, t):
        '''Intializes the panels. Panels are pointing due south to optimize sun'''
        self.a = altitude #where N to S is the panel pointing?  
        self.s = sunny #Is it sunny out?
        self.t = time_exposed #how long is the panel exposed to sun

    def Shelter():
        if wind.speed >= 25 # is this how i ask it to look at a variable in a different class?
            #skip to next timestep 
        else
            return None

    def ChangeAlt(self):
        '''At different times of year, the panel changes the altitute it points at to better follow the sun'''
        self.a = schedule.optimum_altitude
        return self.a
        print str(self.a)

    def ReadSun():
        self.s = schedule.power #should ask schedule if sunny or not

