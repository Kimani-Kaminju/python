income = 99999
if income <= 5999:
    print("Contribution is:",150.00)
elif income >5999 and  income< 7999:
    print("Contribution is:",300.00)
elif income >= 7999 and income <= 11999:
    print("Contribution is:",400.00)  
elif income >=11999 and income< 14999:
    print("Contribution is:",500.00) 
elif income >=14999 and income< 19999:
    print("Contribution is:",600.00)
elif income >=19999 and income< 24999:
    print("Contribution is:",750.00)
elif income >=24999 and income< 29999:
    print("Contribution is:",850.00)
elif income >=29999 and income< 49999:
    print("Contribution is:",1000.00)
elif income >=49999 and income<= 99999:
    print("Contribution is:",1500.00)
elif income >100000:
    print("Contribution is:",2000.00)
else:
    print("Invalid Entry")