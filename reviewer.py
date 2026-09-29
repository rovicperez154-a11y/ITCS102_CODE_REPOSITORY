age = int(input(" Owner age --->  "))
revenue = float(input(" Monthly revenue --->  "))
credit = int(input(" Credit Score --->  "))
years = float(input(" Years in Business --->  "))
has_defaults = bool(input(" does your business file for bankrupcy ---> "))
col= str(input(" Collateral name ---> "))
cov = float(input(" Collateral value --->  "))

max_loan = 0
base_fee = 0

#Outer baseline requirements
if age >= 21 and years >=2.0 and has_defaults == False:
    print("You have pass the baseline requirements")
 #tier 1
    if credit >= 720:
        print(" You have a high credit score")
        if revenue >= 50000:
                    print(" You have a high revenue")
                    base_fee = revenue * 0.015
                    print(" Your base fee is set to",base_fee)
                    if credit >= 620 and credit < 720:
                        max_loan = revenue * 1.5
                        print(" you have a low credit score")
                        if years >= 5.0:
                             base_fee = max_loan * 0.02
                             print(" You are illegible")


                        else:
                             base_fee = max_loan * 0.035
                             print(" Your base fee is set to", base_fee)
                             print(" Your credit score is too low")




        else:
              base_fee = revenue * 0.025
              print(" Your base fee is set to", base_fee)

    else:
        (" You have a low credit score")
        
else:
    print(" You are rejected")