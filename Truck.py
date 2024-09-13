import Package
import HashTable
from datetime import timedelta


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

# check to see if package is loaded onto truck
    def check_for_packages(self, package_id):
        if package_id in self.assigned_packages:
            return True, print("Package is on Truck: %d" % self.id_number)
        else: return False, print("Package is not on Truck: %d" % self.id_number)

# display all the truck attributes
    def display_truck_info(truck):
        print("Truck ID: ", truck.id_number, "\n"
              "Assigned [%d] Packages: " % len(truck.assigned_packages),truck.assigned_packages, "\n"
              "Available Slots on Truck: ", truck.capacity, "\n"
              "Driver Assigned to truck: ", truck.driver)