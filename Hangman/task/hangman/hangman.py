import random

# Write your code here

user_action = input('Type "play" to play the game, "exit" to quit:')

if user_action == "play":
    LIVES = 8

    CHOICES = ["python", "java", "kotlin", "javascript"]
    print("H A N G M A N")
    CHOICE = list(random.choice(CHOICES))

    hidden_word = list(len(CHOICE) * "-")
    attempts = []

    while LIVES > 0:
        if hidden_word == list(CHOICE):
            break
        print("\n" + "".join(hidden_word))
        user_input = input("Input a letter: ")
        if len(user_input) > 1:
            print("You should input a single letter")
            continue
        elif not user_input.isalpha() or user_input.isupper():
            print("Please enter a lowercase English letter")
            continue

        if user_input in CHOICE:
            for i in range(len(CHOICE)):
                if CHOICE[i] == user_input:
                    if hidden_word[i] == user_input:
                        print("You've already guessed this letter")
                        break
                    else:
                        hidden_word[i] = user_input

        else:
            if user_input in attempts and user_input not in CHOICE:
                print("You've already guessed this letter")
            else:
                print("That letter doesn't appear in the wor"
                      "d")
                LIVES -= 1
                attempts.append(user_input)

    if "-" not in hidden_word:
        print(f"""{CHOICE}
    You guessed the word!
    You survived!""")
    else:
        print("You lost!")
