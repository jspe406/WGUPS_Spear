

class Package:

    def __init__(self, id_number, delivery_address, delivery_city, delivery_state, delivery_zip, delivery_deadline,
                 package_mass, special_notes):
        self.id_number = id_number
        self.delivery_address = delivery_address
        self.delivery_city = delivery_city
        self.delivery_state = delivery_state
        self.delivery_zip = delivery_zip
        self.delivery_deadline = delivery_deadline
        self.package_mass = package_mass
        self.special_notes = special_notes
        self.package_group = 0
        self.package_priority = 0
        self.delivery_status = "At the Hub"
        self.time_of_delivery = None
        self.time_put_on_truck = None


    def get_address(self):
        return self.delivery_address

    def get_status(self):
        return self.delivery_status

    def is_on_truck(self, time):
        if time.time() > self.time_put_on_truck and time < self.time_of_delivery:
            return True

    def is_delivered(self, time):
        if time.time() >  self.time_of_delivery:
            return True
    
