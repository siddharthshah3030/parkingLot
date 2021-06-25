import unittest
from parking import *

class TestParking(unittest.TestCase):
    
    def test_create_new_parking_lot(self):
        parking_lot = parking()
        parking_lot.create(3)
        self.assertEqual(3,len(parking_lot.slots))


    def test_park_car(self):
        parking_lot = parking()
        parking_lot.create(3)
        slot_parked = parking_lot.park("HH-HH",int(2))
        self.assertEqual(slot_parked,not None )


    def test_parking_lot_is_full(self):
        parking_lot = parking()
        parking_lot.create(1)
        slot_parked = parking_lot.park("HH-HH",int(2))
        slot_parked = parking_lot.park("HH-HH",int(2))
        self.assertEqual(slot_parked,  None )


    def test_slot_from_plates(self):
        parking_lot = parking()
        parking_lot.create(1)
        parking_lot.park("HH-HH",int(2))
        slots = parking_lot.slots_from_plate("HH-HH")
        self.assertEqual(len(slots),  1 )
        


    def test_slot_from_age(self):
        parking_lot = parking()
        parking_lot.create(1)
        parking_lot.park("HH-HH",int(2))
        slots = parking_lot.slots_from_age(2)
        self.assertEqual(len(slots),  1 )
        

    def test_plates_from_age(self):
        parking_lot = parking()
        parking_lot.create(1)
        parking_lot.park("HH-HH",int(2))
        slots = parking_lot.plates_from_age(2)
        self.assertEqual(len(slots),  1 )


    def test_leave_occupied_slot(self):
        parking_lot = parking()
        parking_lot.create(1)
        parking_lot.park("HH-HH",int(2))
        slot_emptied = parking_lot.empty_slot(0)
        self.assertEqual(slot_emptied.plate, "HH-HH")
        

    def test_leave_empty_slot(self):
        parking_lot = parking()
        parking_lot.create(4)
        parking_lot.park("HH-HH",int(2))
        slot_emptied = parking_lot.empty_slot(2)
        self.assertEqual(slot_emptied, None )


if __name__ == '__main__':
    unittest.main()