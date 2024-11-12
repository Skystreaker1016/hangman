print("\033[1m" + "\033[4m" + "- Welcome to Hangman -" + "\033[0m")
print("""HOW TO PLAY:
- Type in a word for a friend to guess
- Guess letters to form the word
- Correct letters will appear in their places in the word, while wrong letters will count against you
- You have 6 wrong letters before the word is revealed
Good luck!
""")

chances=6

while True:
    answer=input("Your word: ").lower()
    for letter in answer:
        print("_ ")
    print("Chances:", chances)

    guess=input("Guess a letter: ").lower()
    if letter in answer:
        print("\033[0;32m" + "Correct!" + "\033[0m")
