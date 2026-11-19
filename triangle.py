rr = int(input("Enter number --> "))

for x in range (rr):
    p = 1
    for y in range (x, rr):
        print(" ", end=" ")
    for y in range (x):
        print(p, end= " ")
        p+=rr
    for z in range (x+1):
        print(p, end=" ")
        p-=1
    print()