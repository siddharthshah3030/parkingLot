from parking import *

parking_lot = parking()

def create_new_parking_lot(query):
  parking_lot.create(int(query[1]) )

def park_car(query):
  parking_lot.park(query[1],int(query[3]))

def get_slot_numbers_from_plates(query):
  parking_lot.slots_from_plate(query[1])


def get_slot_numbers_from_age(query):
  parking_lot.slots_from_age(int(query[1]))

def remove_car(query):
  parking_lot.empty_slot(int(query[1]))
  
def get_plates_from_age(query):
  parking_lot.plates_from_age(int(query[1]))


