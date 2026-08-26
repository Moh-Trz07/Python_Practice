import random

print("\n==={HANGMAN GAME}===\n") # introduction of game

guess = 6  # number of allowed guesses
words = ["developer", "kotlin", "software", "computer", "keyboard"]  # list of words
word = random.choice(words)  # randomly choose a word from the list
word_length = len(word)  # length of the chosen word
error_letters = []  # how many letters does the player guessed wrong
correct_letters = []  # track correct letters for hint system
display_word = ["_"] * word_length  # display the word with underscores
hint_used = 3  # number of using hints
Game = True  # game state

# Hangman ASCII art - 7 stages (0 to 6 wrong guesses)
hangman_stages = [
    # o wrong guesses
    """
       --------
       |      |
              |
              |
              |
              |
    ===========
    """,
    # 1 wrong guesses
    """
       --------
       |      |
       o      |
              |
              |
              |
    ===========
    """,
    # 2 wrong guesses
    """
       --------
       |      |
       o      |
       |      |
              |
              |
    ===========
    """,
    # 3 wrong guesses
    """
       --------
       |      |
       o      |
     --|      |
              |
              |
    ===========
    """,
    # 4 wrong guesses
    """
       --------
       |      |
       o      |
     --|--    |
              |
              |
    ===========
    """,
    # 5 wrong guesses
    """
       --------
       |      |
       o      |
     --|--    |
      /       |
              |
    ===========
    """,
    # 6 wrong guesses (game over)
    """
       --------
       |      |
       o      |
     --|--    |
      / \     |
              |
    ===========
    """
]

print("==You have maximum 6 incorrect guesses, if you want a hint print (hint)==\n")

while Game == True:
    # Display hangman stage based on wrong guesses
    wrong_guesses = len(error_letters)
    print(hangman_stages[wrong_guesses])

    print("Word: " + " ".join(display_word))  # display current state of the word
    print(f"\nGuesses left: {guess}")
    
    if error_letters:
        print(f"Wrong letters: {', '.join(error_letters)}")  # display wrong letters guessed
    player_guess = input("\nGuess a letter: ").lower()  # get player's guess
    
    if player_guess == "hint":
     if hint_used > 0:
        all_letters = 'abcdefghijklmnopqrstuvwxyz' # get all letters that are NOT in the word NOT already guessed
        possible_hints = []
        for letter in all_letters:
            if letter not in word and letter not in error_letters and letter not in correct_letters: 
                possible_hints.append(letter)
        
        if possible_hints:
            hint_letter = random.choice(possible_hints)
            print(f"\n💡 Hint: The letter '{hint_letter}' is NOT in the word")
            hint_used -= 1
            print(f"You have {hint_used} hints left.\n")
        else:
            print("No more hint letters available!")
     else:
        print("You've already used your hint!")
     continue
    
    if len(player_guess) != 1 or not player_guess.isalpha():
        print("Please enter a single letter!")  # validate input
        continue
    
    if player_guess in display_word or player_guess in error_letters:
        print(f"You already guessed '{player_guess}'!")  # check for repeated guesses
        continue
    
    if player_guess in word:
        print(f"✓ Good guess! '{player_guess}' is in the word.")  # correct guess
        if player_guess not in correct_letters:
            correct_letters.append(player_guess)
        
        for i, letter in enumerate(word):  # update display word with correct guesses
            if letter == player_guess:
                display_word[i] = player_guess
    else:
        print(f"✗ Sorry, '{player_guess}' is not in the word.")  # incorrect guess
        error_letters.append(player_guess)
        guess -= 1
    
    # Check win/lose conditions
    if "_" not in display_word:
        print(hangman_stages[len(error_letters)])  # Show final hangman state
        print(f"\n🎉 Congratulations! You won! 🎉")
        print(f"The word was: {word}")
        Game = False
    elif guess == 0:
        print(hangman_stages[6])  # Show full hangman (game over)
        print(f"\n💀 Game Over! You've been hanged! 💀")
        print(f"The word was: {word}")
        Game = False

print("\nThanks for playing Hangman!") # end of game