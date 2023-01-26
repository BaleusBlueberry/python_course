import pandas

BACKGROUND_COLOR = "#B1DDC6"
from pandas import *
from tkinter import *
import random
import pathlib

# import list of words:
try:
    data = read_csv("words_to_learn.csv")

    datasave = "words_to_learn"
except:
    data = read_csv("data.csv")
    datasave = "data"
    print("took regular data")

list_of_words = data.to_dict("records")
total_words_left = len(list_of_words)
print(total_words_left)
wrongly_guessed = []

#########

# when clicking on the right button
def right():
    if total_words_left > 0:
        save_wrong_progress("right")
    choose_word()
    show_swedish_word()


# when clicking on the wrong button
def wrong():
    if total_words_left > 0:
        save_wrong_progress("wrong")
    choose_word()
    show_swedish_word()


# save progress to the correct place
def save_wrong_progress(choice):
    if datasave == "words_to_learn":

        if choice == "right":
            remove_word_from_list()
            data_frame = pandas.DataFrame(list_of_words)
            data_frame.to_csv("words_to_learn.csv", index=False)

        elif choice == "wrong":
            pass

    elif datasave == "data":

        if choice == "right":
            data_frame = pandas.DataFrame(list_of_words)
            data_frame.to_csv("data.csv", index=False)

        elif choice == "wrong":
            if chosen_words not in wrongly_guessed:
                wrongly_guessed.append(chosen_words)
                data_frame = pandas.DataFrame(wrongly_guessed)
                data_frame.to_csv("words_to_learn.csv", index=False)


# removing one element from the list
def remove_word_from_list():
    global total_words_left
    print(list_of_words)
    list_of_words.pop(chosen_number)
    print(list_of_words)

    total_words_left -= 1
    if total_words_left <= 0:
        file = pathlib.Path("words_to_learn.csv")
        file.unlink()


# randomly choose a word and display it
def choose_word():
    global chosen_number
    global chosen_words
    chosen_number = random.randint(0, total_words_left - 1)
    chosen_words = list_of_words[chosen_number]
    print(f"chosen number is {chosen_number} and chosen list is {chosen_words}")

# show the swidish card
def show_swedish_word():
    global wait_time
    window.after_cancel(wait_time)
    card.itemconfig(title_front_card, text="Swedish", fill="black")
    card.itemconfig(word_front_card, text=chosen_words["Swedish"], fill="black")
    card.itemconfig(card_image, image=front_image)
    wait_time = window.after(3000, show_english_word)


# shows the English word
def show_english_word():
    card.itemconfig(title_front_card, text="English", fill="white")
    card.itemconfig(word_front_card, text=chosen_words["English"], fill="white")
    card.itemconfig(card_image, image=back_image)


# creating the window:
window = Tk()
window.title("Language Card Memory")
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

# creating front card:
back_image = PhotoImage(file="images/card_back.png")
front_image = PhotoImage(file="images/card_front.png")
card = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_image = card.create_image(400, 260, image=front_image, anchor="center")

# front card text:
title_front_card = card.create_text(400, 150, text="Title", fill="black", font=("Ariel", 40, "italic"))
word_front_card = card.create_text(400, 263, text="Word", fill="black", font=("Ariel", 60, "bold"))

# check marks
right_button_image = PhotoImage(file="images/right.png")
wrong_button_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_button_image, command=wrong)
right_button = Button(image=right_button_image, command=right)

# placing elements
card.grid(column=1, row=1, columnspan=2, rowspan=4)
wrong_button.grid(column=1, row=5)
right_button.grid(column=2, row=5)

choose_word()
card.itemconfig(title_front_card, text="Swedish", fill="black")
card.itemconfig(word_front_card, text=list_of_words[chosen_number]["Swedish"], fill="black")
card.itemconfig(card_image, image=front_image)
wait_time = window.after(3000, show_swedish_word)

window.mainloop()
