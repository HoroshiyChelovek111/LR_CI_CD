from .car import Car
import unittest

class DefinitelyBrokenTests(unittest.TestCase):
    def test_that_always_fails(self):
        """Этот тест ВСЕГДА падает"""
        self.assertEqual(1, 2, "1 не равно 2!")
        
    def test_another_fail(self):
        """Еще один падающий тест"""
        car = Car("Test", 100)
        # Машина создается с 0 топлива, не может ехать!
        car.drive(10)  # ДОЛЖЕН УПАСТЬ с Exception
