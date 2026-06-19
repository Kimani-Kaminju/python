#Python with parameters
#Parameters are values that get passed as arguments when you invoke a function

def greeting(name):
    print(f"Hello{name}.Hope you are doing fine")

greeting("Jane")
greeting("Mutuse")
greeting("Kim")
greeting("Mike")

#Below is an addition function that accepts three parameters
def add(x,y,z):
    sum= x+y+z
    print("The sum of the numbers is:",sum)
#invoke
add(45,20,16)
add(10,20,30)

print("=============================")
#By use of a function that accepts parameters,calculate the speed of a vehicle which covered 400 km in 5hrs time
 
def speed(d,t):
    speed=d/t
    print("The speed is:",speed)
speed(400,5)
