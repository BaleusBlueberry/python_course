from tkinter import *
import time, datetime , math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 5
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
finished_work = ""

def start_timer():
    global reps
    global finished_work
    work_sec = WORK_MIN * 1
    short_brake_sec = SHORT_BREAK_MIN * 1
    long_brake_sec = LONG_BREAK_MIN * 1
    reps += 1
    print(reps)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Tomatos")
window.config(padx=100, pady=50, bg=PINK)


image_tomato = PhotoImage(file="tomato.png")
canvis = Canvas(width=200, height=224, bg=PINK, highlightthickness=0)
canvis.create_image(100, 112, image=image_tomato)
timer_text = canvis.create_text(101, 125, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvis.grid(column=1, row=1)

timer_texts = Label(text="Timer", bg=PINK, fg=GREEN, font=(FONT_NAME, 40, "bold"))
timer_texts.grid(column=1, row=0)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset")
reset_button.grid(column=2, row=2)

check_mark_text = Label(bg=PINK, fg=GREEN, font=(FONT_NAME, 30, "bold"))
check_mark_text.grid(column=1, row=4, )



window.mainloop()