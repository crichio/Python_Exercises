# exercise in python data types

# this code creates variables of all different data types, prints each variables data type, and then prints a string of text with each variable

user_name = "crichio"               # String
first_name = "Christian"            # String
last_name = "Ricciardi"             # String
age = 26                            # Integer
height = 5.83                       # Floating point number
weight = 172.5                      # Floating point number
is_member = True                    # Boolean value
is_platinum_member = False          # Boolean value
relationship_status = None          # NoneType
fav_algebra_problem = 3 + 4j        # Complex 




print(type(user_name), type(first_name), type(last_name), type(age),        # Prints the data type of each variable
type(height), type(weight), type(is_member), type(is_platinum_member), 
type(relationship_status), type(fav_algebra_problem))

print(f"Hello, {user_name}! You are {age} years old. Your heigh is: {height} and you weight is: {weight}. Are you a member?: {is_member}. Are you a platinum member?: {is_platinum_member}. You should get a girlfriend because your relationship status is {relationship_status}. Do you like algebra? Try this: {fav_algebra_problem}.")

# Prints all the variables in a string