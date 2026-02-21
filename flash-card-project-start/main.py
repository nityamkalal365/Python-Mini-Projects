from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
sample={}

try:
    words = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    org_words= pandas.read_csv("./data/french_words.csv")
    sample=org_words.to_dict(orient="records")
else:
    sample = words.to_dict(orient="records")
current_card={}
def show_word():
    global current_card,timer
    window.after_cancel(timer)
    current_card=random.choice(sample)
    canvas.itemconfig(lang_text, text='French', fill="black")
    canvas.itemconfig(keyword, text=f"{current_card["French"]}", fill="black")
    canvas.itemconfig(main_frame, image=front_img)
    timer=window.after(3000,func=eng)


def eng():
        canvas.itemconfig(main_frame,image=back_image)
        canvas.itemconfig(lang_text,text="English",fill="white")
        canvas.itemconfig(keyword,text=f"{current_card["English"]}",fill="white")

def known_word():
    sample.remove(current_card)
    remain=pandas.DataFrame(sample)
    remain.to_csv("./data/words_to_learn.csv",index=False)
    show_word()


window = Tk()
window.title("Flash Cards")
timer=window.after(3000,func=eng)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR ,highlightthickness=0)
front_img = PhotoImage(file="./images/card_front.png")
main_frame=canvas.create_image(400, 263, image=front_img)
lang_text=canvas.create_text(400, 150, text="French", fill="black", font=("Ariel",40, "italic"))
keyword=canvas.create_text(400,263,text="Word",fill="black",font=("Ariel",60,"bold"))
tick=PhotoImage(file="./images/right.png")
cross=PhotoImage(file="./images/wrong.png")
back_image=PhotoImage(file="./images/card_back.png")
tick_button=Button(image=tick,highlightthickness=0,command=known_word)
cross_button=Button(image=cross,highlightthickness=0,command=show_word)
canvas.grid(row=0,column=0,columnspan=2)
tick_button.grid(row=1,column=1)
cross_button.grid(row=1,column=0)
show_word()

window.mainloop()