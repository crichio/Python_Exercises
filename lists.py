# python lists exercise

# this code creates a list of foods and performs a series of methods that change the list, and the prints items within the list

foods = ["Pizza", "Sushi", "Tacos"]          # creates a new list called foods and stores 3 items in the list in the form of strings

foods[0] = "Spaghetti"                       # replaces the item at index 0 (the first item) with a new string item
foods.insert(1, "Cheeseburger")              # adds a new item at index 1 (second item)
foods.append("Burrito")                      # adds a new item at the end of the list

print(foods)                                 # prints the foods list
print(foods[2])                              # prints the item at index 2 (third item) of the foods list, which in this case is "Sushi"
print(len(foods))                            # prints the length of the foods list

for food in foods:                           # loops over the foods list and prints each of them to the screen in their own singular output
    print(food)
