from customer import Customer
import random
import datetime

atm = Customer(id)

while(True):
    pinNumber = int(input("Enter your pin number : "))
    wrong = 1
    
    if wrong > 3:
        print("Error. Take your card and try it again later")
        break

    while(pinNumber != int(atm.get_customer_pin()) and wrong <= 3):
        pinNumber = int(input("The pin which you entered is wrong. Try entering your pin again : "))
        wrong += 1

    while(pinNumber == int(atm.get_customer_pin()) and wrong <= 3):
        print("Welcome in Progate ATM")
        print("1. Check balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Change your pin")
        print("5. Exit")
        choose = int(input("Choose menu (1-5) : "))

        if choose < 1 or choose > 5:
            print("That menu is not featured. Choose it again")
            print("")
        elif choose == 1:
            print("Your balance : Rp. " + str(atm.get_customer_balance()))
            print("")
        elif choose == 2:
            debet = int(input("How much money do you want to withdraw? "))
            verify = input("Are you sure to withdraw Rp." + str(debet) + ",- from your balance? (Y/N) ")
            if verify == 'y' or verify == 'Y':
                if debet <= 0 : 
                    print("Error.. Incorrect money!!")
                    print("")
                    continue
                elif debet < atm.get_customer_balance() :
                    print("Your previous balance : Rp. " + str(atm.get_customer_balance()) + ",-")
                    atm.debit(debet)
                    print("Successfully in withdrawing money.")
                    print("Your remaining balance : Rp. " + str(atm.get_customer_balance()) + ",-" )
                    print("")
                else:
                    print("Your balance doesn't have that much.")
                    print("Please deposit some.")
                    print("")
            else:
                print("Aborting the request.....")
                print("")
                continue
        elif choose == 3:
            print("Your balance : Rp. " + str(atm.get_customer_balance()) + ",-")
            deposit = int(input("How much money do you want to save ? : Rp. "))
            verify = input("Are you sure to save Rp." + str(deposit) + ",- into your balance? (Y/N) ")
            if verify == 'y' or verify == 'Y':
                if deposit <= 0:
                    print("Error.. Incorrect money!!")
                    print("")
                else:
                    print("Your previous balance : Rp. " + str(atm.get_customer_balance()) + ",-")
                    atm.credit(deposit)
                    print("Successfully in depositing money into your account")
                    print("Your balance : Rp. " + str(atm.get_customer_balance()) + ",-")
                    print("")
            else:
                print("Aborting the request.....")
                print("")
                continue
        elif choose == 4:
            oldPin = int(input("Enter your pin : "))
            while oldPin != atm.get_customer_pin():
                print("You entered wrong pin number. Try again")
            
            newPin = int(input("Enter your new pin number. Make sure it is different from your older pin number : "))
            verify_newPin = int(input("Enter your new pin number again : "))
            
            while newPin != verify_newPin:
                print("The pin you entered is not match. Try again")
            
            if newPin != AtmCard.get_defaultpin():
                print("You have successfully change your pin")
                print("")
            else:
                print("You cannot use the previous password!")
                print("")

        elif choose == 5:
            date = datetime.datetime.now()
            print("Record " + str(random.randint(100000, 1000000)) + " on " + str(date.strftime("%x")))
            print("Your balance : Rp." + str(atm.get_customer_balance()) + ",-")
            print("Thank you and good bye")
            exit(0)