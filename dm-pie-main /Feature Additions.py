from enum import Enum

class Size(Enum):
    SMALL = "Small"
    MEDIUM = "Medium"
    LARGE = "Large"
    MEGA = "Mega"

class Flavor(Enum):
    LEMON = "Lemon"
    ORANGE = "Orange"
    STRAWBERRY = "Strawberry"
    MANGO = "Mango"
    BLUEBERRY = "Blueberry"
    VANILLA = "Vanilla"
    CHOCOLATE = "Chocolate"

class Drink:
    SIZE_COSTS = {
        Size.SMALL: 1.50,
        Size.MEDIUM: 1.75,
        Size.LARGE: 2.05,
        Size.MEGA: 2.15
    }

    FLAVOR_COST = 0.15

    def __init__(self, name, size: Size, flavor: Flavor = None):
        self.name = name
        self.size = size
        self.flavor = flavor

    def get_size(self):
        return self.size

    def set_size(self, size: Size):
        self.size = size

    def get_total(self):
        total = self.SIZE_COSTS[self.size]
        if self.flavor:
            total += self.FLAVOR_COST
        return total

    def __repr__(self):
        description = f"{self.name} ({self.size.value})"
        if self.flavor:
            description += f" with {self.flavor.value}"
        return description

    # Dynamically calculate the cost for the drink
    @property
    def cost(self):
        return self.get_total()

class Order:
    TAX_RATE = 0.0725  # 7.25% tax

    def __init__(self):
        self.drinks = []

    def add_drink(self, drink: Drink):
        self.drinks.append(drink)

    def get_total(self):
        subtotal = sum(drink.get_total() for drink in self.drinks)
        tax = subtotal * self.TAX_RATE
        return subtotal + tax

    def get_receipt(self):
        receipt_lines = []
        subtotal = 0
        for drink in self.drinks:
            drink_total = drink.get_total()
            receipt_lines.append(f"{drink}: ${drink_total:.2f}")
            subtotal += drink_total
        tax = subtotal * self.TAX_RATE
        total = subtotal + tax
        receipt_lines.append(f"Subtotal: ${subtotal:.2f}")
        receipt_lines.append(f"Tax (7.25%): ${tax:.2f}")
        receipt_lines.append(f"Total: ${total:.2f}")
        return "\n".join(receipt_lines)

# Create some drinks
drink1 = Drink(name="Hill Fog", size=Size.LARGE, flavor=Flavor.LEMON)
drink2 = Drink(name="Mr. Salt", size=Size.MEGA, flavor=Flavor.ORANGE)

# Create an order and add drinks
order = Order()
order.add_drink(drink1)
order.add_drink(drink2)

# Get the total and receipt
print(order.get_receipt())

Hill Fog (Large) with Lemon: $2.20
Mr. Salt (Mega) with Orange: $2.30
Subtotal: $4.50
Tax (7.25%): $0.33
Total: $4.83