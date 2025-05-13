import random

hangman_pics = [
    '''
     +---+
     |   |
         |
         |
         |
         |
    =========''', 
    '''
     +---+
     |   |
     O   |
         |
         |
         |
    =========''', 
    '''
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========''', 
    '''
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========''', 
    '''
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========''', 
    '''
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========''', 
    '''
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    ========='''
]

words = ["python", "developer", "programming", "keyboard", "monitor", "internet", "security", "function"]

word = random.choice(words)
word_display = ["_" for _ in word]
guessed_letters = []
lives = 6

print("=== Welcome to Hangman Pro! ===")
print("Guess the word before the man is hanged!")

while lives > 0 and "_" in word_display:
    print(hangman_pics[6 - lives])
    print("Word:", " ".join(word_display))
    print("Guessed letters:", ", ".join(guessed_letters))
    print("Lives remaining:", lives)

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.\n")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Nice! You guessed a correct letter.\n")
        for i in range(len(word)):
            if word[i] == guess:
                word_display[i] = guess
    else:
        print("Oops! That letter is not in the word.\n")
        lives -= 1

if "_" not in word_display:
    print("🎉 Congratulations! You saved the man!")
    print("The word was:", word)
else:
    print(hangman_pics[6])
    print("💀 Game Over! The man has been hanged!")
    print("The word was:", word)
