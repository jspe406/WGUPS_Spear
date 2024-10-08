import Package
import HashTable
from datetime import timedelta
from datetime import datetime, timedelta

class Truck:
    def __init__(self, id_number, driver):
        self.id_number = id_number
        self.assigned_packages = []
        self.capacity = 16
        self.hub_address = "4001 South 700 East"
        self.driver = driver
        self.speed = 18 # Miles per Hour
        self.mileage = 0
        self.last_delivered = None
        self.start_time = timedelta(hours = 8, minutes = 0, seconds = 0)
        self.time = None
        self.last_time = None
        self.second_start = timedelta(hours = 10, minutes = 7, seconds = 20)

# get functions
    def get_id_number(self):
        return self.id_number

    def get_assigned_packages(self):
        return self.assigned_packages

    def get_capacity(self):
        return self.capacity

    def get_driver(self):
        return self.driver

    def get_assigned_packages(self):
        return self.assigned_packages
    
    def get_mileage(self):
        return self.mileage
    
    def get_last_delivered(self):
        return self.last_delivered
    
    def get_start_time(self):
        return self.start_time
    
    def get_time(self):
        return self.time
    
    def add_time(self, distance):
        self.time += timedelta(minutes=(distance / self.speed * 60))
        return self.time

    def calculate_time(self, distance):
        return timedelta(minutes=(distance / self.speed * 60))


    def time_to_mileage(self, time):
        if self.id_number == 1 and time < datetime.strptime(str(timedelta(hours=8, minutes=0, seconds=0)), "%H:%M:%S"):
            mileage = 0

        elif self.id_number == 2 and time < self.start_time:
            mileage = 0
        else:
            if time > self.last_time: time = self.last_time
            if self.id_number == 1:
                start_time = timedelta(hours = 8, minutes = 0, seconds = 0)
                start_time = datetime.strptime(str(start_time), "%H:%M:%S")
                mileage = round(((time - start_time).total_seconds() / 3600 * self.speed), 1)
            if self.id_number == 2:
                start_time = timedelta(hours = 9, minutes = 5, seconds = 0)
                start_time = datetime.strptime(str(start_time), "%H:%M:%S")
                mileage = round(((time - start_time).total_seconds() / 3600 * self.speed), 1)

        return mileage