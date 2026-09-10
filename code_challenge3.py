name = input("Enter your name ---->   ")
items = str(input("type of item ---->   "))
is_frag = bool(input("Is it fragile ---->   "))
weight = float(input("how heavy it is in(kg) ---->   "))
distance = float(input("travel distance in (km) ---->    "))
is_express = eval(input("is it express ---->    "))
is_international = eval(input("is it international ---->   "))

#calculations
base_cost = (weight * 2.50) + (distance * 0.15)
	

#freeshipping
if weight <= 2.0 and distance <= 100 and  is_express == False and is_international == False:
	print("freeshipping")
	total = 0

elif is_international == True and is_express == True :
	print("package is international and express")
	total = (base_cost * 1.40) + 50

elif is_express == True or is_international == True and weight > 20:
	print("internatonal and express package is greater than 20")
	total = (base_cost * 1.20) + 25

elif weight > 30 or distance > 1000:
 	print("The package is overweight")
 	total = base_cost + 30


else  : 
        print("standard rate")
        total = base_cost

print("Buyers name:", name)
print("Items name:", items)
print("Over all total", total,"php" )

	
	                      



