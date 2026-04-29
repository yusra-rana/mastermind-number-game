import random

# Generate random 4-digit number
num = random.randrange(1000, 10000)

# First guess from user
guess = int(input("Guess the 4 digit number: "))

# Number of tries
count_try = 1

# Loop until correct guess
while guess != num:

    # Convert into string to compare digits
    guess = str(guess)
    num = str(num)

    # Correct digit counter
    correct = 0

    # Check each digit
    for i in range(4):
        if guess[i] == num[i]:
            correct += 1

    # Show result
    if correct == 0:
        print("No digit is correct.")
    else:
        print("You got", correct, "digit(s) correct.")

    # Next guess
    guess = int(input("Try again: "))

    # Increase tries
    count_try += 1

    # Convert secret number back to integer
    num = int(num)

# Final result
print("Congratulations! You guessed the number.")
print("Total tries:", count_try)