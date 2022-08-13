from tkinter import *
import random

font_set = ("Courel", 12, "bold")
DICE_ART = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
BG="#DADDDF"

def roll():
    dice1_art = random.choice(DICE_ART)
    dice2_art = random.choice(DICE_ART)
    dice1.config(text=dice1_art)
    dice2.config(text=dice2_art)

window = Tk()
window.title("Dice Rolling Simulator")
window.config(padx=10, pady=10, bg=BG)
window.resizable(width=False, height=False)

dice1 = Label(text='\u2685', font=("Courel", 220), bg=BG)
dice2 = Label(text='\u2685', font= ("Courel", 220), bg=BG)
dice1.grid(row=1, column=0, columnspan=1)
dice2.grid(row=1, column=1, columnspan=2)

roll_button = Button(text="Roll the Dice", font=font_set, command=roll)
roll_button.grid(row=2, column=2)

window.mainloop()


