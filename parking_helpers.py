from parking import *

# generating instance of parking lot
parking_lot = parking()

def create_new_parking_lot(query):
  parking_lot.create(int(query[1]))
  print(f"Created parking of {int(query[1])} slots")

def park_car(query):
  slot_parked = parking_lot.park(query[1],int(query[3]))
  if (slot_parked==None):
    print(f"Parking lot is fully occupied and vehicle {query[1]} cannot be parked")
  else:
    print(f'Car with vehicle registration number "{query[1]}" has been parked at slot number {slot_parked}')

def get_slot_numbers_from_plates(query):
  slots = parking_lot.slots_from_plate(query[1])
  if(len(slots)==0):
    print(f"no vehicle with the license plate {query[1]} exists in the parking lot")
  else:
    print(slots)
  
def get_slot_numbers_from_age(query):
  slots = parking_lot.slots_from_age(int(query[1]))
  if(len(slots)==0):
    print(f"no vehicles of drivers with the age {query[1]} exists in the parking lot")
  else:
    print(slots)

def remove_car(query):
  car_details = parking_lot.empty_slot(int(query[1]))
  if car_details==None :
    print(f"slot {queryp[1]} is already empty")
  else:
    print(f'Slot number {int(query[1])} vacated, the car with vehicle registration number "{car_details["plate"]}" left the space, the driver of the car was of age {car_details["age"]}')

  
def get_plates_from_age(query):
  slots = parking_lot.plates_from_age(int(query[1]))
  if(len(slots)==0):
    print(f"no vehicles of drivers with the age {query[1]} exists in the parking lot")
  else:
    print(slots)


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
    print("Invalid query format, please check") 
  