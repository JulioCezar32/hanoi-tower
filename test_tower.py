from pin import Pin
from ring import Ring
from tower import Tower
import unittest

SIZE_DOES_NOT_MATTER = 1

class TestTower(unittest.TestCase):
    def test_initialize_tower_with_three_pins(self):
        tower = Tower(SIZE_DOES_NOT_MATTER)

        number_of_pins = len(tower.pins)

        self.assertEqual(number_of_pins, 3)

    def test_initialize_tower_with_three_rings(self):
        tower = Tower(3)

        pinOne = tower.pins[0]
        number_of_rings = len(pinOne.get_rings())

        self.assertEqual(number_of_rings, 3)

    def test_remove_a_ring_from_the_pin_one_and_insert_into_pin_two(self):
        tower = Tower(3)

        tower.next_step()
        pinTwo = tower.pins[1]
        number_of_rings = len(pinTwo.get_rings())

        self.assertEqual(number_of_rings, 1)

    def test_move_ring(self):
        tower = Tower(3)

        tower.move_ring(1, 2)
        pinTwo = tower.pins[1]
        number_of_rings = len(pinTwo.get_rings())

        self.assertEqual(number_of_rings, 1)
if __name__ =='__main__':
    unittest.main()
