size = int(input("Please enter the size--> "))

for p in range(size):
    for i in range(size - p - 1):
        print(" ", end="")
    for z in range(2 * p + 1):
        print("*", end="")
    print()
    
for x in range(size - 1):
    for y in range(x + 1):
        print(" ", end="")
    for z in range(2 * (size - x - 2) + 1):
        print("*", end="")
    print()