# 06. Inventory

class Inventory:
    def __init__(self, capacity):
        self._capacity = capacity
        self.items = []

    def add_item(self, item):
        if self._capacity:
            self.items.append(item)
            self._capacity -= 1
        else:
            return "not enough room in the inventory"

    def get_capacity(self):
        return len(self.items)

    def __repr__(self):
        return f"Items: {', '.join(self.items)}.\nCapacity left: {self._capacity}"


# test code
"""
inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
inventory.add_item("bottle")
print(inventory.get_capacity())
print(inventory)
"""