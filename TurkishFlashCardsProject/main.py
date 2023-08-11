BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random
# button functions
current_card = {}
all_words = {}
def rightAnswer():
    all_words.remove(current_card)
    wrongAnswer()
    data = pandas.DataFrame(all_words)
    data.to_csv("data/words_left.csv", index = False)
def wrongAnswer():
    global current_card, flip_timer
    screen.after_cancel(flip_timer)
    current_card = random.choice(all_words)
    canvas.itemconfig(card_title, text="Turkish", fill="black")
    canvas.itemconfig(shown_word, text=current_card["Turkish"], fill="black")
    canvas.itemconfig(card_background, image=card_front)
    flip_timer = screen.after(3000, func=flipCard)

def flipCard():
    canvas.itemconfig(card_title, text= "English", fill="white")
    canvas.itemconfig(shown_word, text= current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back)



# screen
screen = Tk()
screen.title("Turkish Flash Cards")
screen.config(pady=50, padx=50,bg=BACKGROUND_COLOR)
flip_timer = screen.after(3000, func=flipCard)


# images
card_back = PhotoImage("file=images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")
right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

# canvas
canvas = Canvas(width=800, height=526,bg=BACKGROUND_COLOR)
canvas.config(highlightthickness= 0)
card_background = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400 ,150, text="title", font=("Arial", 40, "italic"))
shown_word = canvas.create_text(400 ,263, text="word", font=("Arial", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)


# buttons
wrong_button = Button()
wrong_button.config(image=wrong_image,highlightthickness= 0,command=wrongAnswer)
wrong_button.grid(column = 0, row= 1)
right_button = Button()
right_button.config(image=right_image,highlightthickness= 0, command=rightAnswer)
right_button.grid(column = 1, row= 1)

# pandas reader

try:
    data = pandas.read_csv("data/words_left.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/Translations.csv")
    all_words = original_data.to_dict(orient="records")
else:
    all_words = data.to_dict(orient="records")

wrongAnswer()

screen.mainloop()
