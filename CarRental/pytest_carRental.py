import pytest
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from carRental import CarRental
from customer import Customer


def test_Car_Rental_displays_correct_stock(self):
    shop1 = CarRental()
    shop2 = CarRental(10)
    assert shop1.displaystock() == 0
    assert shop2.displaystock() == 10
    
def test_rentCarOnHourlyBasis_for_negative_number_of_cars(self):
    shop = CarRental(10)
    assert shop.rentOnHourlyBasis(-1) == None

def test_rentCarOnHourlyBasis_for_zero_number_of_cars(self):
    shop = CarRental(10)
    assert (shop.rentOnHourlyBasis(0) == None

def test_rentCarOnHourlyBasis_for_valid_positive_number_of_cars(self):
    shop = CarRental(10)
    hour = datetime.now().hour
    assert shop.rentOnHourlyBasis(2).hour == hour

def test_rentCarOnHourlyBasis_for_invalid_positive_number_of_cars(self):
    shop = CarRental(10)
    assert shop.rentOnHourlyBasis(11) == None

def test_rentCarOnDailyBasis_for_negative_number_of_cars(self):
    shop = CarRental(10)
    assert shop.rentOnDailyBasis(-1) == None

def test_rentCarOnDailyBasis_for_zero_number_of_cars(self):
    shop = CarRental(10)
    assert shop.rentOnDailyBasis(0) == None

def test_rentCarOnDailyBasis_for_valid_positive_number_of_cars(self):
    shop = CarRental(10)
    hour = datetime.now().hour
    assert shop.rentOnDailyBasis(2).hour == hour

def test_rentCarOnDailyBasis_for_invalid_positive_number_of_cars(self):
    shop = CarRental(10)
    assert shop.rentOnDailyBasis(11) == None

def test_rentCarOnWeeklyBasis_for_negative_number_of_cars(self):
    shop = CarRental(10)
    assert shop.rentOnWeeklyBasis(-1) == None

def test_rentCarOnWeeklyBasis_for_zero_number_of_cars(self):
    shop = CarRental(10)
    assert shop.rentOnWeeklyBasis(0) == None

def test_rentCarOnWeeklyBasis_for_valid_positive_number_of_cars(self):
    shop = CarRental(10)
    hour = datetime.now().hour
    assert shop.rentOnWeeklyBasis(2).hour == hour

def test_rentCarOnWeeklyBasis_for_invalid_positive_number_of_cars(self):
    shop = CarRental(10)
    assert shop.rentOnWeeklyBasis(11) == None

def test_returnCar_for_invalid_rentalTime(self):
    # create a shop and a customer
    shop = CarRental(10)
    customer = Customer()

    # let the customer not rent a bike a try to return one.
    request = customer.returnCar()
    assert shop.returnCar(request) == None

    # manually check return function with error values
    assert shop.returnCar((0,0,0)) == None
    
def test_returnCar_for_invalid_rentalBasis(self):
    # create a shop and a customer
    shop = CarRental(10)
    customer = Customer()
    
    # create valid rentalTime and cars
    customer.rentalTime = datetime.now()
    customer.cars = 3

    # create invalid rentalbasis
    customer.rentalBasis = 8

    request = customer.returnCar()
    assert shop.returnCar(request) == 0

def test_returnCar_for_invalid_numOfCars(self):
 
    # create a shop and a customer
    shop = CarRental(10)
    customer = Customer()
    
    # create valid rentalTime and rentalBasis
    customer.rentalTime = datetime.now()
    customer.rentalBasis = 1

    # create invalid cars
    customer.cars = 0

    request = customer.returnCar()
    assert shop.returnCar(request) == None

def test_returnCar_for_valid_credentials(self):
 
    # create a shop and a various customers
    shop = CarRental(50)
    customer1 = Customer()
    customer2 = Customer()
    customer3 = Customer()
    customer4 = Customer()
    customer5 = Customer()
    customer6 = Customer()
    customer7 = Customer()
    customer8 = Customer()

    # create valid rentalBasis for each customer
    customer1.rentalBasis = 1 # hourly
    customer2.rentalBasis = 1 # hourly
    customer3.rentalBasis = 2 # daily
    customer4.rentalBasis = 2 # daily
    customer5.rentalBasis = 3 # weekly
    customer6.rentalBasis = 3 # weekly
    customer7.rentalBasis = 4 # monthly
    customer8.rentalBasis = 4 # monthly

    # create valid cars for each customer
    customer1.cars = 1
    customer2.cars = 5 
    customer3.cars = 2
    customer4.cars = 8 
    customer5.cars = 15
    customer6.cars = 30
    customer7.cars = 4
    customer8.cars = 10

    # create past valid rental times for each customer
    
    customer1.rentalTime = datetime.now() + timedelta(hours=-4)
    customer2.rentalTime = datetime.now() + timedelta(hours=-23)
    customer3.rentalTime = datetime.now() + timedelta(days=-4)
    customer4.rentalTime = datetime.now() + timedelta(days=-13)
    customer5.rentalTime = datetime.now() + timedelta(weeks=-6)
    customer6.rentalTime = datetime.now() + timedelta(weeks=-12)
    customer7.rentalTime = datetime.now() + timedelta(weeks=-8)
    customer8.rentalTime = datetime.now() + timedelta(weeks=16)

    # make all customers return their cars
    request1 = customer1.returnCar()
    request2 = customer2.returnCar()
    request3 = customer3.returnCar()
    request4 = customer4.returnCar()
    request5 = customer5.returnCar()
    request6 = customer6.returnCar()
    request7 = customer7.returnCar()
    request8 = customer8.returnCar()

    # check if all of them get correct bill
    assert shop.returnCar(request1) == 80
    assert shop.returnCar(request2) == 2300
    assert shop.returnCar(request3) == 1200
    assert shop.returnCar(request4) == 15600
    assert shop.returnCar(request5) == 58500
    assert shop.returnCar(request6) == 234000
    assert shop.returnCar(request7) == 58500
    assert shop.returnCar(request8) == 234000

def test_returnCar_with_valid_input(self):
    # create a customer
    customer = Customer()

    # create valid rentalTime, rentalBasis, cars
    now = datetime.now()
    customer.rentalTime = now
    customer.rentalBasis = 1
    customer.cars = 4

    assert customer.returnCar() == (now, 1, 4)

def test_returnCar_with_invalid_input(self):
    # create a customer
    customer = Customer()

    # create valid rentalBasis and cars

    customer.rentalBasis = 1
    customer.cars = 0

    # create invalid rentalTime
    customer.rentalTime = 0
    assert customer.returnCar() == (0, 0, 0)
