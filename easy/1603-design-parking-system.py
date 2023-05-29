import unittest


class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.slots_available = {3: small, 2: medium, 1: big}

    def addCar(self, carType: int) -> bool:
        if self.slots_available[carType] > 0:
            self.slots_available[carType] -= 1
            return True
        return False


class TestCase(unittest.TestCase):
    def test_solution(self):
        p = ParkingSystem(1, 1, 0)
        self.assertTrue(p.addCar(1))
        self.assertTrue(p.addCar(2))
        self.assertFalse(p.addCar(3))
        self.assertFalse(p.addCar(1))


if __name__ == "__main__":
    unittest.main()
