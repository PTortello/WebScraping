address = input("url: ")
filename = input("city: ") + ".dat"

with open(filename, 'w') as file:
    file.write(address)
    print("\nSuccesfully created " + filename + "\nPress any key to exit...")

input()
