import unittest

from ring import Ring

class TestRing(unittest.TestCase):

    def test_ring_size(self):
        ring = Ring(1)

        self.assertEqual(str(ring), '1')

if __name__ == '__main__':
    unittest.main()
