class schedule():
    '''this is the schedule'''

    def __init__(self, oa, t, name, step):
        '''initializes the schedule'''
        self.oa = optimum_altitude #where N to S is the panel pointing?  
        self.t = time_exposed
        self.name = name
        self.step = main.timestep % 12

    January = schedule(30,9.0,January,0) #Instead of making these individual classes, I'm moving them to objects. I want to instantiate them here if I can but they will need to be called in other places probably
    February = schedule(31,9.3,February,1) #Months have different optimum altitude, time of sunshine, names, and are indicated by a the modulo from the timestep (every time step is a new month. Time is weird in this simulation)
    March = schedule(32,10.0,March,2) 
    April = schedule(33,10.5,April,3)
    May = schedule(34,10.8,May,4)
    June = schedule(35,12,June,5)
    July = schedule(35,11.5,July,6)
    August = schedule(34,10.5,August,7)
    September = schedule(33,10,September,8)
    October = schedule(32,9.8,October,9)
    November = schedule(31,9.3,November,10)
    December = schedule(30,9.0,December,11)

    def whatmonth(self):
        '''Every month is defined by a different time step'''
        if timestep % 12 == 0: #timestep should be in main, like in POTS, right? Or is it okay to set the month inside the class?
            return January(schedule) # is this how I set this?
        else:
            return None #is this how I get it to look at the other options? Or is this totally redundant from the instances above?
        if timestep % 12 == 1: #timestep should be in main, like in POTS, right?
            return February(schedule) # is this how I set this?
        else:
            return None 
        if timestep % 12 == 2:
            return March(schedule) # is this how I set this?
        else: 
            return None 
        if timestep % 12 == 3: #timestep should be in main, like in POTS, right? Or is it okay to set the month inside the class?
            return April(schedule) # is this how I set this?
        else:
            return None 
        if timestep % 12 == 4: #timestep should be in main, like in POTS, right? Or is it okay to set the month inside the class?
            return May(schedule) # is this how I set this?
        else:
            return None            

    def sunnyorno(self):
        self.p = sun.power
        return sun.power
  