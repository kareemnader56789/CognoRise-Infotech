import random

def get_computer_choice():
    # Randomly choose between rock, paper, and scissors
    return random.choice(['rock', 'paper', 'scissors'])

def get_user_choice():
    # Prompt the user to enter rock, paper, or scissors
    choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    while choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please try again.")
        choice = input("Enter your choice (rock, paper, or scissors): ").lower()
    return choice

def determine_winner(user_choice, computer_choice):
    # Determine the winner based on the game rules
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "win"
    else:
        return "lose"

def play_round():
    # Get user and computer choices
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    # Display the choices
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    # Determine and display the result
    result = determine_winner(user_choice, computer_choice)
    if result == "tie":
        print("It's a tie!")
    elif result == "win":
        print("You win!")
    else:
        print("You lose!")

    return result

def main():
    user_score = 0
    computer_score = 0

    while True:
        # Play one round of the game
        result = play_round()

        # Update the score based on the result
        if result == "win":
            user_score += 1
        elif result == "lose":
            computer_score += 1

        # Display the score
        print(f"\nScore: You {user_score} - {computer_score} Computer")

        # Ask the user if they want to play again
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("Thanks for playing!")

if __name__ == "__main__":
    main()
