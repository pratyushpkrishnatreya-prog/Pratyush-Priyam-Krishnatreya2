import random

def get_computer_choice():
    """Randomly selects the computer's move."""
    return random.choice(['rock', 'paper', 'scissors'])

def get_user_choice():
    """
    Prompts the user for input and validates the choice.
    Returns the valid choice as a string.
    """
    valid_choices = ['rock', 'paper', 'scissors']
    while True:
        user_input = input("Enter your choice (rock, paper, or scissors): ").lower()
        if user_input in valid_choices:
            return user_input
        else:
            print(f"Invalid choice. Please choose from: {', '.join(valid_choices)}")

def determine_winner(user_choice, computer_choice):
    """
    Determines the winner of the round based on the choices.
    Returns: 0 for tie, 1 for user win, -1 for computer win.
    """
    if user_choice == computer_choice:
        return 0  # Tie

    # Define winning conditions
    if (user_choice == 'rock' and computer_choice == 'scissors') or \
       (user_choice == 'scissors' and computer_choice == 'paper') or \
       (user_choice == 'paper' and computer_choice == 'rock'):
        return 1  # User wins
    else:
        return -1 # Computer wins

def play_game():
    """Main function to run the Rock, Paper, Scissors game."""
    print("Welcome to Rock, Paper, Scissors!")
    print("You will play against the computer.")

    user_score = 0
    computer_score = 0
    rounds = 0

    while True:
        try:
            print("\n--- Round {} ---".format(rounds + 1))

            user_choice = get_user_choice()
            computer_choice = get_computer_choice()

            print(f"You chose: {user_choice.upper()}")
            print(f"Computer chose: {computer_choice.upper()}")

            result = determine_winner(user_choice, computer_choice)

            if result == 1:
                user_score += 1
                print("You win this round!")
            elif result == -1:
                computer_score += 1
                print("Computer wins this round!")
            else:
                print("It's a tie!")

            rounds += 1
            print(f"Current Score: You {user_score} - {computer_score} Computer")

            # Ask to play again
            play_again = input("Play another round? (y/n): ").lower()
            if play_again != 'y':
                break

        except KeyboardInterrupt:
            # Allows the user to easily exit with Ctrl+C
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            break


    print("\n--- Game Over ---")
    print(f"Final Score: You {user_score} - {computer_score} Computer")

    if user_score > computer_score:
        print("Congratulations! You won the game overall!")
    elif computer_score > user_score:
        print("Better luck next time! The Computer won overall.")
    else:
        print("The game ended in a draw!")

# Ensure the play_game function runs when the script is executed directly
if __name__ == "__main__":
    play_game()
