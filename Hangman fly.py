import random
words = ["python", "programming", "hangman", "developer", "keyboard"]
word_to_guess = random.choice(words)
guessed_word = ["_"] * len(word_to_guess)
guessed_letters = set()
tries = 3
print("Welcome to Hangman!")
while tries > 0:
    print("Current word: ", " ".join(guessed_word))
    print(f"Guessed letters: {', '.join(guessed_letters)}")
    print(f"Attempts remaining: {tries}")
    
    guess = input("Enter a letter: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

        if guess in guessed_letters:
            print(f"You've already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word_to_guess:
            print(f"Good job! The letter '{guess}' is in the word.")
            for i in range(len(word_to_guess)):
                if word_to_guess[i] == guess:
                    guessed_word[i] = guess
        else:
            print(f"Oops! The letter '{guess}' is not in the word.")
            tries-= 1

        if " ".join(guessed_word) == word_to_guess:
            print(f"\nCongratulations! You've guessed the word: {word_to_guess}")
            break
    else:
        print(f"\nGame over! The word was: {word_to_guess}")
