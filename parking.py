slots = []


def create_parking_lot(size):
  global slots
  slots = size*[None];


def park(plate,age):
  # i = slots.index(None)
  availableSlot = None
  for i in range(len(slots)):
      if slots[i] == None:
        availableSlot = i
        break

  slots[availableSlot] = {
    "plate":plate,
    "age":age
  }
  print("parked",plate)

def get_slot_numbers_from_age(age):
  slot_numbers = []
  for index, slot in enumerate(slots):
    if (slot and slot["age"]==age):
      slot_numbers.append(index+1)

  print(slot_numbers)

def get_slot_numbers_from_plates(plate):
  slot_numbers = []
  for index, slot in enumerate(slots):
    if (slot and slot["plate"]==plate):
      slot_numbers.append(index+1)
  print(slot_numbers)

def remove_car(slot_number):
  if(slots[slot_number-1]==None): print("Slot already vacant")
  else:
    print("removed car")
    slots[slot_number-1]= None
  
def get_plates_from_age(age):
  plate_numbers = []
  for index, slot in enumerate(slots):
    if (slot and slot["age"]==age):
      plate_numbers.append(slot["plate"])
  print(plate_numbers)


create_parking_lot(45)
# park("sd",34)
# park("s22",35)
# park("s22",34)
# print(slots)
# get_slot_numbers_from_age(34)
# get_slot_numbers_from_age(34)
# get_slot_numbers_from_plates("sd")
# remove_car(2)
# get_plates_from_age(34)