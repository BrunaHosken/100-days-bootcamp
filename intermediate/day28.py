# Pomodoro GUI
from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_time():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text = f"00:00")
    timer_label.config(text="Timer", fg = GREEN)
    check_marks.config(text="")
    start_button.config(state="normal")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    window.bell()
    start_button.config(state="disabled")
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    window.attributes('-topmost', 1)
    window.attributes('-topmost', 0)

    if reps % 8 == 0:
        timer_label.config(text="Break", fg = RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        timer_label.config(text="Break", fg = PINK )
        count_down(short_break_sec)
    else:
        timer_label.config(text="Work", fg = GREEN)
        count_down(work_sec)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count%60
    
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count > 0:
       global timer
       timer =  window.after(1000, count_down, count - 1)
    else:
        window.bell()
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"

        check_marks.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx = 100, pady = 50, bg = YELLOW)

canvas = Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness = 0)
photoimage = PhotoImage(file = "./pomodoro_files/tomato.png")
canvas.create_image(100, 112, image = photoimage)
timer_text = canvas.create_text(103, 135, text = "00:00", fill = "white", font = (FONT_NAME, 35, "bold"))
canvas.grid(column = 1, row = 1)


timer_label = Label(text="Timer", fg = GREEN, bg = YELLOW, font = (FONT_NAME, 50, "bold"))
timer_label.grid(column = 1, row = 0)

start_button = Button(text = "Start", highlightthickness = 0, command = start_timer)
start_button.grid(column = 0, row = 2)

reset_button = Button(text = "Reset", highlightthickness = 0, command = reset_time)
reset_button.grid(column = 2, row = 2)

check_marks = Label(fg = GREEN, bg = YELLOW, font = (FONT_NAME, 20, "bold"))
check_marks.grid(column = 1, row = 3)

window.mainloop()
