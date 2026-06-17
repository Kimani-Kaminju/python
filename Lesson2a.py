#Boolean-data type that evaluates to either true or false
 
israining = False
print(israining)
#shows false
print(type(israining))
#shows False <class 'bool'>

#PYTHON LISTS
#List is a collection of items that are ordered in a certain way
#introduced by use of ()
#stored inside indexes.INDEXES START WITH 0
#List can easily be changed

cars = ["BMW", "BENZ", "HACE","PRADO", "PROBOX", "MCLAREN","RANGER","ROVER"] 
print(cars)
#output ['BMW', 'HONDA', 'RANGER', 'RANGER', 'ROVER']
print(type(cars))
# output <class 'list'> 

# accessing items of a list       
#we use indexes access them
print(cars[0])
#bmw
print(cars[4])
#rover

#list slicing-creating a list from an already existing list
print(cars[4:])

print(cars[3:7])

#LIST MUTABILITY
#we use 'append' function to add an item at the end of the list
cars.append("Mercedes")
print(cars)

cars.append("subaru")
print(cars)

#'pop' function at the end of the list
cars.pop()
print(cars)

#we can replace an item on certain index
cars[0]="Pajero"
print("cars")

del cars[4]
print(cars)

#check on remove,sort on lists