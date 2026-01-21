import random

# List of 5 predefined words
words = ["animal", "orange", "apple", "program", "banana"]

# Select a random word
word = random.choice(words)

# Create a list to store guessed letters
guessed_letters = []

# Number of incorrect guesses allowed
max_attempts = 6
attempts = 0

print("🎮 Welcome to Hangman Game!")
print("You have 6 incorrect guesses.\n")

# Main game loop
while attempts < max_attempts:
    display_word = ""

    # Display current word state
    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"

    print("Word:", display_word)
    print("Guessed letters:", guessed_letters)
    print("Remaining attempts:", max_attempts - attempts)

    # Check if player has guessed the word
    if "_" not in display_word:
        print("\n🎉 Congratulations! You guessed the word correctly.")
        break

    # Take user input
    guess = input("Enter a letter: ").lower()

    # Check if input is valid
    if guess in guessed_letters:
        print("You already guessed that letter.\n")
    elif guess in word:
        guessed_letters.append(guess)
        print("Correct guess!\n")
    else:
        guessed_letters.append(guess)
        attempts += 1
        print("Wrong guess!\n")

# Game over condition
if attempts == max_attempts:
    print("\n❌ Game Over! You ran out of attempts.")
    print("The word was:", word)

   

