# Joseph Spear - WGU Student ID: 011552587

import csv
from datetime import datetime, timedelta

from Package import Package
from HashTable import HashTable
from Truck import Truck

# Set groups to hold packages
group1 = []
group2 = []
group3 = []
group4 = []
group5 = []

# Assign Package's Priority
priority1 = []
priority2 = []
priority3 = []

# Initalize trucks for delivery
truck1 = Truck(1,1)
truck2 = Truck(2,2)

# Array to hold the packages ready to be delivered
undelivered_packages = []

available_packages = []


def package_table_loader(hashTable):

    # get package data from csv file
    with open('packages.csv') as packages:
        reader = csv.reader(packages, delimiter = ',')
        for row in reader:
            id_number = int(row[0])
            delivery_address = row[1]
            delivery_city = row[2]
            delivery_state = row[3]
            delivery_zip = row[4]
            delivery_deadline = row[5]
            package_mass = row[6]
            special_notes = row[7]



            # Create package object to use
            package = Package(id_number, delivery_address, delivery_city, delivery_state, delivery_zip,
                          delivery_deadline, package_mass,
                          special_notes)

            # insert package data into hash table
            hashTable.insert(package)
            undelivered_packages.append(package.delivery_address)
            available_packages.append(package.id_number)

def set_package_group(hashTable): # package group is determined by the special notes

    for package in hashTable.package_table:
        if 'Must be delivered with' in package.special_notes \
        or package.id_number == 13 \
        or package.id_number == 15 \
        or package.id_number == 19:
            package.package_group = 1
            group1.append(package.id_number)
        elif 'Can only be on truck 2' in package.special_notes:
            package.package_group = 2
            group2.append(package.id_number)
        elif 'Delayed on flight' in package.special_notes:
            package.package_group = 3
            group3.append(package.id_number)
        elif 'Wrong address listed' in package.special_notes:
            package.package_group = 4
            group4.append(package.id_number)
        else: package.package_group = 5, group5.append(package.id_number)

def set_package_priority(hashTable): #  priority is determined by the delivery deadline
    for package in hashTable.package_table:
        if '9:00 AM' in package.delivery_deadline:
            package.package_priority = 1
            priority1.append(package.id_number)
        elif '10:30 AM' in package.delivery_deadline:
            package.package_priority = 2
            priority2.append(package.id_number)
        else: package.package_priority = 3, priority3.append(package.id_number)

# Look up function to display all package information
def package_lookup(hashTable, prompt):
    id_number = int(prompt)
    package = hashTable.lookup(id_number)

    print("Package Info: \n"
          "Package ID: " + str(package.id_number) + "\n"
          "Delivery Deadline: " + str(package.delivery_deadline) + "\n"                                          
          "Address: " + str(package.delivery_address) + "\n"
          "City: " + str(package.delivery_city) + "\n"
          "Zip: " + str(package.delivery_zip) + "\n"
          "Weight: " + str(package.package_mass) + "\n"
          "Status: " + str(package.delivery_status) + "\n")


def load_distance_data():
    with open('distances.csv') as csv_file:
        # Create a reader object which will iterate over lines in the 'distances.csv' file
        csv_reader = csv.reader(csv_file, delimiter=',')

        # Create the list that will store the distance data
        num_addresses = get_num_addresses()
        distance_data = [[0 for x in range(num_addresses)] for y in range(num_addresses)]

        # Iterate through the reader and parse the distance information between each address
        src_address_index = 0

        for src_address in csv_reader:
            for dest_address_index in range(num_addresses):
                if src_address[dest_address_index] != '':
                    distance_data[src_address_index][dest_address_index] = float(src_address[dest_address_index])
                    distance_data[dest_address_index][src_address_index] = float(src_address[dest_address_index])
            src_address_index = src_address_index + 1

            #print(distance_data[src_address_index -1])

        return distance_data

def distance_table_loader():

    with open('distances.csv') as distances:
        reader = csv.reader(distances, delimiter = ',')



# Returns a list of address data parsed from the 'addresses.csv' file
def load_address_data():
    # Open the 'addresses.csv' file
    with open('addresses.csv') as csv_file:
        address_list = []

        # Create a reader object which will iterate over lines in the packages.csv file
        csv_reader = csv.reader(csv_file, delimiter=',')

        # Iterate through the reader and parse the information from each row
        for row_text in csv_reader:
            # Each row contains the full address for a location. Only parse the street address for the address list
            full_address = row_text[0].split("\n")
            street_address = full_address[1].strip()
            address_list.append(street_address)
            #print(address_list)
    return address_list


