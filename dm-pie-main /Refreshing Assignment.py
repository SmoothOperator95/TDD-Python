class Drink:
    # Class-level data for valid bases and flavors
    VALID_BASES = ['water', 'sbrite', 'pokeacola', 'Mr. Salt', 'hill fog', 'leaf wine']
    VALID_FLAVORS = ['lemon', 'cherry', 'strawberry', 'mint', 'blueberry', 'lime']
    
    def __init__(self, base):
        if base not in Drink.VALID_BASES:
            raise ValueError(f"Invalid base. Valid bases are: {', '.join(Drink.VALID_BASES)}")
        
        self._base = base
        self._flavors = set()  # Use a set to automatically handle duplicate flavors
        
    # Getter methods
    def get_base(self):
        return self._base
    
    def get_flavors(self):
        return list(self._flavors)
    
    def get_num_flavors(self):
        return len(self._flavors)
    
    # Accessor methods
    def set_flavors(self, flavors):
        """Set the flavors for the drink. Ignores duplicates automatically."""
        if not all(f in Drink.VALID_FLAVORS for f in flavors):
            raise ValueError(f"Invalid flavor(s). Valid flavors are: {', '.join(Drink.VALID_FLAVORS)}")
        
        self._flavors = set(flavors)  # Automatically removes duplicates
    
    def add_flavor(self, flavor):
        """Add a single flavor to the drink, if it's valid and not already added."""
        if flavor not in Drink.VALID_FLAVORS:
            raise ValueError(f"Invalid flavor. Valid flavors are: {', '.join(Drink.VALID_FLAVORS)}")
        
        self._flavors.add(flavor)


class Order:
    def __init__(self):
        self._items = []
    
    # Getter methods
    def get_items(self):
        return self._items
    
    def get_total(self):
        # Let's assume a simple pricing scheme for now (example: base price + $1 per flavor)
        total = 0
        for item in self._items:
            total += 5  # Base price for the drink
            total += item.get_num_flavors()  # $1 per flavor
        return total
    
    def get_num_items(self):
        return len(self._items)
    
    def get_receipt(self):
        receipt = []
        for item in self._items:
            base = item.get_base()
            flavors = ', '.join(item.get_flavors()) if item.get_flavors() else 'No flavors'
            receipt.append(f"{base} with {flavors}")
        return "\n".join(receipt)
    
    # Accessor methods
    def add_item(self, drink):
        """Add a drink item to the order."""
        if not isinstance(drink, Drink):
            raise ValueError("Only Drink objects can be added to the order")
        self._items.append(drink)
    
    def remove_item(self, index):
        """Remove a drink item from the order by index."""
        if index < 0 or index >= len(self._items):
            raise IndexError("Index out of range")
        del self._items[index]


# Example Usage

# Create drinks
drink1 = Drink(base='water')
drink1.add_flavor('lemon')
drink1.add_flavor('mint')

drink2 = Drink(base='sbrite')
drink2.set_flavors(['cherry', 'blueberry'])

# Create an order
order = Order()

# Add drinks to the order
order.add_item(drink1)
order.add_item(drink2)

# Get receipt and total
print(order.get_receipt())  # Receipt of all items
print(f"Total: ${order.get_total()}")  # Total price

# Remove a drink
order.remove_item(0)

# New receipt and total after removal
print(order.get_receipt())
print(f"Total: ${order.get_total()}")