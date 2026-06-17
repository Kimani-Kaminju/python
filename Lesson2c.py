phonebook = {
    "Benson" : 2542757907,
    "Mary" :2547987409,
    "Joseph" : 254457478
 }
print("My dictionary is: ",phonebook)
print(type(phonebook))

#accessing the items
print(phonebook["Benson"])
print(phonebook["Mary"])

print("====================================")

player={
    "name" : "Messi",
    "age" : 40,
    "teams" : ["Miami","PSG","Barcelona", "Argentina"],
    "more" : {
        "children" : 3,
        "residence": "US",
        "phone" : (2547464677,2547695895,2547648748)
                   
    }
}
print("name of the player is:",player["name"])
print(player["teams"][2])
print(player["more"]["phone"][1])
