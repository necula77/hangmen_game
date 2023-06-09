
import json
from random import randint

def update_word(word, guessed_letter, secret_word):
    updated_word = ""
    for i in range(len(secret_word)):
        if secret_word[i] == guessed_letter:
            updated_word += guessed_letter + " "
        else:
            updated_word += word[2*i:2*i+2]  # Adjust index to skip spaces
    return updated_word.strip()


player_name = input("Introduceti numele dvs: \n >> ")
life = 10
guess = False

with open("fisier.json", "r") as file:
    data = file.read()
    data = json.loads(data)

cuvant = data["words"]
random_index = randint(0, len(cuvant) - 1)
hangman = cuvant[random_index]
guess_word = "_ " * len(hangman)

while life != 0 and guess_word.strip() != hangman:
    guess_letter = input("Introduceti litera: \n >> ")
    if guess_letter in hangman:
        guess_word = update_word(guess_word, guess_letter, hangman)
        print(guess_word)
        print("Ai gasit o litera.")
    else:
        life -= 1
        print(f"Ai gresit, mai ai {life} incercari.")

    if guess_word.replace(" ","") == hangman:
        print(f"Felicitari {player_name}, ai ghicit cuvantul: {hangman}.")
        guess = True
        break

if life == 0:
    print("Ai pierdut!")

