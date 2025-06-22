# smooooooth operators

# exercise in using python operators to manipulate values and variables

x = 6                                       # assigns 6 to variable x
y = 8                                       # assigns 8 to variable y
z = 4                                       # assigns 4 to variable z

# arithmetic operators

addition = x + y                            # adds x and y, 14
subtraction = x - y                         # subtracts x and y, -2
multiplication = x * y                      # multiplies x and y , 48
division = x / y                            # divides x and y, .75
floor_division = x // y                     # divides x and y and rounds down, 0
modulus = x % y                             # gets remainder of x into y, 6
exponentiation = x ** y                     # x to the y power, 1,679,616

# assignment operators

assign = z                                  # assigns z to the assign variable, 4
z += 2                                      
assign_add = z                              # adds 2 to z and assigns the sum to z, 6
z -= 2
assign_subtract = z                         # subtracts 2 from z and assigns the difference to z, 4
z *= 2
assign_multiply = z                         # multiplies 2 to z and assigns the product to z, 8
z /= 2
assign_divide = z                           # divides 2 from z and assigns the quotient to z, 4.0
z //= 2
assign_floor_divide = z                     # divides 2 from z, rounds down, and assigns the solution to z, 2.0
z %= 2
assign_modulus = z                          # divides 2 from z, gets the remainder and assigns the solution to z, 0.0
z **= 2
assign_exponentiate = z                     # raises z to the 2 power and assigns the solution to z, 0.0

# comparison operators

equal = x == y                              # x equals y, returns boolean value, False
not_equal = x != y                          # x does not equal y, returns boolean value, True
greater_than = x > y                        # x is greater than y, returns boolean value, False
less_than = x < y                           # x is less than y, returns boolean value, True
greater_than_or_equal = x >= y              # x is greater than ofr equal to y, returns boolean value, False
less_than_or_equal = x <= y                 # x i less than or equal to y, returns boolean value, True

# logical operators

and_operator = x < 7 and y > 7              # returns true if BOTH operations are true, True
or_operator  = x > 7 or y > 7               # returns tru if EITHER operations are true, True
not_operator = not(x > y)                   # returns the opposite of correct boolean value, True

# membership operators

numbers_sequence = [1,3,5,7,9]              # declares variable called numbers_sequence and assigns it to an array of odd numbers
guess = 3                                   # declares variable called guess and assigns it to the number 3

in_operator = guess in numbers_sequence             # declares variable called in_operator and asks if guess is in numbers_sequence, returns boolean value, True
not_in_operator = guess not in numbers_sequence     # declares variable not_in_operator and asks if guess is not in numbers_sequence, returns boolean value, False

# identity operators

is_operator = x is y                        # declares variable called is_operator and asks if x is equal to y, returns a boolean value, False
is_not_operator = x is not y                # declares variable called is_not_operator and asks if x is not equal to y, returns a boolean value, True



# OUTPUTS

#let's print our work!



# arithmetic operators outputs

#prints all variable in arithmetic operation to the screen

print(addition)                 # 14
print(subtraction)              # -2
print(multiplication)           # 48
print(division)                 # .75
print(floor_division)           # 0
print(modulus)                  # 6
print(exponentiation)           # 1,679,616

# assignment operators outputs

#prints all variable in assignment operators to the screen

print(assign)                   # 4
print(assign_add)               # 6
print(assign_subtract)          # 4
print(assign_multiply)          # 8
print(assign_divide)            # 4.0
print(assign_floor_divide)      # 2.0
print(assign_modulus)           # 0.0
print(assign_exponentiate)      # 0.0

#comparison operators outputs

# prints all the variable in comparison operators to the screen

print(equal)                    # False
print(not_equal)                # True
print(greater_than)             # False
print(less_than)                # True
print(greater_than_or_equal)    # False
print(less_than_or_equal)       # True

# logical operators outputs

# prints all the variable in logical operators to the screen

print(and_operator)             # True
print(or_operator)              # True
print(not_operator)             # True

# membership operators outputs

# prints all the variables in membership operators to the screen

print(in_operator)              # True
print(not_in_operator)          # False

# identity operators outputs

# prints all the variable in identity operators to the screen

print(is_operator)              # False
print(is_not_operator)          # True