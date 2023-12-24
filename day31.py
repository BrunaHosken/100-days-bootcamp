from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"
random_word = {}
words_to_learn= {}


#CSV 

try:
    data = pandas.read_csv("./flash_card_files/data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./flash_card_files/data/french_words.csv")
    words_to_learn = original_data.to_dict(orient="records")
else:
    words_to_learn = data.to_dict(orient="records")



def flip_card():
    text_english = random_word["English"]
    canvas.itemconfig(language_text, text = "English", fill = "white")
    canvas.itemconfig(word_text, text = text_english, fill = "white")
    canvas.itemconfig(canvas_image, image=photoimage_back)
    


def next_card():
    global random_word, flip_timer
    window.after_cancel(flip_timer)

    random_word = random.choice(words_to_learn)
    text_french = random_word["French"]
    
    canvas.itemconfig(language_text, text = "French", fill='black')
    canvas.itemconfig(word_text, text = text_french, fill='black')
    canvas.itemconfig(canvas_image, image=photoimage_front)

    flip_timer = window.after(3000, flip_card)
    

def known_card():
    words_to_learn.remove(random_word)
    new_data = pandas.DataFrame(words_to_learn)
    new_data.to_csv("./flash_card_files/data/words_to_learn.csv", index=False)
    if(len(words_to_learn)==0):
        canvas.itemconfig(language_text, text = "You don't have words to learn", fill='black')
        canvas.itemconfig(word_text, text = "Congratulations!!", fill='black')
        wrong_button.config(state="disable")
        right_button.config(state="disable")
        window.after_cancel(flip_timer)
    else:
        next_card()


#CANVAS
window = Tk()
window.title("Flashy")
window.config(padx = 50, pady = 50, bg = BACKGROUND_COLOR)

has_words = len(words_to_learn)>1

state = "normal"
if has_words:
    flip_timer = window.after(3000, flip_card)
else:
    state = "disabled"

canvas = Canvas(width = 800, height = 526, highlightthickness = 0, bg = BACKGROUND_COLOR)
photoimage_front = PhotoImage(file = "./flash_card_files/images/card_front.png")
photoimage_back = PhotoImage(file = "./flash_card_files/images/card_back.png")
canvas_image = canvas.create_image(400, 263, image = photoimage_front)
canvas.grid(column = 1, row = 0, sticky="EW")

language_text = canvas.create_text(400, 150, text = "You don't have words to learn", fill = "black", font = (FONT_NAME, 40, "italic"))
word_text = canvas.create_text(400, 263, text = "Congratulations!!", fill = "black", font = (FONT_NAME, 60, "bold"))
canvas.grid(column = 0, row = 0, columnspan=2, sticky="EW")


#Buttons
wrong_image = PhotoImage(file="./flash_card_files/images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, bg = BACKGROUND_COLOR, command=next_card, state=state)
wrong_button.grid(column = 0, row = 1, sticky="EW")

right_image = PhotoImage(file="./flash_card_files/images/right.png")
right_button = Button(image=right_image, highlightthickness=0, bg = BACKGROUND_COLOR, command=known_card, state=state)
right_button.grid(column = 1, row = 1, sticky="EW")


if has_words:
    next_card()


window.mainloop()