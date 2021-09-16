class vehicle:
    def __init__(self,members_name, mileage, capacity,member_function):
          self.members_name = members_name
          self.mileage = mileage
          self.capacity = capacity
          self.member_function = member_function

    def fare_amount(self):
        return self.capacity * 100

class Bus(vehicle):
        def fare_amount(self):
            bus_fare = self.capacity * 100
            total_fare = bus_fare + (0.10 * bus_fare)
            return total_fare

school_bus = Bus("skool bus",'20km/hr',50,'private transportation')
print(school_bus.fare_amount())
