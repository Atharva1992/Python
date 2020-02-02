age = input("What is your age :")

try:
    agenum = int(age)
except:
    agenum = -1 ;

if agenum > -1 :
    print("Your age is : ",agenum)
else :
    print("You entered incorrect value")
