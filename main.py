from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text = "00:00")
    label_timer.config(text = 'Timer')
    label_checkmark.config(text='')
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        label_timer.config(text = 'Break', fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label_timer.config(text='Break', fg=PINK)
    else:
        count_down(work_sec)
        label_timer.config(text='Work', fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    # format the date
    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    # update the canvas
    canvas.itemconfig(timer_text, text = f'{count_min}:{count_sec}')
    if count >0:
        global timer
        timer = window.after(1000, count_down, count-1) # 1 second= 1000 ms
    else:
        start_timer()
        marks = ''
        work_sessions = reps//2
        for _ in range(work_sessions):
            marks += '✔'
        label_checkmark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx= 100, pady= 50, bg=YELLOW)

# create the canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightbackground=YELLOW)
tomato_img = PhotoImage(file = 'tomato.png')
canvas.create_image(103,112, image=tomato_img)
timer_text = canvas.create_text(103,130,text = "00:00", fill='white', font=(FONT_NAME, 35,"bold"))
canvas.grid(column= 1, row=1)

# create the labels
# timer label
label_timer = Label(text="Timer", font=(FONT_NAME, 50,"bold"), fg=GREEN, bg=YELLOW)
label_timer.grid(column=1,row=0)

# checkmark label
label_checkmark = Label(font=(FONT_NAME, 40,"bold"), fg=GREEN, bg=YELLOW)
label_checkmark.grid(column=1,row=3)

# create the buttons
button_start = Button(text="Start", command=start_timer, highlightbackground=YELLOW)
button_start.grid(column=0,row=2)

button_reset = Button(text="Reset", command=reset_timer, highlightbackground=YELLOW)
button_reset.grid(column=2,row=2)

window.mainloop()