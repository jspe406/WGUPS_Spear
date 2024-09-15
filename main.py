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
truck_list = [truck1.id_number, truck2.id_number]

total_mileage = truck1.mileage + truck2.mileage

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

def package_lookup(hashTable, id): # look up function for requirement B
    package = hashTable.package_table[id]

    print("Delivery Address: ", package.delivery_address, "\n"
          "Delivery Deadline: ", package.delivery_deadline, "\n"
          "City: ", package.city, "\n"
          "Zip Code: ", package.zip_code, "\n"
          "Weight (kg): ", package.weight, "\n"
          "Status: " + package.delivery_status, "\n"
          "Delivery Time: ", package.time_of_delivery, "\n")

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

    
def update_address(hashTable, id):
    self = hashTable.lookup(id)
    self.delivery_address = '410 S State St'
    self.delivery_city = 'Salt Lake City'
    self.delivery_state = 'UT'
    self.delivery_zip = '84111'


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

        for package in package_list:
            if package == 9:
                package_list.remove(package)

        for i in range(len(group2)): # adds group 2 packages to truck
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
    '''Selection sort method used. It finds the package in the list that is closest to the Hub.
    Then creates a new array and adds the package. Then finds the next closest package to the one that was previously added.
    This process repeats until all packages from the unsorted list have been placed in the sorted list'''
    sorted_list = []
    starting_address = truck.hub_address
    unsorted_list = truck.assigned_packages.copy()
    total_distance = 0

    while len(unsorted_list) > 0:
        next_package =  None
        next_distance = 50

        for i in unsorted_list:
            package = hashTable.lookup(i)
            package.time_put_on_truck = truck.start_time 
            # finds closest distance from hub
            distance = distance_between(starting_address, id_address_converter(hashTable, i))

            if distance < next_distance:
                next_distance = distance
                next_package = i

        sorted_list.append(next_package)
        if next_package in unsorted_list: # removes from unsorted list
            unsorted_list.remove(next_package)
        starting_address = id_address_converter(hashTable, next_package)
        total_distance = round(total_distance + next_distance,1)
        

    # empties the list of packages on truck and copies over the sorted list
    truck.assigned_packages.clear()
    truck.assigned_packages = sorted_list


def complete_route(hashTable, truck): # takes the loaded truck and delivers all packages in order on truck
    starting_address = truck.hub_address
    current_address = starting_address
    trip_mileage = 0

    for i in truck.assigned_packages: # updates delivery status
        package = hashTable.lookup(i)
        package.delivery_status = "Out for Delivery"
        
    for i in truck.assigned_packages.copy(): # adds mileage from point a to point b and removes package from list after delilvered
        package = hashTable.lookup(i)

        truck.mileage = round(truck.mileage + distance_between(current_address, id_address_converter(hashTable, i)),1)
        trip_mileage = round(trip_mileage + distance_between(current_address, id_address_converter(hashTable, i)),1)
        current_address = id_address_converter(hashTable, i)

        package.delivery_status = "Delivered"
        if truck.start_time == timedelta(hours = 10, minutes = 7, seconds = 20): # for the second truck a different value was needed to track the time of delivery
            if truck.assigned_packages == [0]: current_address = truck.hub_address
            package.time_of_delivery = truck.start_time + truck.calculate_time(trip_mileage)
        else:
            package.time_of_delivery = truck.start_time + truck.calculate_time(truck.mileage)
        truck.last_time = package.time_of_delivery
        truck.last_time = datetime.strptime(str(truck.last_time), '%H:%M:%S')

        if id_address_converter(hashTable, i) in undelivered_packages: undelivered_packages.remove(id_address_converter(hashTable, i))
        truck.assigned_packages.remove(i)
        truck.capacity += 1
        truck.last_delivered = i

        '''  
        #leaving this in if needed for debugging because it was useful for tracking and finding errors.
        
        print("Package: ", i, "\nStatus: ", package.delivery_status)
        print("Start Time: ", package.time_put_on_truck)
        print("At: ", package.time_of_delivery)
        print("Next address: ", current_address)
        print("Mileage: ",truck.mileage)
        print("Last Delivery: ", truck.last_delivered)
        
        print("Truck : ", truck.id_number)
        print("Delivery Completed at ", package.time_of_delivery)
        print("-----------------------------------")
        '''

