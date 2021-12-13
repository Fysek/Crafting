# ===========================================================================
# Copyright 2019 Mateusz Dyrdół. All rights reserved.
# ===========================================================================

class Customer:
    def __init__(self):
        self.cars = 0
        self.rentalBasis = 0
        self.rentalTime = 0
        self.bill = 0

    def requestCar(self):
        cars = input("How many cars would you like to rent?")
        try:
            cars = int(cars)
        except ValueError:
            print("That's not a positive integer!")
            return -1

        if cars < 1:
            print("Invalid input. Number of cars should be greater than zero!")
            return -1
        else:
            self.cars = cars
        return self.cars

    def returnCar(self):
        if self.rentalBasis and self.rentalTime and self.cars:
            return self.rentalTime, self.rentalBasis, self.cars
        else:
            return 0, 0, 0
