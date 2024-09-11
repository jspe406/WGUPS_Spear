import Package
import HashTable


class Truck:
    def __init__(self, id_number, driver):
        self.id_number = id_number
        self.assigned_packages = set()
        self.capacity = 16
        self.driver = driver
        self.speed = 18 # Miles per Hour

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
