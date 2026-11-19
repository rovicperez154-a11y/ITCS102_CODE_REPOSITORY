size = int(input("Please enter the size--> "))

for x in range (size) :
    for y in range (size) :
        if x + y == size -1 or y == size -1 :
            print("*", end=" ")
        else :
            print(" ", end=" ")
    print()

for x in range (size) :
    for y in range (size) :
        if x + y == size -1 or y == 0 :
            print("*", end=" ")
        else :
            print(" ", end=" ")
    print()