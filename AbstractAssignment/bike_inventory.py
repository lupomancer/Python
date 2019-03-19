#!/usr/bin/env python3
#
# BikeInventory Class
#
# Cody Sayer and William Prout
#
# Ver 1.2
from electric_bike import ElectricBike
from motor_bike import MotorBike
from abstract_bike import AbstractBike


_bikes = []
bike_inventory_list = []


def add(bike):
    """adds a bike to the list of bikes
    
    Arguments:
        bike {list} -- a list of bike components
    """

    _bikes.append(bike)
    bike_part_list = AbstractBike(bike[0], bike[1], bike[2], bike[3], bike[4], bike[5], bike[6], bike[7], bike[8], bike[9])
    bike_inventory_list.append(bike_part_list)



def get(id):
    """returns a list of bike stats based on ID
    
    Arguments:
        id {int} -- bike ID
    
    Returns:
        list -- list of bike components
    """

    bikes = []
    for bike in _bikes:
        if bike[0] == id:
            bikes.append(bike)
            return bike
        else:
            pass
    if len(bikes) == []:
        raise(Exception)
        



def get_all():
    """returns all bikes in a list
    """

    all_bikes = []
    i = 0
    while i < len(bike_inventory_list):
        id = bike_inventory_list[i].get_id()
        manufacturer = bike_inventory_list[i].get_manufacturer()
        model = bike_inventory_list[i].get_model()
        year = bike_inventory_list[i].get_year()
        price = bike_inventory_list[i].get_price()
        wheel_size = bike_inventory_list[i].get_wheel_size()
        details = bike_inventory_list[i].get_details()
        all_bikes.append([id, manufacturer, model, year, price, wheel_size, details[0], details[1], details[2], details[3]])
        i += 1

    if len(all_bikes) > 0:
        return(all_bikes)
    else:
        return(None)



def get_all_by_category(category):
    """returns all bikes of a certain category
    
    Arguments:
        category {string} -- bike type
    """

    category_bikes = []

    all = get_all()
    for bike in all:
        if bike[6] == category:
            category_bikes.append(bike)


    if len(category_bikes) > 0:
        print(category_bikes)
    else:
        print("There are no bikes in category %s" % (category))



def update(bike):
    """updates a bike in the list with new information entered
    
    Arguments:
        bike {list} -- list of bike components
    """

    all = get_all()
    for existing_bike in all:
        if bike[0] == existing_bike[0]:
            delete(bike_inventory_list[0])
            add(bike)
    raise(Exception)



def delete(id):
    """removes a bike based on ID
    
    Arguments:
        id {int} -- bike ID
    """

    all = get_all()
    i=0
    for bike in all:
        if bike[0] == id:
            del bike_inventory_list[i]
            return
        i += 1
    raise(Exception)



def main():
    """runs all commands and prints outputs
    """

    bike1 = [100, 'norco', 'hardrock', 2006, 350, 26, 'Electric Bike', 75, 'stepper', 15]
    bike2 = [101, 'norco', 'bigfoot', 2006, 500, 22, 'Electric Bike', 80, 'brushless', 20]
    bike3 = [102, 'harley', 'panhead', 1998, 2000, 24, 'Motorbike', 20, 4, True]
    bike4 = [103, 'harley', 'the other one', 1969, 5000, 24, 'Motorbike', 20, 4, False]
    add(bike1)
    add(bike2)
    add(bike3)
    add(bike4)

    print()
    if get(100)[6] == 'Electric Bike':
        print("The bike with id %d is an %s, is a %s %s, was made in %d, has %d inch wheels, has a battery capacity of %d kWh, uses a %s motor, and has a %d inch hub." % (
            get(100)[0], get(100)[6], get(100)[1], get(100)[2], get(100)[3], get(100)[5], get(100)[7], get(100)[8], get(100)[9]))
    elif get(100)[6] == 'Motorbike':
        if get(100)[9] == True:
            street_legal_status = 'street legal'
        else:
            street_legal_status = 'not street legal'
        print("The bike with id %d is an %s, is a %s %s, was made in %d, has %d inch wheels, has a fuel capacity of %d litres, has an engine displacement of %d litres, and is %s." % (
            get(100)[0], get(100)[6], get(100)[1], get(100)[2], get(100)[3], get(100)[5], get(100)[7], get(100)[8], street_legal_status))
    print()
    if get(101)[6] == 'Electric Bike':
        print("The bike with id %d is an %s, is a %s %s, was made in %d, has %d inch wheels, has a battery capacity of %d kWh, uses a %s motor, and has a %d inch hub." % (
            get(101)[0], get(101)[6], get(101)[1], get(101)[2], get(101)[3], get(101)[5], get(101)[7], get(101)[8], get(101)[9]))
    elif get(101)[6] == 'Motorbike':
        if get(101)[9] == True:
            street_legal_status = 'street legal'
        else:
            street_legal_status = 'not street legal'
        print("The bike with id %d is an %s, is a %s %s, was made in %d, has %d inch wheels, has a fuel capacity of %d litres, has an engine displacement of %d litres, and is %s." % (
            get(101)[0], get(101)[6], get(101)[1], get(101)[2], get(101)[3], get(101)[5], get(101)[7], get(101)[8], street_legal_status))
    print()
    if get(102)[6] == 'Electric Bike':
        print("The bike with id %d is an %s, is a %s %s, was made in %d, has %d inch wheels, has a battery capacity of %d kWh, uses a %s motor, and has a %d inch hub." % (
            get(102)[0], get(102)[6], get(102)[1], get(102)[2], get(102)[3], get(102)[5], get(102)[7], get(102)[8], get(102)[9]))
    elif get(102)[6] == 'Motorbike':
        if get(102)[9] == True:
            street_legal_status = 'street legal'
        else:
            street_legal_status = 'not street legal'
        print("The bike with id %d is an %s, is a %s %s, was made in %d, has %d inch wheels, has a fuel capacity of %d litres, has an engine displacement of %d litres, and is %s." % (
            get(102)[0], get(102)[6], get(102)[1], get(102)[2], get(102)[3], get(102)[5], get(102)[7], get(102)[8], street_legal_status))
    print()
    if get(103)[6] == 'Electric Bike':
        print("The bike with id %d is an %s, is a %s %s, was made in %d, has %d inch wheels, has a battery capacity of %d kWh, uses a %s motor, and has a %d inch hub." % (
            get(103)[0], get(103)[6], get(103)[1], get(103)[2], get(103)[3], get(103)[5], get(103)[7], get(103)[8], get(103)[9]))
    elif get(103)[6] == 'Motorbike':
        if get(103)[9] == True:
            street_legal_status = 'street legal'
        else:
            street_legal_status = 'not street legal'
        print("The bike with id %d is an %s, is a %s %s, was made in %d, has %d inch wheels, has a fuel capacity of %d litres, has an engine displacement of %d litres, and is %s." % (
            get(103)[0], get(103)[6], get(103)[1], get(103)[2], get(103)[3], get(103)[5], get(103)[7], get(103)[8], street_legal_status))
    print()

    print("The list of all bike stats are as follows:")
    print(get_all())
    print()
    print()
    print('All bikes in category Electric Bike are as follows:')
    get_all_by_category('Electric Bike')
    print()
    print('Deleteing bike with ID of 100')
    delete(100)
    print()
    print("Printing all bikes once more")
    print(get_all())
    print()
    
if __name__ == "__main__":
    main()
