import unittest
from enum import Enum
from your_module import Size, Flavor, Drink

class TestDrink(unittest.TestCase):

    def setUp(self):
        """Set up for the test cases."""
        self.drink1 = Drink(name="Hill Fog", size=Size.LARGE, flavor=Flavor.LEMON)
        self.drink2 = Drink(name="Mr. Salt", size=Size.MEGA, flavor=Flavor.ORANGE)
    
    def test_get_size(self):
        """Test the get_size method."""
        self.assertEqual(self.drink1.get_size(), Size.LARGE)
        self.assertEqual(self.drink2.get_size(), Size.MEGA)

    def test_set_size(self):
        """Test the set_size method."""
        self.drink1.set_size(Size.SMALL)
        self.assertEqual(self.drink1.get_size(), Size.SMALL)
    
    def test_get_total(self):
        """Test the get_total method."""
        self.assertEqual(self.drink1.get_total(), 2.05)  # Size.LARGE and no flavor
        self.assertEqual(self.drink2.get_total(), 2.30)  # Size.MEGA and flavor added

    def test_repr(self):
        """Test the __repr__ method."""
        self.assertEqual(repr(self.drink1), "Hill Fog (Large) with Lemon")
        self.assertEqual(repr(self.drink2), "Mr. Salt (Mega) with Orange")

    def test_cost_property(self):
        """Test the cost property."""
        self.assertEqual(self.drink1.cost, 2.05)
        self.assertEqual(self.drink2.cost, 2.30)

if __name__ == '__main__':
    unittest.main()

import unittest
from your_module import Drink, Size, Flavor, Order

class TestOrder(unittest.TestCase):

    def setUp(self):
        """Set up for the test cases."""
        self.drink1 = Drink(name="Hill Fog", size=Size.LARGE, flavor=Flavor.LEMON)
        self.drink2 = Drink(name="Mr. Salt", size=Size.MEGA, flavor=Flavor.ORANGE)
        self.order = Order()
        self.order.add_drink(self.drink1)
        self.order.add_drink(self.drink2)
    
    def test_get_total(self):
        """Test the get_total method."""
        self.assertEqual(self.order.get_total(), 4.83)  # 4.50 subtotal + 0.33 tax
    
    def test_get_receipt(self):
        """Test the get_receipt method."""
        expected_receipt = (
            "Hill Fog (Large) with Lemon: $2.20\n"
            "Mr. Salt (Mega) with Orange: $2.30\n"
            "Subtotal: $4.50\n"
            "Tax (7.25%): $0.33\n"
            "Total: $4.83"
        )
        self.assertEqual(self.order.get_receipt(), expected_receipt)

if __name__ == '__main__':
    unittest.main()