# Space-Time Complexity: O(N)
# Returns the number of addresses found in the 'addresses.csv' file based on the number of rows
def get_num_addresses():
    num_addresses = 0
    # Open the 'addresses.csv'  file to count the number of rows in the file
    with open('addresses.csv') as csv_file:
        # Create a reader object which will iterate over lines in the 'distances.csv' file
        csv_reader = csv.reader(csv_file, delimiter=',')

        # Count the number of rows/columns, which will determine the size of the list
        for row in csv_reader:
            num_addresses = num_addresses + 1

    return num_addresses

def id_address_converter(hashTable, id): # some functions use id number or the string address. 
                                         # this is here to make it easier to use both or either
                                         # it takes the id number and returns the address for the package
    address1 = hashTable.lookup(id).delivery_address

    return str(address1)


# Space-Time Complexity: O(1)
# Returns the distance between two addresses
def distance_between(address1, address2):
    distance_list = load_distance_data()
    address_list = load_address_data()

    # Find the index of both addresses
    address1_index = address_list.index(address1)
    address2_index = address_list.index(address2)

    return float(distance_list[address1_index][address2_index])

def find_distance(hashTable, id1, id2): # distance_between function that uses id number instead as input... not necessary just more simple sometimes
    current_address = hashTable.lookup(id1).delivery_address
    checking_address = hashTable.lookup(id2).delivery_address

    distance = float(distance_between(current_address, checking_address))
    return distance

def find_nearest_distance(hashTable, id): # returns the distance to the nearest package
    current_package = hashTable.lookup(id)
    current_package_id = current_package.id_number
    current_address = current_package.delivery_address

    next_address = None
    next_address_distance = 50

    for i in available_packages:
        checking_id = hashTable.lookup(i)
        checking_address = checking_id.delivery_address
        if distance_between(current_address, checking_address) <= next_address_distance:
            next_address = checking_address
            next_address_distance = distance_between(current_address, checking_address)
            next_address_id = checking_id.id_number
    return float(next_address_distance)

def find_nearest_package(hashTable, id): # returns the id number of the nearest package
    current_package = hashTable.lookup(id)
    current_package_id = current_package.id_number
    current_address = current_package.delivery_address

    next_address = None
    next_address_distance = 50

    for i in available_packages:
        checking_id = hashTable.lookup(i)
        checking_address = checking_id.delivery_address
        if distance_between(current_address, checking_address) < next_address_distance:
            next_address = checking_address
            next_address_distance = distance_between(current_address, checking_address)
            next_address_id = checking_id.id_number

    return next_address_id


# assigns and loads the packages onto the truck
def fill_truck(hashTable, truck):

    # Truck 1
    if truck.get_id_number() == 1:
        package_list = available_packages.copy() # copy of package id's to work with

        for package in package_list: # removes packages from available list
            if package in group2 or package in group3 or package in group4:
                package_list.remove(package)

        for i in range(len(priority1)): # adds priority 1 packages
            if priority1[i] not in truck.assigned_packages: truck.capacity = truck.capacity - 1
            if priority1[i] not in truck.assigned_packages: truck.assigned_packages.append(priority1[i])
            if priority1[i] in package_list: package_list.remove(priority1[i])

        if truck.get_capacity() >= len(group1): # if there is room for all of group 1
            for i in range(len(group1)): # add group 1 packages
                if group1[i] not in truck.assigned_packages: truck.capacity = truck.capacity - 1
                if group1[i] not in truck.assigned_packages: truck.assigned_packages.append(group1[i])
                if group1[i] in package_list: package_list.remove(group1[i])

        # fill remaining spots on truck
        truck_fill_remaining_spots(hashTable, truck1, package_list)


    # Truck 2
    elif truck.get_id_number() == 2 and truck.get_capacity() >= len(group2):
        package_list = available_packages.copy()

        for package in truck1.assigned_packages: # removes packages already on truck 1
            package_list.remove(package)

        for i in range(len(group2)): # filters out packages that can not be used
            if group2[i] not in truck.assigned_packages: truck.capacity = truck.capacity - 1
            truck.assigned_packages.append(group2[i])
            if group2[i] in package_list: package_list.remove(group2[i])

        #adds packages until truck is full. truck.display_truck_info()
        truck_fill_remaining_spots(hashTable, truck2, package_list)
 

def truck_fill_remaining_spots(hashTable, truck, package_list): #loops through and finds closest packages
    while truck.get_capacity() > 0: # stops when truck is full
            next_distance = 10
            next_package = None
            for i in truck.assigned_packages: # all packages already in truck
                closest_distance = 10
                closest_package = None
                for j in package_list: # undelivered available packages
                
                    distance = find_distance(hashTable, i, j)
                    package = j
                    checking = i

                    if distance < closest_distance:
                        closest_distance = distance
                        closest_package = package
                if closest_distance < next_distance: 
                    next_distance = closest_distance
                    next_package = closest_package
            
            # adds package to truck and removes it from list
            truck.assigned_packages.append(next_package)
            package_list.remove(next_package)
            truck.capacity = truck.capacity - 1
            

