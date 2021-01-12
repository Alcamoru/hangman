import random
# Write your code here
LIVES = 8

CHOICES = ["python", "java", "kotlin", "javascript"]
print("H A N G M A N")
CHOICE = list(random.choice(CHOICES))

hidden_word = list(len(CHOICE) * "-")

while LIVES > 0:
    print("\n" + "".join(hidden_word))
    user_input = input("Input a letter: ")

    if user_input in CHOICE:
        for i in range(len(CHOICE)):
            if CHOICE[i] == user_input:
                if hidden_word[i] == user_input:
                    print("No improvements")
                    LIVES -= 1
                    break
                else:
                    hidden_word[i] = user_input
    else:
        print("That letter doesn't appear in the word")
        LIVES -= 1

if "-" not in hidden_word:
    print(f"""{CHOICE}
You guessed the word!
You survived!""")
else:
    print("You lost!")
