age = int(input("Enter you age --->   "))
is_employed = bool(input(" are you currently employed (True/False) --->    "))
credit_score = int(input("Enter your credit score --->   "))
anual_income = float(input("Your anual income --->   "))
has_collateral = bool(input("Do you have any collateral (True/False) --->"))

Base_rate = 0.0

if age >= 21 and is_employed == True:
        print("Applicant pass baseline requirements")
        if credit_score >= 750:
           Base_rate = 5.0
           print("You have a high credit score")
        if anual_income >=100000:
           Base_rate = 4.5
           print("You have a high salary")
        else: 
              print("failed")
        if credit_score <= 600 and credit_score < 750:
             Base_rate = 8.0
             print("You have a high credit score")
             if 








    