def sort_packages_on_truck(hashTable, truck):
    sorted_list = []
    starting_address = truck.hub_address
    unsorted_list = truck.assigned_packages.copy()
    total_distance = 0

    while len(unsorted_list) > 0:
        next_package =  None
        next_distance = 50

        for i in unsorted_list:
            # finds closest distance from hub
            distance = distance_between(starting_address, id_address_converter(hashTable, i))

            if distance < next_distance:
                next_distance = distance
                next_package = i

        sorted_list.append(next_package)
        if next_package in unsorted_list:
            unsorted_list.remove(next_package)
        starting_address = id_address_converter(hashTable, next_package)
        total_distance = round(total_distance + next_distance,1) 

    # empties the list of packages on truck and copies over the sorted list
    truck.assigned_packages.clear()
    truck.assigned_packages = sorted_list


def complete_route(hashTable, truck):
    starting_address = truck.hub_address
    current_address = starting_address

    for i in truck.assigned_packages: # updates delivery status
        package = hashTable.lookup(i)
        package.delivery_status = "Out for Delivery"
        
    for i in truck.assigned_packages.copy(): # adds mileage from point a to point b and removes package from list after delilvered
        delivery_distance = distance_between(current_address, id_address_converter(hashTable, i)),1
        truck.mileage = round(truck.mileage + distance_between(current_address, id_address_converter(hashTable, i)),1)
        print("Starting Address: ", current_address)
        current_address = id_address_converter(hashTable, i)
        package.delivery_status = "Delivered"
        package.time_of_delivery = truck.start_time + truck.calculate_time(truck.mileage)
        undelivered_packages.remove(id_address_converter(hashTable, i))
        truck.assigned_packages.remove(i)
        truck.capacity += 1
        truck.last_delivered = i

        print("Package: ", i, "\nStatus: ", package.delivery_status)
        print("At: ", package.time_of_delivery)
        print("Next address: ", current_address)
        print("Mileage: ",truck.mileage)
        print("Last Delivery: ", truck.last_delivered)
        print("-----------------------------------")
        print("Truck : ", truck.id_number)
        print("Delivery Completed at ", package.time_of_delivery)

def return_to_hub(hashTable, truck):
        hub = truck.hub_address
        last_delivery = id_address_converter(hashTable, truck.last_delivered)

        truck.mileage = truck.mileage + distance_between(last_delivery, hub)   


def assign_remaining_packages(hashTable, truck):
    remaining = len(undelivered_packages.copy())
    while remaining > 0:
        for package in hashTable.package_table:
            if package.delivery_status == "At the Hub":
                truck.assigned_packages.append(package.id_number)
                truck.capacity = truck.capacity - 1
                remaining = remaining - 1
    sort_packages_on_truck(hashTable, truck)
    complete_route(hashTable, truck)


def prepare_packages(hashTable):

    set_package_group(hashTable)
    set_package_priority(hashTable)

    load_address_data()
    load_distance_data()

    fill_truck(hashTable, truck1)
    fill_truck(hashTable, truck2)

    sort_packages_on_truck(hashTable, truck1)
    sort_packages_on_truck(hashTable, truck2)

def deliver_packages(hashTable):

    complete_route(hashTable, truck1)
    complete_route(hashTable, truck2)
    
    if undelivered_packages != None:
        return_to_hub(hashTable, truck1)
        assign_remaining_packages(hashTable, truck1)

    if undelivered_packages != None:
        return_to_hub(hashTable, truck2)
        assign_remaining_packages(hashTable, truck2)

    

def prompt_time():
    report_datetime = None

    # Prompt the user for a specified time
    while report_datetime is None:
        try:
            report_datetime = datetime.strptime(
                input("Please provide a time for the report in the format [HOUR:MINUTE AM/PM]: "), "%I:%M %p")
        except:
            print("\tError: Invalid time format. Please try again.\n")

    return report_datetime

def main(): # functions calling other functions to maintain clean code

    print("Testing...")

    delivery_table = HashTable() 

    package_table_loader(delivery_table)

    prepare_packages(delivery_table)

    truck1.start_time = timedelta(hours=8,minutes=30)
    truck1.time = truck1.start_time

    print("Start time: ", truck1.start_time)
    print("\nTime of first Delivery: ", truck1.time)

    deliver_packages(delivery_table)

    total_mileage = truck1.mileage + truck2.mileage

    print("EOD MILEAGE: ", total_mileage)

    print("\nTest complete!")



if __name__ == '__main__':
    main()
