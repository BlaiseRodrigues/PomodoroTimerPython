from tkinter import *
import time, math


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 10
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    tomato_ticks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer(**kwargs):
    global reps
    reps+=1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps%8==0:
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    elif reps%2==0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_minutes = math.floor(count / 60)
    if count_minutes < 10:
        count_minutes = '0' + str(count_minutes)

    count_seconds = count % 60
    if count_seconds == 0:
        count_seconds = '00'
    elif count_seconds < 10:
        count_seconds = '0' + str(count_seconds)
    canvas.itemconfig(timer_text, text=f'{count_minutes}:{count_seconds}')
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks =""
        for _ in range(math.floor(reps/2)):
            marks+="🍅"
        tomato_ticks.config(text=marks, bg=YELLOW)


    # print(count)
    # if count >= 0:
    #     time_left = time.strftime("%M:%S", time.gmtime(count))
    #     canvas.itemconfig(timer_text, text=time_left)
    #     window.after(1000, count_down, count-1)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro Timer')
window.config(padx=100, pady=50, bg=YELLOW)



timer_label = Label(text='Timer', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 25, 'bold'))
# timer_label.config(pady=30)
timer_label.grid(row=0, column =1)

canvas = Canvas(width=300, height=225, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file='tomato.png')
canvas.create_image(140,105, image=image)
timer_text = canvas.create_text(140,125, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(row=1, column=1)


start_butoon = Button(text="Start", command=start_timer, highlightthickness=0)
start_butoon.grid(row=2, column=0)

reset_button = Button(text="Reset", command=reset_timer, highlightthickness=0)
reset_button.grid(row=2, column=2)

tomato_ticks = Label(text='')
tomato_ticks.config(bg=YELLOW, fg='red')
tomato_ticks.grid(row=3, column=1)



window.mainloop()