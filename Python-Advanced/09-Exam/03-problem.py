# 03. Problem
from collections import deque


def stock_availability(inventory_list, command, *args):
    # new_list = deque(inventory_list)
    # new_list = inventory_list
    args = list(args)
    # if len(args) == 1:
    #     try:
    #         args_list = list(map(int, args))
    #     except:
    #         args_list = list(args)

    if command == 'delivery':
        assert len(args) > 0
        inventory_list += list(args)
    elif command == 'sell':
        # assert 0 <= len(args) <= 1
        if len(args) == 0:
            inventory_list.pop(0)
        elif len(args) == 1 and type(args[0]) == int:
            for _ in range(args[0]):
                inventory_list.pop(0)
        elif len(args) >= 1:
            for cupcake in args:
                if is_order_valid(inventory_list, cupcake):
                    inventory_list = remove_cupcakes(inventory_list, cupcake)

    return list(inventory_list)


def remove_cupcakes(inventory_list, cupcake):
    res = [i for i in inventory_list if i != cupcake]
    return res


def is_order_valid(inventory, order):
    if order in inventory:
        return True
    return False


# Test Code
print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))