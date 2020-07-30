winning_number=30
gussed_number = int(input("gussed a number to win this game between 1 to 100 :"))
if gussed_number == winning_number:
    print("you win it ! hurry")
elif gussed_number<30 :
    print("you gussed too low")
elif gussed_number>30:
    print("you gussed too high")
elif gussed_number>100:
    print("please enter valid number! thankyou")
print("thankyou for playing you are good gusser !")