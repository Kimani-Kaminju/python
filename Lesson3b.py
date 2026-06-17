#Base on the if....elif....else conditional statement,we can create the grading system as shown below

marks = 106

if marks > 0 and marks < 30:
    print("The Grade attained is: F")
elif marks >30 and marks < 50:
    print("The Grade attained is: D")
elif marks > 50 and marks < 60:
     print("The Grade attained is: C")
elif marks > 60 and marks < 70:
     print("The Grade attained is: B")
elif marks > 70 and marks < 100:
      print("The Grade attained is: A")
else:
     print("invalid entry try again..")

print("============================================")
#John wants to donate blood but there is a condition he needs to meet.A person to donate blood has to be 50 KG and above and his /her age is not less than 18.
#create a python program that is able to check whether john who has 57kg is able to donate blood and is 26years is able to donate

age = 26
weight = 57

if age == 18 and weight == 50:
     print("You can donate blood")
elif age > 18 and weight > 50:
     print("You can donate blood")
else:
     print("You cant donate blood")