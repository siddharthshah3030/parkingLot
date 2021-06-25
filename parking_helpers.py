from parking import *

# generating instance of parking lot
parking_lot = parking()


def create_new_parking_lot(query):
    size = query[1]
    parking_lot.create(int(size))
    print(f"Created parking of {int(size)} slots")


def park_car(query):
    plate = query[1]
    age = query[3]
    slot_parked = parking_lot.park(plate, int(age))
    if (slot_parked == None):
        print(
            f"Parking lot is fully occupied and vehicle {plate} cannot be parked")
    else:
        print(
            f'Car with vehicle registration number "{plate}" has been parked at slot number {slot_parked}')


def get_slot_numbers_from_plates(query):
    plate = query[1]
    slots = parking_lot.slots_from_plate(plate)
    if(len(slots) == 0):
        print(
            f"no vehicle with the license plate {plate} exists in the parking lot")
    else:
        print(*slots)


def get_slot_numbers_from_age(query):
    age = query[1]
    slots = parking_lot.slots_from_age(int(age))
    if(len(slots) == 0):
        print(
            f"no vehicles of drivers with the age {age} exists in the parking lot")
    else:
        print(*slots)


def remove_car(query):
    slot_number = query[1]
    car_details = parking_lot.empty_slot(int(slot_number)-1)
    if car_details == None:
        print(f"slot {slot_number} is already empty")
    else:
        print(
            f'Slot number {int(slot_number)} vacated, the car with vehicle registration number "{car_details.plate}" left the space, the driver of the car was of age {car_details.age}')


def get_plates_from_age(query):
    age = query[1]
    slots = parking_lot.plates_from_age(int(age))
    if(len(slots) == 0):
        print(
            f"no vehicles of drivers with the age {age} exists in the parking lot")
    else:
        print(*slots)


def execute(query):
    query = query.split(" ")
    if query[0] == "Create_parking_lot":
        create_new_parking_lot(query)
    elif query[0] == "Park":
        park_car(query)
    elif query[0] == "Slot_numbers_for_driver_of_age":
        get_slot_numbers_from_age(query)
    elif query[0] == "Slot_number_for_car_with_number":
        get_slot_numbers_from_plates(query)
    elif query[0] == "Vehicle_registration_number_for_driver_of_age":
        get_plates_from_age(query)
    elif query[0] == "Leave":
        remove_car(query)
    else:
        warnings.warn(
            'Execution of a query failed, query is - ""' + ''.join(query)+'""')
