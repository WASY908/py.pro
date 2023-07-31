#Enter the First Value

First_value=input("Enter The First Number")
Operator=input("Enter Any Operator You Like To Perform(+,-,%,/,*)")
#Enter the Second Value

Second_value=input("Enter The Second Number")

First_value=int(First_value)
Second_value=int(Second_value)

if Operator=="+":
    print(First_value + Second_value)

elif Operator=="-":
    print(First_value - Second_value)

elif Operator=="*":
    print(First_value * Second_value)

elif Operator=="/":
    print(First_value / Second_value)

elif Operator=="%":
    print(First_value % Second_value)

else:
    print("Invalid Operators")


