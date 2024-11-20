import unittest
from enum import Enum
from your_module import Size, Flavor, Drink

class TestDrink(unittest.TestCase):
    """Unit tests for the Drink class."""
    
    def setUp(self):
        """
        Set up for the test cases.
        
        Initializes two Drink objects with different sizes and flavors for testing.
        """
        self.drink1 = Drink(name="Hill Fog", size=Size.LARGE, flavor=Flavor.LEMON)
        self.drink2 = Drink(name="Mr. Salt", size=Size.MEGA, flavor=Flavor.ORANGE)
    
    def test_get_size(self):
        """Test the get_size method of the Drink class."""
        # Ensure that the correct size is returned for each drink
        self.assertEqual(self.drink1.get_size(), Size.LARGE)
        self.assertEqual(self.drink2.get_size(), Size.MEGA)

    def test_set_size(self):
        """Test the set_size method of the Drink class."""
        # Update drink1's size to SMALL and verify it
        self.drink1.set_size(Size.SMALL)
        self.assertEqual(self.drink1.get_size(), Size.SMALL)
    
    def test_get_total(self):
        """Test the get_total method of the Drink class."""
        # Verify the total price of each drink based on size and flavor
        self.assertEqual(self.drink1.get_total(), 2.05)  # Size.LARGE and no flavor
        self.assertEqual(self.drink2.get_total(), 2.30)  # Size.MEGA and flavor added

    def test_repr(self):
        """Test the __repr__ method of the Drink class."""
        # Check that the string representation of each drink is formatted correctly
        self.assertEqual(repr(self.drink1), "Hill Fog (Large) with Lemon")
        self.assertEqual(repr(self.drink2), "Mr. Salt (Mega) with Orange")

    def test_cost_property(self):
        """Test the cost property of the Drink class."""
        # Ensure that the cost property returns the correct value
        self.assertEqual(self.drink1.cost, 2.05)
        self.assertEqual(self.drink2.cost, 2.30)

if __name__ == '__main__':
    unittest.main()

import unittest
from your_module import Drink, Size, Flavor, Order

class TestOrder(unittest.TestCase):
    """Unit tests for the Order class."""
    
    def setUp(self):
        """
        Set up for the test cases.
        
        Initializes two Drink objects and adds them to an Order object for testing.
        """
        self.drink1 = Drink(name="Hill Fog", size=Size.LARGE, flavor=Flavor.LEMON)
        self.drink2 = Drink(name="Mr. Salt", size=Size.MEGA, flavor=Flavor.ORANGE)
        self.order = Order()
        self.order.add_drink(self.drink1)  # Adding drink1 to the order
        self.order.add_drink(self.drink2)  # Adding drink2 to the order
    
    def test_get_total(self):
        """Test the get_total method of the Order class."""
        # Ensure that the total of the order is calculated correctly, including tax
        self.assertEqual(self.order.get_total(), 4.83)  # 4.50 subtotal + 0.33 tax
    
    def test_get_receipt(self):
        """Test the get_receipt method of the Order class."""
        # Verify that the receipt is formatted as expected, with all details included
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