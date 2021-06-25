from parking import *

parking_lot = parking()

def create_new_parking_lot(query):
  parking_lot.create(int(query[1]))
  print(f"Created parking of {query[1]} slots")

def park_car(query):
  slot_parked = parking_lot.park(query[1],int(query[3]))
  print(f'Car with vehicle registration number "{query[1]}" has been parked at slot number {slot_parked}')

def get_slot_numbers_from_plates(query):
  slots = parking_lot.slots_from_plate(query[1])
  print(slots)
  
def get_slot_numbers_from_age(query):
  slots = parking_lot.slots_from_age(int(query[1]))
  print(slots)

def remove_car(query):
  car_details = parking_lot.empty_slot(int(query[1]))
  if car_details==None :print(f"slot {queryp[1]} is already empty")
  print(f'Slot number {query[1]} vacated, the car with vehicle registration number "{car_details["plate"]}" left the space, the driver of the car was of age {car_details["age"]}')

  
def get_plates_from_age(query):
  slots = parking_lot.plates_from_age(int(query[1]))
  
  print(slots)


