import unittest
import shippingCost

class TestShippingCost(unittest.TestCase):
    #first test case
    def test_shippingCostA(self):
        result = shippingCost.calculateCost(11)
        self.assertEqual(result, 4.75)

    # Test case for weight greater than 6 but less or equal to 10
    def test_shippingCostB(self):
        result = shippingCost.calculateCost(7)
        self.assertEqual(result, 4.00)
    
    # Test case for weight greater than 2 but less or equal to 6
    def test_shippingCostC(self):
        result = shippingCost.calculateCost(3)
        self.assertEqual(result, 3.00)

    # Test case for weight less or equal to 2
    def test_shippingCostD(self):
        result = shippingCost.calculateCost(1)
        self.assertEqual(result, 1.50)

            
#run with python -m unittest test_shippingCost.py
