from tkinter import *
import time, datetime , math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 20
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
finished_work = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps, finished_work
    window.after_cancel(timer)
    reps = 0
    finished_work = 0
    canvis.itemconfig(timer_text, text="00:00")
    check_mark_text.config(text="")
    timer_texts.config(text="Timer")
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps, finished_work
    work_sec = WORK_MIN * 60
    short_brake_sec = SHORT_BREAK_MIN * 60
    long_brake_sec = LONG_BREAK_MIN * 60
    reps += 1

    if (reps % 2) != 0:
        timer_texts.config(text="Work Time", fg=GREEN)
        count_down(work_sec)

    else:
        timer_texts.config(text="Brake", fg=RED)
        if (reps % 8) == 0:
            count_down(long_brake_sec)
        else:
            count_down(short_brake_sec)
    if reps % 2 == 0 and reps > 1:
        finished_work += "✓"
        check_mark_text.config(text=finished_work)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global reps, timer

    if count > 0:
        displayed_minutes = math.floor(count / 60)
        displayed_seconds = count % 60
        if displayed_seconds < 10:
            displayed_seconds = f"0{displayed_seconds}"

        if displayed_minutes < 10:
            displayed_minutes = f"0{displayed_minutes}"
        canvis.itemconfig(timer_text, text=f"{displayed_minutes}:{displayed_seconds}")
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()




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

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

check_mark_text = Label(bg=PINK, fg=GREEN, font=(FONT_NAME, 30, "bold"))
check_mark_text.grid(column=1, row=4, )



window.mainloop()