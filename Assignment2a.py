age = 11

if age < 10:
    print("You are in Primary Classes")
elif 10 < age < 15:
    print("You are in Junior Secondary")
elif 15 < age < 19:
    print("You are in Senior Secondary")
elif age > 19:
    print("You are in College")
else:
    print("Age does not fall into the specified categories")


print("=================================")


languages = (
    "French", "Kiswahili", "Chinese", "Congolese", "English", 
    "Indian", "Portuguese", "Italian", "Russian", "Japanese"
)


for lang in languages:
    if lang == "English":
        print("English is found")
    
else:
    print("English is not found")
