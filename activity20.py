from getpass import getpass
u = "rovicpogi"
p = "rovic"

isLogin = False

while isLogin == False:

    user = input( " please enter your username --->  ")
    password = getpass(" please enter your passwrod --->  ")

    if user == u and password == p:
        print(" ACCESS GRANTED")
        isLogin = True

    else:
        print(" ACCESS DENIED ")
        isLogin = False