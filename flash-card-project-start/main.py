import pandas as pd
from tkinter import *
from tkinter import messagebox
import random

BACKGROUND_COLOR = "#B1DDC6"
data_dict={}
current_card={}

try:
    data=pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data=pd.read_csv("data/french_words.csv")
    data_dict=original_data.to_dict(orient="records")
else:
    data_dict=data.to_dict(orient="records")


def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card=random.choice(data_dict)
    canvas.itemconfig(canvas_title,text="French",fill="Black")
    canvas.itemconfig(canvas_word,text=current_card["French"],fill="Black")
    canvas.itemconfig(card_background,image=card_front_image)
    flip_timer= window.after(4000, func=flip_card)

def is_known():
    data_dict.remove(current_card)
    data_to_learn=pd.DataFrame(data_dict)
    data_to_learn.to_csv("data/words_to_learn.csv",index=False)
    next_card()

def flip_card():
    canvas.itemconfig(canvas_title,text="English",fill="White")
    canvas.itemconfig(canvas_word,text=current_card["English"],fill="White")
    canvas.itemconfig(card_background,image=canvas_backimage)

window=Tk()
window.title("FLASH CARD GAME")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer=window.after(4000,func=flip_card)

canvas=Canvas(width=800,height=526,highlightthickness=1)
card_front_image=PhotoImage(file="images/card_front.png")
canvas_backimage=PhotoImage(file="images/card_back.png")
card_background=canvas.create_image(400,263,image=card_front_image)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas_title=canvas.create_text(400,150,text="",font=("Arial",40,"italic"))
canvas_word=canvas.create_text(400,263,text="",font=("Arial",60,"bold"))
canvas.grid(column=0,row=0,columnspan=2)

check_image=PhotoImage(file="images/right.png")
check_button=Button(image=check_image,highlightthickness=0,command=is_known)
check_button.grid(row=1,column=0)

wrong_image=PhotoImage(file="images/wrong.png")
wrong_button=Button(image=wrong_image,highlightthickness=0,command=next_card)
wrong_button.grid(row=1,column=1)

next_card()

window.mainloop()



