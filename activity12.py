import getpass

username = 'aldenpogi'
password = 'rovicpogi143'

u = input("Enter your Username -----> ")
p = getpass.getpass("Enter your Password -----> ")

if username == u and p == password :
          print("ACESS GRANTED")

else : 
          print("ACESS DENIED")

