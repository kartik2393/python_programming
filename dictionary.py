fruit={"lemon": "sour taste",
       "apple": "good for health",
       "watermelon": "immunity"}
# print(fruit)
# print(fruit["lemon"])
# fruit["pear"]= "kind of an apple"
# print(fruit)
# fruit["lemon"]="great with tequila"
# print(fruit)
# del fruit["lemon"]
# fruit.clear()
# print(fruit)
print(fruit)
while True:
    key=input("enter the name of a fruit: ")
    if key=="quit":
        break
    if key in fruit:
        description=fruit.get(key)
        print(description)
    else:
        print("we dont have that  " +  key)


