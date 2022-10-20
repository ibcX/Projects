from cProfile import label
from tkinter import *
import random
from tkinter.font import BOLD
root = Tk()
root.title ("Hangman game")
root.geometry("570x410")

canvas=Canvas(root, width=270, height=300, bg="white")
canvas.grid(row=2, rowspan=4, column=2, columnspan=3)

canvas.create_line(140, 250, 170, 170, width=5)  # left
canvas.create_line(200, 250, 170, 170, width=5)  # right
canvas.create_line(170, 170, 170, 10, width=5) # pillar
canvas.create_line(50, 10, 173, 10, width=5) # horizontal


welcome_label = Label(root, text="Bine ați venit la jocul Hangman!", pady=0)
welcome_label.grid(row=1, column=0)

label1 = Label(root, text="Identificați din maxim 6 incercări cuvântul: ", pady=5, padx=5)
label1.grid(row=3, column =0)

nr_cuvinte = Label(root, text="Numarul de cuvinte identificate corect: 0\nNumarul de cuvinte neidentificate: 0", pady=5, padx=5)
nr_cuvinte.grid(row=2, column =0)

input_field = Entry(root, width=20, borderwidth=2, state="disabled")
input_field.grid(column=0, row=5)

guess_label = Label(root, text="", font=30)
guess_label.grid(row=4, column=0)

lives_label = Label(root, text="", font=10, padx=20)
lives_label.grid(row=6, column=0)

new_record_label = Label(root, text="", font=(BOLD, 13), padx=50)
new_record_label.grid(row=7, column=0)

score_label = Label(root, text="Scor: 0", font=(BOLD, 13))
score_label.grid(row=1, column=2)
score = 0

record_label = Label(root, text="Record: 0", font=(10))
record_label.grid(row=1, column=3)
record = 0

nr_cuvinte_corecte = 0
nr_cuvinte_gresite = 0

def remove_text():
    guess_label.config(text="")
    lives_label.config(text="", font="normal", fg="#020318")
    score_label.config(text="Scor: 0")
    new_record_label.config(text="")

def start_function ():
    global chosen_word
    global input_letter
    global print_word
    global lives
    global guess_word
    global input_field
    global guess_label
    global lives_label
    global score
    remove_text()

    input_field.config(state="normal")

    canvas.delete("head", "left_arm", "right_arm", "body", "left_foot", "right_foot", "rope")
    words = ['casa', 'python', 'masina', 'autobuz', "elefant", "masa", "televizor", "caine", "pisica", "calculator", "menta", "lumina", "lama", "carte", "engleza", "situatie"]

    chosen_word = words[random.randint(0, len(words) - 1)]
    print(chosen_word)
    input_letter=""
    print_word = "_ " * len(chosen_word)
    guess_label.config(text=f"{print_word}")

    lives = 6
    score = 0
    guess_word = list("_" * len(chosen_word))


start_button = Button(root, text= "Start", font=("Calibri",14,"bold"), command=start_function)
start_button.grid(row=6, column=1, columnspan=2)


# start_button.bind("<Return>", start_function)

def count_lives(letter_in_word):
    global lives
    if letter_in_word == False:
        lives = lives - 1
    if lives > 0:
        start_button.config(text="Restart")
    lives_label.config(text=f"Mai ai {lives} incercari!")

    if lives < 6:
        canvas.create_oval(70, 50, 30, 90, width=5, tag="head")  # head
        if lives < 5:
            canvas.create_line(50, 150, 50, 90, width=5, tag="body")  # body
            if lives < 4:
                canvas.create_line(0, 120, 50, 90, width=5, tag="left_arm")  # left arm
                if lives < 3:
                    canvas.create_line(100, 120, 50, 90, width=5, tag="right_arm")  # right arm
                    if lives < 2:
                        canvas.create_line(0, 200, 50, 150, width=5, tag="left_foot")  # left foot
                        if lives <1:
                            canvas.create_line(100, 200, 50, 150, width=5, tag="right_foot")  # right foot
                            canvas.create_line(50, 10, 50, 55, fill='red', dash=(10, 5), width=3, tag="rope")  # rope

    if lives == 0:
        input_field.config(state="disabled")
    # return lives

def letter_verif(input_letter):
    global guess_word
    global print_word
    global nr_cuvinte_corecte
    global nr_cuvinte_gresite

    i = 0
    for letter in chosen_word:
        if letter == input_letter:
            guess_word[i] = input_letter
            i += 1
        else:
            i += 1
    if lives == 0:
        lives_label.config(text=f"Ai pierdut!", fg='#f00', font=(BOLD, 15))
        nr_cuvinte_gresite += 1
    if guess_word == list(chosen_word):
        lives_label.config(text=f"Felicitari, ai castigat!", fg='lime green', font=(BOLD, 15))
        input_field.config(state="disabled")
        nr_cuvinte_corecte += 1
    nr_cuvinte.config(text=f"Numarul de cuvinte identificate corect: {nr_cuvinte_corecte}\nNumarul de cuvinte neidentificate: {nr_cuvinte_gresite}")

    return guess_word

def score_calc(letter_in_word):
    global score
    if letter_in_word == True:
        score = score + 100
    elif letter_in_word == False:
        score = score - 50
    return score

def store_letter(event):
    global guess_word
    global print_word
    global record

    input_letter = input_field.get()
    input_field.delete(0, END)
    if len(input_letter.strip(" ")) > 0:
        if input_letter in chosen_word:
            if input_letter in guess_word:
                letter_in_word = False
            else:
                letter_in_word = True
        else:
            letter_in_word = False

        if lives > 0:
            count_lives(letter_in_word)
            letter_verif(input_letter)
            score_calc(letter_in_word)

        print_word = ""
        for letter in guess_word:
            print_word = print_word + " " + letter
        score_label.config(text=f"Scor: {score}")
        guess_label.config(text=f"{print_word}")

        if guess_word == list(chosen_word):
            if score > record:
                record = score
                record_label.config(text=f"Record: {record}")
                new_record_label.config(text="Nou record!", font=(BOLD, 15))

def close():
   root.quit()

exit_button = Button(root, text= "Close the Window", font=("Calibri",14,"bold"), command=close)
exit_button.grid(row=6, column=3, columnspan=2)

root.bind('<Return>', store_letter)

root.mainloop()