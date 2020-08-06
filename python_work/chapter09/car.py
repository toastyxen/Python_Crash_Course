# A set of classes used to represent gas and electric cars
class Car:
    # A Simple attempt to represent a car
    def __init__(self, make, model, year):
        # Initialize attributes to describe a car
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        # Return a neatly formatted descriptiove name
        # The code in the book they have {self.manufacturer}, instead of {self.make} 
        # I pressume to diliberatly cause an error so you can trouble shoot
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        # Print statement showing the car's milaage
        print(f"This car has {self.odometer_reading} miles on it.")
    
    def update_odometer(self, mileage):
        # Set the odometer to the given value
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        # Add given amount to the odometer reading.
        if miles < 0:
            print("You can't roll back an odometer!")
        else:
            self.odometer_reading += miles