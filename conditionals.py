# conditional flow exercise

# code asks for the user's age and responds depending on the user's answer

age = int(input("Enter your age: "))                                        # declares a variable called age that asks the user their age and converts it into an integer

if age < 0:                                                                 # if the age variable is less than 0, print the string below
    print("You aren't even born yet!")
elif age <= 5:                                                              # else, if the age variable is less than or equal to 5, print the string below
    print("You're just a baby!") 
elif age <= 18:                                                             # else, if the age variable is less than or equal to 18, print the string below
    print("You are just getting started!")
elif age <= 30:                                                             # else, if the age variable is less than or equal to 30, print the string below
    print("You're starting to get the hang of it now!")
elif age <= 65:                                                             # else, if the age variable is less than or equal to 65, print the string below
    print("You are a full grown adult. Congrats on making it this far!")
elif age <= 85:                                                             # else, if the age variable is less than or equal to 85, print the string below
    print("Dang! You are getting old there!")
elif age <= 120:                                                            # else, if the age variable is less than or equal to 120, print the string below
    print("Wow! How are you not dead yet!")
else:                                                                       # else, print the string below
    print("Surely you must be dead by now.")

    