import random

# List of words for the game
word_list = ['python', 'hangman', 'programming', 'developer', 'challenge']

# Hangman stages for incorrect guesses
hangman_stages = [
    '''
       ------
       |    |
       |
       |
       |
       |
    --------
    ''',
    '''
       ------
       |    |
       |    O
       |
       |
       |
    --------
    ''',
    '''
       ------
       |    |
       |    O
       |    |
       |
       |
    --------
    ''',
    '''
       ------
       |    |
       |    O
       |   /|
       |
       |
    --------
    ''',
    '''
       ------
       |    |
       |    O
       |   /|\\
       |
       |
    --------
    ''',
    '''
       ------
       |    |
       |    O
       |   /|\\
       |   /
       |
    --------
    ''',
    '''
       ------
       |    |
       |    O
       |   /|\\
       |   / \\
       |
    --------
    '''
]

def get_random_word(word_list):
    # Select a random word from the list
    return random.choice(word_list)

def display_word_state(word, guessed_letters):
    # Display the current state of the word with guessed letters revealed
    display = ''.join([letter if letter in guessed_letters else '_' for letter in word])
    return display

def play_round():
    word = get_random_word(word_list)
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect = len(hangman_stages) - 1

    print("Welcome to Hangman!")

    # Play the game until the user wins or loses
    while incorrect_guesses < max_incorrect:
        print(hangman_stages[incorrect_guesses])
        print(f"Word: {display_word_state(word, guessed_letters)}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")

        # Get user input for a letter guess
        guess = input("Guess a letter: ").lower()

        # Check if the guess is valid
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        # Check if the guess is in the word
        if guess in word:
            print(f"Good job! {guess} is in the word.")
        else:
            print(f"Sorry, {guess} is not in the word.")
            incorrect_guesses += 1

        # Check if the user has guessed the entire word
        if all(letter in guessed_letters for letter in word):
            print(f"Congratulations! You guessed the word: {word}")
            return True

    # If the user runs out of guesses, they lose
    print(hangman_stages[incorrect_guesses])
    print(f"Sorry, you lost! The word was: {word}")
    return False

def main():
    while True:
        play_round()
        # Ask the user if they want to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("Thanks for playing!")

if __name__ == "__main__":
    main()
