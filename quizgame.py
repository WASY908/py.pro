print("Welcome To My Computer Quiz")
playing=input("Do You Want To Play? ")
print(playing)

if playing != "yes" and playing != "Yes":
    quit()

print("Ok ! Let's play :) ")
score=0

answer=input("What Does CPU Stand For? ")

if answer=="central processing unit" or answer=="Central Processing Unit":
    print("Correct")
    score+=1
else:
    print("Incorrect!")
    score-=1

answer=input("What Does GPU Stand For? ")

if answer=="graphic processing unit" or answer=="Graphic Processing Unit":
    print("Correct")
    score+=1
else:
    print("Incorrect!")
    score-=1

answer=input("What Does RAM Stand For? ")

if answer=="random access memory" or answer=="Random Access Memory":
    print("Correct")
    score+=1
else:
    print("Incorrect!")
    score-=1

answer=input("What Does PSU Stand For? ")

if answer=="power supply" or answer=="Power Supply":
    print("Correct")
    score+=1
else:
    print("Incorrect!")
    score-=1

print("You got " + str(score) + " questions correct!")

print("You got " + str ((score/4) * 100) + " %.")