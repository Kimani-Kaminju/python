#python fuctions
#function-block of code that perfom a given task/action/job.They are re-usable meaning
#We have two main types of functions:
    #inbuilt-predefined/installed with the python interpreter eg:-print,append,sort,pop
    #user defined-functions created by a programmer
        #to create a user-defined function we use the def keyword followed by the name of the function,paretheses and full colon at the end.on the line that follows,you need to indent which marks the start of the body function

def greeting ():
    print("Hello there,Hope you are doing fine")
#below we invoke/call the fuction by use of its name
greeting()

print("==============")
#Addition function
def addition():
    number1 = 30
    number2 = 20
    answer  = number1 + number2
    print("The answer is:",answer)
addition()
print("==============")
#function to multiply three number , invoke the function to get the output

def multiply():
    number3 =  20
    number4 =  20
    number5 = 20
    result  = number3 * number4 * number5
    print("The Result is:",result)
multiply()
print("==============")
#Below is a function that accepts user input
def divide():
    number6 = int(input("Enter the first number"))
    number7 = int(input("Enter the second number"))
    quotient = number6/number7
    print("The answer is:",quotient)
divide()
divide()