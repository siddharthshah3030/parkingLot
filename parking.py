"""
Logical parking class
interact via parking_helper.py
"""

class parking:
  def __init__(self):
    self.slots = []

  def create(self,size):
    self.slots = [None]*size

  def park(self,plate,age):
    availableSlot = None
    for i in range(len(self.slots)):
        if self.slots[i] == None:
          availableSlot = i
          break
    if(availableSlot==None):
      return None
    self.slots[availableSlot] = {
      "plate":plate,
      "age":age
    }
    return availableSlot+1

  def slots_from_age(self,age):
    slot_numbers = []
    for index, slot in enumerate(self.slots):
      if (slot and slot["age"]==age):
        slot_numbers.append(index+1)

    return slot_numbers

  def slots_from_plate(self,plate):
    plate = plate.replace("\n", "")
    slot_numbers = []
    for index, slot in enumerate(self.slots):
      if (slot and slot["plate"] == plate):
        slot_numbers.append(index+1)
    return slot_numbers

  def empty_slot(self,slot_number):
    car_details = None
    if(self.slots[slot_number-1]==None): 
      return None
    else:
      car_details = self.slots[slot_number-1]
      self.slots[slot_number-1]= None
    return car_details
    
  def plates_from_age(self,age):
    plate_numbers = []
    for index, slot in enumerate(self.slots):
      if (slot and slot["age"]== age):
      
        plate_numbers.append(slot["plate"])
    return plate_numbers

# create_parking_lot
# parking_lot = parking()
# parking_lot.create_parking_lot(4)
# parking_lot.park_car("sd",34)
# parking_lot.park_car("s22",35)
# parking_lot.park_car("s22",34)
# parking_lot.get_slot_numbers_from_age(34)
# parking_lot.get_slot_numbers_from_age(34)
# parking_lot.get_slot_numbers_from_plates("sd")
# parking_lot.remove_car(2)
# parking_lot.get_plates_from_age(34)