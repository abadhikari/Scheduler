from datetime import datetime
from calendar import monthrange

class date:
    def __init__(self,month,day,year,hour=12,minute=0,time_of_day='AM'):
        self.month = month
        self.day = day
        self.year = year
        self.hour = hour
        self.minute = minute
        self.time_of_day = time_of_day

    def find_priority(self):
        # gives a value for the priority in the pq depending on the date due vs current date
        pass

    def __str__(self):
        return str(self.month) + '/' + str(self.day) + '/' + str(self.year) + '/' + str(self.hour) + '/' + str(self.minute) + self.time_of_day
