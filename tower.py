from ring import Ring
from pin import Pin

NUMBER_OF_PINS = 4

class Tower(Ring, Pin):
    def __init__(self, number_of_rings):
        self._registrator = number_of_rings
        self.set_pins()
        self.set_rings(number_of_rings)
        self.run(self._registrator, 1, 3, 2)
        #All Rings Should be initilized inside the pinOne

    def set_pins(self):
        pinOne = Pin()
        pinTwo = Pin()
        pinThree = Pin()
        self.pins = [pinOne, pinTwo, pinThree]

    def set_rings(self, number_of_rings):
        RING_RANGE = range(number_of_rings + 1, 1, -1)
        pinOne = self.pins[0]
        for ring_size in RING_RANGE:
            ring = Ring(ring_size)
            pinOne.insert_ring(ring)

    def move_ring(self, remove, insert):
        removed_pin = self.pins[remove - 1]
        inserted_pin = self.pins[insert - 1]

        moving_ring = removed_pin.remove_ring()
        inserted_pin.insert_ring(moving_ring)

    def run(self, number_of_ring, origin, destination, auxiliary):

        if(number_of_ring > 0):
            self.run(number_of_ring - 1 , origin, auxiliary, destination)
            self.move_ring(origin, destination)
        #    print("DISCO {} MOVIDO DO PINO {} PARA O PINO {}".format(number_of_ring, auxiliary, destination))
            self.run(number_of_ring -1, auxiliary, destination, origin)
