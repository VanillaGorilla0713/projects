# Basic Inventory app for fantasy text game

from collections import Counter


def displayInventory(inventory):
    print("Inventory:")
    for key, value in inventory.items():
        print(str(value) + ' ' + key)
        
    print("Total number of items: " + str(sum(my_stuff.values())))
    print()


def addToInventory(inventory, addItems):
    for item in addItems:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory


def addToInventory2(inventory, addItems):
    inventory.update(addItems)


if __name__ == "__main__":
    # inventory vairable for first and second functions
    my_stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    # inventory variables for third function using an alternative to second function 
    my_inv = Counter({'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12})
    # dragon items that will be added to inventory
    dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

    # display inventory for first func
    displayInventory(my_stuff)
    # adds inventory for second func
    addToInventory(my_stuff, dragonLoot)
    # display inventory for second func
    displayInventory(my_stuff)
    # add inventory for third func
    addToInventory2(my_inv, dragonLoot)
    # display inventory for third func
    displayInventory(my_inv)
