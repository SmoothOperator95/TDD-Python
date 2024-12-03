class Drink:
    def __init__(self, drink_type: str, price: float):
        self.drink_type = drink_type
        self.price = price
        self.toppings = []

    def get_price(self):
        return self.price

    def set_price(self, price: float):
        self.price = price

    def add_topping(self, topping: str):
        self.toppings.append(topping)

    def get_toppings(self):
        return self.toppings

    def get_drink_type(self):
        return self.drink_type

    def __str__(self):
        toppings = ', '.join(self.toppings) if self.toppings else 'None'
        return f"{self.drink_type}: ${self.price:.2f} with toppings: {toppings}"

class Food:
    FOOD_PRICES = {
        'Hotdog': 2.30,
        'Corndog': 2.00,
        'Ice Cream': 3.00,
        'Onion Rings': 1.75,
        'French Fries': 1.50,
        'Tater Tots': 1.70,
        'Nacho Chips': 1.90
    }

    TOPPING_PRICES = {
        'Cherry': 0.00,
        'Whipped Cream': 0.00,
        'Caramel Sauce': 0.50,
        'Chocolate Sauce': 0.50,
        'Nacho Cheese': 0.30,
        'Chili': 0.60,
        'Bacon Bits': 0.30,
        'Ketchup': 0.00,
        'Mustard': 0.00
    }

    def __init__(self, food_type: str):
        self.food_type = food_type
        if food_type in Food.FOOD_PRICES:
            self.price = Food.FOOD_PRICES[food_type]
        else:
            raise ValueError(f"Unknown food type: {food_type}")
        self.toppings = []

    def get_price(self):
        # Add topping price to base price
        toppings_cost = sum(Food.TOPPING_PRICES[topping] for topping in self.toppings)
        return self.price + toppings_cost

    def add_topping(self, topping: str):
        if topping in Food.TOPPING_PRICES:
            self.toppings.append(topping)
        else:
            raise ValueError(f"Unknown topping: {topping}")

    def get_toppings(self):
        return self.toppings

    def get_food_type(self):
        return self.food_type

    def __str__(self):
        toppings = ', '.join(self.toppings) if self.toppings else 'None'
        return f"{self.food_type}: ${self.get_price():.2f} with toppings: {toppings}"

class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        return sum(item.get_price() for item in self.items)

    def generate_receipt(self):
        receipt = "\nReceipt\n--------\n"
        for item in self.items:
            receipt += f"{item}\n"
        receipt += f"\nTotal: ${self.calculate_total():.2f}"
        return receipt

import unittest

class TestOrderSystem(unittest.TestCase):

    def test_drink_creation(self):
        drink = Drink("Coke", 1.50)
        self.assertEqual(drink.get_drink_type(), "Coke")
        self.assertEqual(drink.get_price(), 1.50)
        drink.set_price(1.75)
        self.assertEqual(drink.get_price(), 1.75)

    def test_drink_toppings(self):
        drink = Drink("Coke", 1.50)
        drink.add_topping("Whipped Cream")
        self.assertIn("Whipped Cream", drink.get_toppings())
        self.assertEqual(drink.get_price(), 1.50)  # Toppings don't affect the price in this case

    def test_food_creation(self):
        food = Food("Hotdog")
        self.assertEqual(food.get_food_type(), "Hotdog")
        self.assertEqual(food.get_price(), 2.30)

    def test_food_toppings(self):
        food = Food("French Fries")
        food.add_topping("Nacho Cheese")
        self.assertEqual(food.get_price(), 1.80)  # Base price (1.50) + Nacho Cheese (0.30)

    def test_order_creation(self):
        order = Order()
        drink = Drink("Coke", 1.50)
        food = Food("Hotdog")
        order.add_item(drink)
        order.add_item(food)
        self.assertEqual(order.calculate_total(), 2.30 + 1.50)
        self.assertIn("Hotdog: $2.30", order.generate_receipt())
        self.assertIn("Coke: $1.50", order.generate_receipt())

    def test_receipt_generation(self):
        order = Order()
        drink = Drink("Coke", 1.50)
        food = Food("French Fries")
        food.add_topping("Nacho Cheese")
        order.add_item(drink)
        order.add_item(food)
        receipt = order.generate_receipt()
        self.assertIn("Coke: $1.50", receipt)
        self.assertIn("French Fries: $1.80", receipt)
        self.assertIn("Total: $3.30", receipt)

if __name__ == "__main__":
    unittest.main()

##Run: python -m unittest test_file_name.py##