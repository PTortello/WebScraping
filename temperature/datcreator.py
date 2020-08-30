"""
datcreator.py
Pedro Tortello - 08/2020
Creates .DAT file containing url address of choosen location.
"""

address = input("url: ")
filename = input("city: ") + ".dat"

with open(filename, 'w') as file:
    file.write(address)
    print("\nSuccesfully created " + filename + "\nPress any key to exit...")

input()
