# In-Class Exercise #3 - Add a method that takes in three 
# parameters of year, doors and seats and prints out a formatted 
# print statement with make, model, year, seats, and doors

# Create class with 2 paramters inside of the __init__ which are make and model
class Car():
    color = 'black'
    def __init__(self, make, model):
        self.make = make
        self.model = model
        
    def buildCar(self, year, doors, seats):
        self.year = year
        self.doors = doors
        self.seats = seats
        print(f'You have a {self.doors}.')

    def carYear(self, year):
        year_made = input("What is the year of your car? ")
        self.make.append(year_made)
        
    def carDoors(self, doors):
        the_doors = input("How many doors does it have? ")
        self.make.append(the_doors)
        
    def carSeats(self, seats):
        seating = input("What is the make of your car? ")
        self.make.append(seating)
        