def return_to_hub(hashTable, truck):
        hub = truck.hub_address
        last_delivery = id_address_converter(hashTable, truck.last_delivered)

        truck.mileage = truck.mileage + distance_between(last_delivery, hub)

        truck.time = truck.start_time + truck.calculate_time(truck.mileage)
        truck.start_time = truck.time


def assign_remaining_packages(hashTable, truck):
    remaining = len(undelivered_packages.copy())
    while remaining > 0:
        for package in hashTable.package_table:
            if package.delivery_status == "At the Hub":
                truck.assigned_packages.append(package.id_number)
                truck.capacity = truck.capacity - 1
                remaining = remaining - 1
    sort_packages_on_truck(hashTable, truck)


def prepare_trucks(): # sets start times for trucks
    truck2.start_time = timedelta(hours=9, minutes=5)  # Truck 2 start time
    truck2.time = truck2.start_time
    truck1.start_time = timedelta(hours=8, minutes=0)
    truck1.time = truck1.start_time


def transform_time_data(hashTable): # changes time data to be able be used in other functions
    for package in hashTable.package_table:
        time = str(package.time_put_on_truck)
        parsed_time = datetime.strptime(time, "%H:%M:%S").time()
        package.time_put_on_truck = parsed_time

        time = str(package.time_of_delivery)
        parsed_time = datetime.strptime(time, "%H:%M:%S").time()
        package.time_of_delivery = parsed_time


def transform_truck_times(): #changes time format to be able to be used in other functions
    # truck 1 start time
    time = str(truck1.start_time)
    parsed_time = datetime.strptime(time, "%H:%M:%S")
    truck1.start_time = parsed_time
    # truck 2 start time
    time = str(truck2.start_time)
    parsed_time = datetime.strptime(time, "%H:%M:%S")
    truck2.start_time = parsed_time


def prepare_packages(hashTable): # assigns packages to trucks based on the most optimal route and then sorts all packages.
    set_package_group(hashTable)
    set_package_priority(hashTable)

    load_address_data()
    load_distance_data()

    fill_truck(hashTable, truck1)
    fill_truck(hashTable, truck2)

    sort_packages_on_truck(hashTable, truck1)
    sort_packages_on_truck(hashTable, truck2)


def deliver_packages(hashTable): # runs through to complete the routes and bring truck 1 back to the hub to deliver remaining packages
    complete_route(hashTable, truck1)
    complete_route(hashTable, truck2)

    return_to_hub(hashTable, truck1)
    update_address(hashTable, 9)  # truck 1 arrives back to hub at 10:37 so we can now update the address for package 9
    assign_remaining_packages(hashTable, truck1)

    complete_route(hashTable, truck1)


def prompt_time(): # takes input from the user to pass to inquires for a time
    report_datetime = None
    # Prompt the user for a specified time
    while report_datetime is None:
        try:
            report_datetime = datetime.strptime(
                input("Please provide a time for the report in the format [HOUR:MINUTE AM/PM]: "), "%I:%M %p")
        except:
            print("\tError: Invalid time format. Please try again.\n")

    return report_datetime


