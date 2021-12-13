# ===========================================================================
# Copyright 2019 Mateusz Dyrdół. All rights reserved.
# ===========================================================================

from carRental import CarRental
from customer import Customer


def main():
    carRentalOffice = CarRental(100)
    customer = Customer()

    while True:
        print("""
        ---------Rent a car---------
        1. Show available cars
        2. Rent a car on hourly basis 
        3. Rent a car on daily basis  
        4. Rent a car on weekly basis 
        5. Rent a car on monthly basis 
        6. Return a car
        7. Exit
        """)
        
        option = input("Please insert your option: ")
        
        try:
            option = int(option)
        except ValueError:
            print("Invalid input. Please enter number between 1-7")
            continue

        if option == 1:
            carRentalOffice.displaystock()
        elif option == 2:
            customer.rentalTime = carRentalOffice.rentOnHourlyBasis(customer.requestCar())
            customer.rentalBasis = 1
        elif option == 3:
            customer.rentalTime = carRentalOffice.rentOnDailyBasis(customer.requestCar())
            customer.rentalBasis = 2
        elif option == 4:
            customer.rentalTime = carRentalOffice.rentOnWeeklyBasis(customer.requestCar())
            customer.rentalBasis = 3
        elif option == 5:
            customer.rentalTime = carRentalOffice.rentOnMonthlyBasis(customer.requestCar())
            customer.rentalBasis = 4
        elif option == 6:
            customer.bill = carRentalOffice.returnCar(customer.returnCar())
            customer.rentalBasis, customer.rentalTime, customer.bikes = 0, 0, 0
        elif option == 7:
            break		
        else:
            print("Invalid input. Please enter number between 1-7")
    print("Thank you for using our car rental system.")


if __name__=="__main__":
    main()