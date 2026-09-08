a = 23
b = 12
c = 34

print( a > b and c < a )
print( a > b or c < a and b == a )
print( not (a > b or c < a and b == a ))




username = "JAMES"
password = "ROSARIO"

Iusername = input("Input your username:  ")
Ipassword = getpass("Input your password:  ")

if Iusername == username:
     if Ipassword == password:
       print("access granted")
else:
       print("Invalid")




