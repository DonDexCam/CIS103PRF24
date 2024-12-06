import random

# Function to print blank lines to simulate clearing the screen
def clear_screen():
    for _ in range(20):  # Prints 20 blank lines
        print()

def main():
    # Ask for player's name
    player_name = input("Enter your name: ").strip()
    if player_name == "":
        player_name = "Player"  # Default name if no name is entered

    # Loop to ask if the player wants to play again
    play_again = "y"
    
    while play_again.lower() == "y":
        # Generate a random number between 1 and 200
        number_to_guess = random.randint(1, 200)
        
        # Ask the player for the number of chances, with a default of 15
        guesses_input = input("Enter the number of chances (1-100, default is 15): ").strip()
        
        # Validate the number of chances
        if guesses_input == "" or guesses_input == "\n":
            guesses = 15
        else:
            try:
                guesses = int(guesses_input)  # Convert input to integer
                if guesses < 1 or guesses > 100:
                    print("Error: Please enter a number between 1 and 100.")
                    continue
            except ValueError:
                print("Error: Please enter a valid integer.")
                continue

        # Initialize game variables
        guesses_left = guesses
        guesses_made = 0
        invalid_guesses = 0

        # Start the game
        clear_screen()  # Clear the screen by printing 20 blank lines
        print(f"Welcome {player_name}! You have {guesses} chances to guess the number.\n")
        
        # Loop for each guess attempt
        while guesses_left > 0:
            print(f"You have {guesses_left} guesses left.")
            print(f"Number of error guesses: {invalid_guesses}")
            print(f"Number of guesses made: {guesses_made}\n")
            
            # Take input for the guess and validate
            guess_input = input(f"Enter your guess between 1 and 200: ").strip()
            
            # Validate if the input is a number
            if guess_input == "":
                print("Error input! You must enter a number.")
                invalid_guesses += 1
                continue
            
            try:
                guess = int(guess_input)  # Convert the input to an integer

                # Check if the guess is within the valid range
                if guess < 1 or guess > 200:
                    print("Error: Your guess must be between 1 and 200.")
                    invalid_guesses += 1
                    continue

            except ValueError:
                print("Error: Please enter a valid integer.")
                invalid_guesses += 1
                continue

            # Increment the guesses made and reduce guesses left
            guesses_made += 1
            guesses_left -= 1

            # Check if the guess is too high, too low, or correct
            if guess < number_to_guess:
                print("Your guess is too low!")
            elif guess > number_to_guess:
                print("Your guess is too high!")
            else:
                print(f"Congratulations {player_name}! You guessed the number {number_to_guess} in {guesses_made} guesses!")
                break

            if guesses_left == 0:
                print(f"Sorry {player_name}, you're out of guesses! The number was {number_to_guess}.")
                break
        
        # Ask if the player wants to play again
        play_again = input("\nDo you want to play again? (y/n): ").strip().lower()
        if play_again != "y":
            print(f"Thanks for playing, {player_name}! Goodbye!")
            break

# Call the main function to start the game
main()
