# Comparison operators
#Used to compare/relate different conditions and usually evaluate to a boolean value(False/true)
#they are : (>,<,<=,>=,!=) 

#<-less than
#>-greater than


print(5>2)
#true
print(5<2)
#false
print(5<=2)
#true
print(5>=2)
#false
print(5==2)
#false
print(5!=2)
#true

#Logical operators

# 1.logical AND-This evaluates to true if only both or all conditions are true
print((5<2) and (5>3))
#false

# 2.Logical OR-evaluates to true if one of the conditon is true
print((5<2) or (5>3))
#true

# 3.Logical not-negates a condition -if the statement turns to be true it displays false and vice versa
print(not(5>3))
#false

print("=====================================================================")

#if...else-conditional statement used to evaluate a condition and if it is met the if block executes otherwise the else block is then executed
        #example
number = -10

if number > 0:
    print("Positive")
else:
    print("negative")

print("===================================")

#python program able to evaluate whether a number is even or odd number
number = 2
if  number %2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number." )

print("============================================================================")

#if..elif..else-evaluates multiple conditions 

mynumber = 7 

if mynumber > 0:
    print("The number is positive")
elif mynumber == 0:
    print("The number is zero")
else:
    print("The number is negative")

print("===============")    
#python program able to check based on the age whether a person is eligible to vote or not.eligible-print you can vote else-print cant be allowed to vote

age = 18

if age > 18:
    print("You can vote Wantam")
elif age == 18:
    print("You can vote Wantam")
else:
    print("You cant vote")


