sum = 0 

conti = True 

while conti == True:
    x = int(input(" please enter a random number --->  "))

    if x == 0:
        print("loop terminated")
        print("the current amount is", sum)
        break

    else:
        print("continues loop")
        print(" your total number is",sum)
        sum += x
        continue


