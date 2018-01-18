import math, time


class schedule():
    '''this is the schedule'''

    def __init__(self, oa, om, oe, name):
        '''initializes the schedule'''
        self.oa = optimum_altitude #where N to S is the panel pointing?  
        self.om = optmorning_time #what time should the panel be pointing at 60 degrees from the E horizon
        self.oe = optevening_time #what time should the panel be pointing at 120 degrees from the E horizon 
        self.name = name

        '''At different times of year, the panel needs to change the altitute it points at to better follow the sun'''
        optimum_altitude = 45 #this should change but that's pretty hard

schedule(30, 7.00, 12.00, January) #this assumes that the sun only moves 1 degree north to south every month 
schedule(31, 7.00, 12.00, February)
schedule(32, 7.00, 12.00, March)
schedule(33, 7.00, 12.00, April)
schedule(34, 7.00, 12.00, May)
schedule(35, 7.00, 12.00, June)
schedule(35, 7.00, 12.00, July)
schedule(34, 7.00, 12.00, August)
schedule(33, 7.00, 12.00, September)
schedule(32, 7.00, 12.00, October)
schedule(31, 7.00, 12.00, November)
schedule(30, 7.00, 12.00, December)
    
    def Inexorible():