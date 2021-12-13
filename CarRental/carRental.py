# ===========================================================================
# Copyright 2019 Mateusz Dyrdół. All rights reserved.
# ===========================================================================
import datetime


class CarRental:
    def __init__(self, stock=0):
        self.stock = stock

    def displaystock(self):
        print("We have currently {} cars available to rent.".format(self.stock))
        return self.stock

    def rentOnHourlyBasis(self, n):
        if n <= 0:
            print("Number of cars should be positive!")
            return None
        
        elif n > self.stock:
            print("Sorry! We have currently {} cars available to rent.".format(self.stock))
            return None
        
        else:
            now = datetime.datetime.now()                      
            print("You have rented a {} car(s) on hourly basis today at {}:{}.".format(n, now.hour, now.minute))
            print("You will be charged $20 for each hour per car.")
            print("We hope that you enjoy our service.")
            self.stock -= n
            return now      
     
    def rentOnDailyBasis(self, n):
        if n <= 0:
            print("Number of cars should be positive!")
            return None

        elif n > self.stock:
            print("Sorry! We have currently {} cars available to rent.".format(self.stock))
            return None
    
        else:
            now = datetime.datetime.now()                      
            print("You have rented {} car(s) on daily basis today at {}:{}.".format(n, now.hour, now.minute))
            print("You will be charged $150 for each day per car.")
            print("We hope that you enjoy our service.")
            self.stock -= n
            return now
        
    def rentOnWeeklyBasis(self, n):
        if n <= 0:
            print("Number of cars should be positive!")
            return None

        elif n > self.stock:
            print("Sorry! We have currently {} cars available to rent.".format(self.stock))
            return None        
        
        else:
            now = datetime.datetime.now()
            print("You have rented {} car(s) on weekly basis today at {}:{}.".format(n, now.hour, now.minute))
            print("You will be charged $650 for each week per car.")
            print("We hope that you enjoy our service.")
            self.stock -= n

            return now

    def rentOnMonthlyBasis(self, n):
        if n <= 0:
            print("Number of cars should be positive!")
            return None

        elif n > self.stock:
            print("Sorry! We have currently {} cars available to rent.".format(self.stock))
            return None

        else:
            now = datetime.datetime.now()
            print("You have rented {} car(s) on weekly basis today at {}:{}.".format(n, now.hour, now.minute))
            print("You will be charged $3000 for each month per car.")
            print("We hope that you enjoy our service.")
            self.stock -= n
            return now


    def returnCar(self, request):
        rentalTime, rentalBasis, numOfCars = request
        bill = 0

        if rentalTime and rentalBasis and numOfCars:
            self.stock += numOfCars
            now = datetime.datetime.now()
            rentalPeriod = now - rentalTime
        
            # hourly bill calculation
            if rentalBasis == 1:
                bill = round(rentalPeriod.seconds / 3600) * 20 * numOfCars
                
            # daily bill calculation
            elif rentalBasis == 2:
                bill = round(rentalPeriod.days) * 150 * numOfCars
                
            # weekly bill calculation
            elif rentalBasis == 3:
                bill = round(rentalPeriod.days/7) * 650 * numOfCars

            # monthly bill calculation
            elif rentalBasis == 4:
                bill = round(rentalPeriod.days/30) * 3000 * numOfCars

            print("Thanks for returning your car. Hope you enjoyed our service!")
            print("That would be ${}".format(bill))
            return bill
        else:
            print("Are you sure you rented a car with us?")
            return None

