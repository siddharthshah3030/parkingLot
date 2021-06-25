from parking_helpers import *


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
    print("error") 
  

with open("input.txt") as file:
  queries = file.readlines()
  for query in queries:
    execute(query)

