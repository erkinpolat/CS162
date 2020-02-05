#Creating the class
class ClockIterator:
    
    #initializing the minute, hour and the string times
    def __init__(self, max):
        self.max = max
    
    #Defining the iter method. Here it just returns self
    def __iter__(self):
        self.min = 0
        self.hour = 0
        self.count = 0
        self.time = str(self.hour).zfill(2) + ':' + str(self.min).zfill(2)
        return self
    
    #For the next step, we increase the minute by 1.
    def __next__(self):
        self.min += 1
        
        #Whenever it exceeds 60 we carry to hour
        if self.min == 60:
            self.min = 0
            self.hour += 1
        
        #Whenever hour reaches 24, we reset it back to 0
        if self.hour == 24:
            self.hour = 0
            
        #We reform the string time
        self.time = str(self.hour).zfill(2) + ':' + str(self.min).zfill(2)
        
        #When we reach the limit given at the beginning we stop iteration 
        self.count += 1
        if self.count == self.max:
            raise StopIteration
        
        return self.time
