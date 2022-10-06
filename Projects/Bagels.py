import random

print("""
    Bagels, a deductive logic game.
                By IBC

I am thinking of a 3-digit number. Try to guess what it is.

Here are some clues: 
When I say:    That means:
  Pico         One digit is correct but in the wrong position.
  Fermi        One digit is correct and in the right position.
  Bagels       No digit is correct.
I have thought up a number. \n""")


def create_random_number():
    random_number = random.randint(100, 999)
    guesses = 10
    print(random_number)
    return guesses, random_number


def check_number(guess_nr, random_nr):
    correct = 0
    pico = 0
    fermi = 0

    if guess_nr == random_nr:
        correct += 1
    else:
        list_guess_number = list(str(guess_nr))
        list_random_number = list(str(random_nr))
        index_1 = 0
        print(list_random_number, list_guess_number)

        for letter in list_random_number:
            index_2 = 0
            for letter_2 in list_guess_number:
                if letter_2 == letter:
                    if index_1 == index_2:
                        fermi += 1
                    else:
                        pico += 1
                index_2 += 1
            index_1 += 1
    return_dict = {
        "pico": pico,
        "fermi": fermi,
        "correct": correct,
    }

    return return_dict


guesses, random_number = create_random_number()
guess_number = 0

while True:

    guess_number = int(input(f"Guess #{guesses}:\n"))
    check_return = check_number(guess_number, random_number)

    if check_return.get("pico") > 0 or check_return.get("fermi", 0) > 0 and check_return.get("correct") == 0:
        print("Fermi " * check_return["fermi"], "Pico " * check_return["pico"])
        guesses -= 1
    elif check_return.get("pico") == 0 and check_return.get("fermi") == 0 and check_return["correct"] == 0:
        print("Bagels")
        guesses -= 1
    elif check_return.get("correct") == 1:
        print("You got it! \n")
        play_again = input("Do you want to play again? (yes or no)").lower()
        if play_again == "yes":
            guesses, random_number = create_random_number()
        elif play_again == "no":
            break
    if guesses == 0:
        print("You lose!")
        play_again = input("Do you want to play again? (yes or no)").lower()
        if play_again == "yes" or play_again == "y":
            guesses, random_number = create_random_number()
        elif play_again == "no" or play_again == "n":
            break
