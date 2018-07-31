from ring import Ring

class Pin:
    def __init__(self):
        self.rings = []

    def insert_ring(self, ring):
        if self.verify_the_inserted_ring(ring):
            self.rings.append(ring)
        else:
            raise ValueError


    def verify_the_inserted_ring(self, ring):
        if self.pin_is_void():
            return True
        elif self.exist_a_smaller_ring_on_the_pin(ring):
            return True
        else:
            return False


    def remove_ring(self):
        return self.rings.pop()

    def exist_a_smaller_ring_on_the_pin(self, ring):
        last_ring_on_pin = self.rings[-1]
        return ring.size < last_ring_on_pin.size

    def pin_is_void(self):
        result = (self.rings == [])
        return result

    def __str__(self):
        number_of_rings = len(self.rings)
        for line in range(0, number_of_rings):
            number_of_space = number_of_rings - line
            print(number_of_space* ' '  + line * '-' + '|' + line*'-' + number_of_space* ' ')
