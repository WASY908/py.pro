name=input("Type your name : ")
print("Welcome",name,"to this adventure !")

answer=input("You are on a dirt road , it has come to an end and you can go left or right . Which way would you like to go ? ").lower()

if answer=='left':
   answer=input("You come to a river , You can walk around it or swin across ?type walk to walk around and swin to swin accross:")

   if answer=="swin":
       print("You swamm across and were eaten by an alligation")
   elif answer=="walk":
       print("You walked for many miles , ran out of water and you lost the game")
   else:
       print("Not a valid option. You Lose !")

elif answer=='right':
    answer=input("You come to a bridge , it look wobbly, do you want to cross it or head back (cross/back) ?")

    if answer=="back":
       print("You go back and lose")
    elif answer=="cross":
       answer=input("You cross the bridge and meet a stranger . Do you talk to them (yea/no)")
       if answer=="yes":
           print("You talk to the stranger and they give you gold . You Win !")
       elif answer =='no':
           print("You ignored the stranger and they are offered and you lose.")
       else:
           print("Not a valid option. You Lose !")
    else:
       print("Not a valid option. You Lose !")

else:
    print("Not a valid option. You Lose !")

print("Thank you for trying ",name)