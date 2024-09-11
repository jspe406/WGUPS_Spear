# Joseph Spear
# WGU Student ID: 011552587

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

def set_package_group(hashTable):

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

def set_package_priority(hashTable):
    for package in hashTable.package_table:
        if '9:00 AM' in package.delivery_deadline:
            package.package_priority = 1
            priority1.append(package.id_number)
        elif '10:30 AM' in package.delivery_deadline:
            package.package_priority = 2
            priority2.append(package.id_number)
        else: package.package_priority = 3, priority3.append(package.id_number)


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

def find_nearest_package(hashTable, id):
    current_package = hashTable.lookup(id)
    current_package_id = current_package.id_number
    current_address = current_package.delivery_address

    next_address = None
    next_address_distance = 50

    for i in available_packages:
        checking_id = hashTable.lookup(id)
        checking_address = checking_id.delivery_address
        if distance_between(current_address, checking_address) < next_address_distance:
            next_address = checking_address
            next_address_distance = distance_between(current_address, checking_address)

    print("Current: ", current_address, current_package_id, "\n"
          "Next Address: ", next_address, next_address_distance)


def distance_table_loader():

    with open('distances.csv') as distances:
        reader = csv.reader(distances, delimiter = ',')


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


# Space-Time Complexity: O(N)
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


# Space-Time Complexity: O(1)
# Returns the distance between two addresses
def distance_between(address1, address2):
    distance_list = load_distance_data()
    address_list = load_address_data()

    # Find the index of both addresses
    address1_index = address_list.index(address1)
    address2_index = address_list.index(address2)

    return distance_list[address1_index][address2_index]

# assigns and loads the packages onto the truck
def fill_truck(hashTable, truck):

    if truck.get_id_number() == 1:
        for package in available_packages:
            if package in group2 or package in group3 or package in group4:
                available_packages.remove(package)

        print(len(available_packages))
        for i in range(len(priority1)):
            if priority1[i] not in truck.assigned_packages: truck.capacity = truck.capacity - 1
            truck.assigned_packages.add(priority1[i])
            if priority1[i] in available_packages: available_packages.remove(priority1[i])


        truck.display_truck_info()
        print(available_packages)
        print(group1)

        if truck.get_capacity() >= len(group1):
            print(available_packages)
            for i in range(len(group1)):
                if group1[i] not in truck.assigned_packages: truck.capacity = truck.capacity - 1
                truck.assigned_packages.add(group1[i])
                if group1[i] in available_packages: available_packages.remove(group1[i])




        truck.display_truck_info()


    elif truck.get_id_number() == 2 and truck.get_capacity() >= len(group2):
        print("Packages for Truck2: ",available_packages, "\n"
              "Count: ", len(available_packages))
        for i in range(len(group2)):
            if group2[i] not in truck.assigned_packages: truck.capacity = truck.capacity - 1
            truck.assigned_packages.add(group2[i])
            if group2[i] in available_packages: available_packages.remove(group2[i])
'''
        truck.display_truck_info()
        print(len(available_packages))
        print(available_packages)
'''



def prepare_packages(hashTable):

    set_package_group(hashTable)
    set_package_priority(hashTable)

    load_address_data()
    load_distance_data()
    fill_truck(hashTable, truck1)
    fill_truck(hashTable, truck2)


# def deliver_packages(hashTable):

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

def main():
    print("Testing...")

    delivery_table = HashTable()

    package_table_loader(delivery_table)

    prepare_packages(delivery_table)

    #package_lookup(delivery_table, input("\nCheck Package Info for [Package ID]:\n "))
    #print(undelivered_packages)


    #find_nearest_package(delivery_table, 3)
    print("\nTest complete!")


    #test_nearest_package(delivery_table, 1)
if __name__ == '__main__':
    main()