def lookup_individual(hashTable):  # function to display data for any given package at any given time

    while True:  # ensures that input form user is within the range of vaild ID numbers
        try:
            id = int(input("Please type the ID number of the package you would like to check (0-39): "))
            if 0 <= id <= 39:
                break
            else:
                print("Invalid input. Please enter a number between 1 and 40.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    time = prompt_time()
    parsed_time = time.time()
    package = hashTable.package_table[id]
    status = package.delivery_status
    start = package.time_put_on_truck
    delivery_time = package.time_of_delivery

    mileage1 = truck1.time_to_mileage(time)
    mileage2 = truck2.time_to_mileage(time)
    total_mileage = mileage1 + mileage2

    # assings a temporary status based on input time

    if parsed_time < start:
        status = "At the Hub"
    if parsed_time > start and parsed_time < delivery_time:
        status = 'En Route'
    elif parsed_time > delivery_time:
        status = 'Delivered'
    delivery_time = datetime.strptime(str(delivery_time), "%H:%M:%S")
    delivery_time = datetime.strftime(delivery_time, "%I:%M %p")

    message = "\nPackage: " + str(id) + " | " + "Status: " + status + " | "
    if status == "Delivered":
        message += "Time of Delivery: " + str(delivery_time) + " | "
    message += "Address: %s, %s %s | " % (str(package.delivery_address), str(package.delivery_city), str(package.delivery_zip))
    message += "Mileage of Truck 1: " + str(mileage1) + " | "
    message += "Mileage of Truck 2: " + str(mileage2) + " | "
    message += "Mileage of both Trucks: " + str(total_mileage) + " | "
    print(message)

    input("Press 'ENTER' to continue")
    prompt_interactive_menu(hashTable, truck_list)


def display_all_packages(hashTable):  # displays all packages and status' at a given time
    time = prompt_time()
    parsed_time = time.time()
    check_time = datetime.strftime(time, "%I:%M %p")

    for i in range(1, 40):  # sets a temporary status for status based on the time of inquiry
        package = hashTable.package_table[i]
        if parsed_time < package.time_put_on_truck:
            status = "At the Hub"
        if parsed_time > package.time_put_on_truck and parsed_time < package.time_of_delivery:
            status = 'En Route'
        elif parsed_time > package.time_of_delivery:
            status = 'Delivered'

        package_info = "Package: " + str(package.id_number) + " | "
        package_info += "Status: " + str(status) + " | "
        if status == "Delivered":
            package_info += "Time of Delivery: " + str(package.time_of_delivery) + " | "
        print(package_info)

    package = hashTable.package_table[
        0]  # package at index 0 is ID 40. I didn't like it printing out starting with ID 40. so I removed it from the loop
    if parsed_time < package.time_put_on_truck:
        status = "At the Hub"
    if parsed_time > package.time_put_on_truck and parsed_time < package.time_of_delivery:
        status = 'En Route'
    elif parsed_time > package.time_of_delivery:
        status = 'Delivered'

    package_info = "Package: " + str(package.id_number) + " | "
    package_info += "Status: " + str(status) + " | "
    if status == "Delivered":
        package_info += "Time of Delivery: " + str(package.time_of_delivery) + " | "
    print(package_info)

    print("Total Miles", (truck1.time_to_mileage(time) + truck2.time_to_mileage(time)))  # mileage of both trucks
    print("Checked at: ", check_time)

    input("Press 'ENTER' to continue")  # creates a break after running the function before running the menu
    prompt_interactive_menu(hashTable, truck_list)


def prompt_interactive_menu(hashTable, truck_list):
    # Display the title of the application
    print("===========================================")
    print("Western Governors University Parcel Service")
    print("===========================================")

    # Display menu options
    print("Please select a menu option to generate a report or retrieve package information.\n")
    print("\t 1. General Report [ALL PACKAGES]")
    print("\t 2. Package Query [INDIVIDUAL PACKAGE]")
    print("\t 3. Exit Program")
    valid_options = [1, 2, 3]

    # Prompt the user for option selection:
    option = None

    while option is None:
        user_input = input("\nEnter your option selection here: ")

        if user_input.isdigit() and int(user_input) in valid_options:
            option = int(user_input)
        else:
            print("Error: Invalid option provided.")

    # Process the option selected by the end-user:
    if option == 1: display_all_packages(hashTable)
    if option == 2: lookup_individual(hashTable)
    if option == 3:
        print("\nThank You. Program will now self-destruct.")
        quit()

def main(): # functions calling other functions to maintain clean code

    print("Program Started...\n")

    delivery_table = HashTable() 
    
    package_table_loader(delivery_table)

    prepare_trucks()

    prepare_packages(delivery_table)

    deliver_packages(delivery_table)

    transform_time_data(delivery_table)
    transform_truck_times()

    prompt_interactive_menu(delivery_table, truck_list)

if __name__ == '__main__':
    main()
