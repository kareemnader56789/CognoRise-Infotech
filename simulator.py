import random

def roll_dice(sides, num_rolls):
    # Generate random numbers for each roll
    rolls = [random.randint(1, sides) for _ in range(num_rolls)]
    return rolls

def main():
    print("Welcome to the Dice Rolling Simulator!")

    try:
        # Get user input for the number of sides and rolls
        sides = int(input("Enter the number of sides on the dice: "))
        num_rolls = int(input("Enter the number of times to roll the dice: "))

        if sides < 1 or num_rolls < 1:
            print("The number of sides and rolls must be greater than 0.")
            return

        # Roll the dice and display the results
        results = roll_dice(sides, num_rolls)
        print(f"\nRolling a {sides}-sided dice {num_rolls} times...")
        print("Results: ", results)

    except ValueError:
        print("Please enter valid numbers for sides and rolls.")

if __name__ == "__main__":
    main()
