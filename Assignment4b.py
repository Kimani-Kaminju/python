#simple interest
def SI(p,r,t):
    Interest= p*r/100*t
    print("The Simple Interest is:",Interest)
SI(4000,5,8)

print("========================")

def si():
    principle = int(input("Enter principle amount"))
    rate = int(input("Enter rate"))
    time = int(input("Enter Time in years"))

    inte = principle*rate/100*time
    print(" your interest is:",inte)
si()

print("==============================")

#Area of triangle
def Area(b,h):
    area=0.5*b*h
    print(area,"sq.m")
Area(16,4,)