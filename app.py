import random

correct_number = random.randint(1, 10)
attempts = 0
max_attempts = 3

print("Welcome to the Number Guessing Game!")
print("Guess the number between 1 and 10.")
print("You have three Attempt.")

# Game loop
while attempts < max_attempts:
    try:
        # user_input = int(input(f"Attempt {attempts + 1}: Enter your guess (1-10): "))
        user_guess = int(input(f"Attempt {attempts + 1}: Enter your guess (1-10): "))

        # user_guess = int(user_input)

        if user_guess < 1 or user_guess > 10:
            print("Invalid input! Please enter a number between 1 and 10.")
            continue
        if user_guess == correct_number:
            print(
                f"Congratulations! You've guessed the correct number {correct_number}."
            )
            break
        attempts += 1

        if attempts == max_attempts:
            print(
                "Boooo... You've run out of attempts! The correct number was:",
                correct_number,
            )
            break

    except ValueError:
        print("Invalid input! Please enter a valid integer between 1 and 10.")
        continue
