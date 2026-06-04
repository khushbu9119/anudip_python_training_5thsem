secret_number = 42
guess = None
while (guess != secret_number):
    guess = int(input("Guess the number: "))
    if (guess < secret_number):
        print("Too low! Try again.")
    elif (guess > secret_number):
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the number!")
