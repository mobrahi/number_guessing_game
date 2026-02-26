import random

def number_guessing_game():
    print("🎯 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Generate random number
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    while attempts < max_attempts:
        try:
            # Get player's guess
            guess = int(input(f"\nAttempt {attempts + 1}/{max_attempts}. Enter your guess: "))
            attempts += 1
            
            # Check the guess
            if guess < secret_number:
                print("📈 Too low! Try a higher number.")
            elif guess > secret_number:
                print("📉 Too high! Try a lower number.")
            else:
                print(f"🎉 Congratulations! You guessed it in {attempts} attempts!")
                return
                
        except ValueError:
            print("❌ Please enter a valid number!")
    
    # Game over - no attempts left
    print(f"\n😔 Game over! The number was {secret_number}.")

# Play the game
if __name__ == "__main__":
    number_guessing_game()
    
    # Ask to play again
    while True:
        play_again = input("\nWould you like to play again? (yes/no): ").lower()
        if play_again == 'yes':
            number_guessing_game()
        elif play_again == 'no':
            print("Thanks for playing! Goodbye! 👋")
            break
        else:
            print("Please enter 'yes' or 'no'")