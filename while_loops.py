# while loops

# code asks the user to guess a number between 1 and 10, repeats this until the guess is the correct number

correct_number = 6                                            # declares a variable called correct number and assigns it the integer 6
guess = None                                                  # declares a variable called guess and assigns it the value None

while guess != correct_number:                                # while the guess variable is not equal to the number in the correct number variable...
    guess = int(input("Guess a number between 1 and 10: "))   # prints guess variable to the screen and changes the value of guess variable to a user input which asks the user to guess a number and converts their response into an integer

print("Correct! You guessed the right number.")               # once the guess variable is equal to the correct number variable, print this string to the screen



# think you can guess the correct number? ;)