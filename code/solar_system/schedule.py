class schedule():
    '''this is the schedule'''

    def __init__(self, oa, t, p, name):
        '''initializes the schedule'''
        self.oa = optimum_altitude #where N to S is the panel pointing?  
        self.t = time exposed
        self.p =  #from the sun class, months are either cloudy or sunny  
        self.name = name

    def whatmonth(self):
        '''Every month is defined by a different time step'''
        raise NotImplementedError("Please Implement the whatmonth method!")
        #This containts a check to make sure subclasses implement this.
        return None

    def sunnyorno(self)
        self.p 
  
    def Inexorible(): #I was imagining this as the time step, but maybe that should go in main?