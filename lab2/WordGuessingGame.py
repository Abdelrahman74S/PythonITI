import random

words = ["apple", "banana", "grape", "orange", "mango"]
word = random.choice(words)
guess = ["_"] * len(word)
numtry = 5

print(words)
print(guess)

while numtry > 0:
    w = input("Enter the word: ")

    if w in word:
        for i in range(len(word)):
            if word[i] == w:
                guess[i] = w
        print("".join(guess))

    else:
        numtry -= 1
        print("no")
        continue

    if "_" not in guess:
        print("you gussed the word")
        print(f"the word is {word}")
        break
if numtry == 0:
    print("game over:")
