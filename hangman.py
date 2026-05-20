import random
words = ["apple", "mango", "grapes", "banana", "orange", "computer", "python", "trophy", "cybersecurity", "dream", "achievement"]
word = random.choice(words)
guessed_letters = []
tries = 5
print("❤️ Welcome to Hangman Game ❤️")
while tries > 0:
    display_word = ""
    print("Lives:", "❤️ " *tries)
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("\nWord:",display_word)
    if "_" not in display_word:
        print("🎉 Congratulations! You Won!")
        break
    guess = input("Guess a letter:").lower()
    if guess in guessed_letters:
        print("You already guessed that letter!")
    elif guess in word:
        guessed_letters.append(guess)
        print("Correct Guess!")
    else:
        tries -= 1
        print("Wrong Guess!")
    if tries == 0:
        print("\n💀 Game Over!")
        print("The word was:", word)
    
