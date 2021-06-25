"""

Logical parking class
interact via parking_helper.py

slots = list of all slots of parking lot
slot = {"plate":licensePlate, "age":age}
availableSlotIndex = minimum distance vacant slot available at any moment, None if parking lot is fully occupied

"""


class Vehicle:
    def __init__(self, plate, age):
        self.plate = plate
        self.age = age


class parking:
    def __init__(self):
        self.slots = []
        self.availableSlotIndex = None

    def create(self, size):
        self.slots = [None]*size
        self.availableSlotIndex = 0  # smallest distance vacant slot

    def park(self, plate, age):
        if(self.availableSlotIndex == None):
            return None
        self.slots[self.availableSlotIndex] = Vehicle(plate, age)
        indexFilled = self.availableSlotIndex
        self.availableSlotIndex = None

        # find the next vacant slot
        for i in range(indexFilled, len(self.slots)):
            if self.slots[i] == None:
                self.availableSlotIndex = i
                break

        return indexFilled+1

    def slots_from_age(self, age):
        slot_numbers = []
        for index, slot in enumerate(self.slots):
            if (slot and slot.age == age):
                slot_numbers.append(index+1)

        return slot_numbers

    def slots_from_plate(self, plate):
        plate = plate.replace("\n", "")
        slot_numbers = []
        for index, slot in enumerate(self.slots):
            if (slot and slot.plate == plate):
                slot_numbers.append(index+1)
        return slot_numbers

    def empty_slot(self, indexToRemove):
        car_details = None
        if(self.slots[indexToRemove] == None):
            return None
        else:
            car_details = self.slots[indexToRemove]

            # check the smallest distance available slot
            if (self.availableSlotIndex == None or (indexToRemove < self.availableSlotIndex)):
                self.availableSlotIndex = indexToRemove
            self.slots[indexToRemove] = None
        return car_details

    def plates_from_age(self, age):
        plate_numbers = []
        for index, slot in enumerate(self.slots):
            if (slot and slot.age == age):

                plate_numbers.append(slot.plate)
        return plate_numbers
