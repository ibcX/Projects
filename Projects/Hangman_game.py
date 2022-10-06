
import random

words = ['casa', 'python', 'masina', 'autobuz']

chosen_word = words[random.randint(0, len(words) - 1)]
print(chosen_word)
lives = 3
print(f"Identificați din maxim {lives} incercări cuvântul: ")
guess_word = "_" * len(chosen_word)
print(guess_word)
guess_word = list(guess_word)
print_word = ""


def letter_verif(input_letter):
    i = 0
    for letter in chosen_word:
        if letter == input_letter:
            guess_word[i] = input_letter
            i += 1
        else:
            i += 1
    return guess_word


def count_lives(lives, input_letter):
    if input_letter not in chosen_word:
        lives = lives - 1
    elif input_letter in guess_word:
        lives = lives - 1
        print("Ai identificat deja litera asta, fraiere!")
    return lives


while print_word != chosen_word and lives > 0:
    input_letter = input("Introduceti o litera: ")

    lives = count_lives(lives, input_letter)
    letter_verif(input_letter)

    print_word = ""
    for letter in guess_word:
        print_word = print_word + letter
    if print_word == chosen_word:
        print(print_word)
        print("Felicitări, ai câștigat!")

    elif lives == 0:
        print("Ai pierdut!")
    elif lives == 1:
        print(print_word)
        print(f"Mai ai o încercare!")
    else:
        print(print_word)
        print(f"Mai ai {lives} incercari!")


