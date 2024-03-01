import unittest
from car import Car


class TestCar(unittest.TestCase):

    def setUp(self):
        self.car = Car()

    def test_initial_speed(self):
        self.assertEqual(self.car.speed, 0)

    def test_initial_odometer(self):
        self.assertEqual(self.car.odometer, 0)

    def test_initial_time(self):
        self.assertEqual(self.car.time, 0)

    def test_accelerate(self):
        self.car.accelerate()
        self.assertEqual(self.car.speed, 5)

    def test_brake(self):
        self.car.brake()
        self.assertEqual(self.car.speed, -5)

    def test_step(self):
        self.car.speed = 10
        self.car.step()
        self.assertEqual(self.car.odometer, 10)
        self.assertEqual(self.car.time, 1)

    def test_average_speed(self):
        self.car.odometer = 100
        self.car.time = 5
        self.assertEqual(self.car.average_speed(), 20)


if __name__ == '__main__':
    unittest.main()
