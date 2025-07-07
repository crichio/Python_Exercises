# whats yo function

# this code asks the user for 2 numbers and then returns back the sum, difference, product, and quotient of both numbers

number_1 = int(input("Enter the first number: "))                # declares a variable called number_1, asks the user to enter a number, and converts their answer into an integer
number_2 = int(input("Enter the second number: "))               # declares a variable called number_2, asks the user to enter a number, and converts their answer into an integer


def add(x, y):                                                  # declares a function called add, and passes 2 parameters called x & y
    return x + y                                                # returns parameter x plus parameter y

def subtract(x, y):                                             # declares a function called subtract, and passes 2 parameters called x & y
    return x - y                                                # returns parameter x minus parameter y

def multiply(x, y):                                             # declares a function called multiply, and passes 2 parameters called x & y
    return x * y                                                # returns parameter x times parameter y

def divide(x, y):                                               # declares a function called divide, and passes 2 parameters called x & y
    if y == 0:                                                  # creates a conditional if parameter y is equal to 0
        return("You cannot divide by 0!")                       # if condition is meet, return a string that says "You cannot divide by 0!"
    return x / y                                                # returns parameter x over parameter y


print()                                                         # prints a blank line before the results to improve readability
print("Sum: ", add(number_1, number_2))                         # prints the add function to screen and passes user input into x and y parameters
print("Difference: ", subtract(number_1, number_2))             # prints the subtract function to screen and passes user input into x and y parameters
print("Product: ", multiply(number_1, number_2))                # prints the multiply function to screen and passes user input into x and y parameters
print("Quotient: ", divide(number_1, number_2))                 # prints the divide function to screen and passes user input into x and y parameters