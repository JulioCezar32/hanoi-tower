import unittest
from pin import Pin
from ring import Ring

SIZE_DOES_NOT_MATTER = 1

class TestRingAndPin(unittest.TestCase):
    def test_insert_a_ring_on_the_pin(self):
        pin = Pin()
        ring = Ring(SIZE_DOES_NOT_MATTER)

        pin.insert_ring(ring)
        inserted_rings = pin.get_rings()

        self.assertEqual(inserted_rings, [ring])

    def test_remove_a_ring_from_the_pin(self):
        pin = Pin()
        ring = Ring(SIZE_DOES_NOT_MATTER)

        pin.insert_ring(ring)
        pin.remove_ring()
        existing_rings = pin.get_rings()

        self.assertEqual(existing_rings, [])


    def test_remove_a_ring_from_the_pin_one_and_insert_into_pin_two(self):
        ## rever
        pinOne = Pin()
        pinTwo = Pin()
        ring = Ring(SIZE_DOES_NOT_MATTER)
        pinOne.insert_ring(ring)
        ##pensar em tirar o ring
        

        removed_ring = pinOne.remove_ring()
        pinTwo.insert_ring(ring)
        existing_rings = pinTwo.get_rings()

        self.assertEqual(existing_rings, [ring])

    def test_ring_has_size_one(self):
        ring = Ring(1)

        ring_size = ring.size

        self.assertEqual(ring_size, 1)

    def test_insert_two_rings_with_different_size(self):
        pin = Pin()
        ringOne = Ring(1)
        ringTwo = Ring(2)

        pin.insert_ring(ringTwo)
        pin.insert_ring(ringOne)
        existing_rings = pin.get_rings()

        self.assertEqual(existing_rings, [ringTwo, ringOne])

    def test_remove_only_the_last_ring(self):
        #what is the best name for this test
        pin = Pin()
        ringTwo = Ring(2)
        ringOne = Ring(1)

        pin.insert_ring(ringTwo)
        pin.insert_ring(ringOne)
        removed_ring = pin.remove_ring()
        remaining_rings = pin.get_rings()

        self.assertEqual(removed_ring, ringOne)
        self.assertEqual(remaining_rings, [ringTwo])

    def test_cant_insert_a_greater_ring_on_a_small_ring(self):
        pin = Pin()
        ringOne = Ring(1)
        ringTwo = Ring(2)

        pin.insert_ring(ringOne)

        with self.assertRaises(ValueError):
            pin.insert_ring(ringTwo)

if __name__ == '__main__':
    unittest.main()
