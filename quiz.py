import tkinter as tk

from collections import defaultdict
from pygame import mixer
from random import randint

from settings import *


def display_question_label(row: int, col: int) -> None:
    mixer.music.load(SND_CLOCK)
    mixer.music.play(loops=4)

    q = questions_list[categories[col]][row*100][0]
    question_label = tk.Label(
        root,
        text = q,
        font = ('Helvetica', 40),
        bg = 'yellow',
        wraplength = 1500,
        justify = 'center'
    )
    question_label.grid(
        row = 1,
        rowspan = num_rows,
        column = 1,
        columnspan = num_columns,
        sticky = 'nsew'
    )

    yes_button = tk.Button(
        root,
        text = row * 100,
        command = lambda: handle_answer(
            True, row, col, question_label,
            yes_button, no_button, answer_button
        ),
        font = ('Helvetica', 16),
        bg = 'green'
    )
    yes_button.grid(row = num_rows + 1, column = 4, sticky = 'nsew')

    no_button = tk.Button(
        root,
        text = '0',
        command = lambda: handle_answer(
            False, row, col, question_label,
            yes_button, no_button, answer_button,
        ),
        font = ('Helvetica', 16),
        bg = 'red'
    )
    no_button.grid(row = num_rows + 1, column = 3, sticky = 'nsew')

    answer_button = tk.Button(
        root,
        text = 'Ответ',
        command = lambda: display_answer_label(row, col, question_label),
        font = ('Helvetica', 16),
        bg = 'blue'
    )
    answer_button.grid(row = num_rows + 1, column = 0, sticky = 'nsew')

    
def display_answer_label(row: int, col: int, question_label: tk.Label) -> None:
    ans = questions_list[categories[col]][row*100][1]
    question_label.config(text = ans)


def handle_answer(
        answer: bool, row: int, col: int, question_label: tk.Label,
        yes_button: tk.Button, no_button: tk.Button, answer_button: tk.Button,
    ) -> None:
    global score1, score2, counter
    counter += 1
    print(counter, answer)
    color = 'red'
    if answer:
        color = 'lightgreen'
        if counter % 2:
            score1 += row * 100
        else:
            score2 += row * 100
        teams[0].config(text = f'{TEAM1}\n{score1}')
        teams[1].config(text = f'{TEAM2}\n{score2}')
    if counter % 2:
        bg1 = 'lightgray'
        bg2 = 'lightblue'
    else:
        bg1 = 'lightblue'
        bg2 = 'lightgray'
    teams[0].config(bg = bg1)
    teams[1].config(bg = bg2)
    buttons[row][col].config(bg = color)

    num = randint(0, 3)
    mixer.music.load(SND_PAUSE[num])
    mixer.music.play(loops=5)

    question_label.destroy()
    yes_button.destroy()
    no_button.destroy()
    answer_button.destroy()


def create_grid(rows: int, columns: int) -> None:
    for row in range(rows):
        for col in range(columns):
            if row == 0:
                # Create LabelFrame for the first row
                label_frame = tk.Label(
                    root,
                    text = categories[col],
                    font = ('Helvetica', 20)
                )
                label_frame.grid(row=row, column=col, sticky='nsew')
            elif col == 0:
                if row == 1:
                    label_frame = tk.Label(
                        root,
                        text = f'{TEAM1}\n{score1}',
                        font = ('Helvetica', 20), bg = 'lightblue'
                    )
                    label_frame.grid(row = row, column = col, sticky = 'nsew')
                    teams[0] = label_frame
                if row == 2:
                    label_frame = tk.Label(
                        root,
                        text = f'{TEAM2}\n{score2}',
                        font = ('Helvetica', 20)
                    )
                    label_frame.grid(row = row, column = col, sticky = 'nsew')
                    teams[1] = label_frame
            else:
                # Create buttons for other rows
                button = tk.Button(
                    root,
                    text = f'{row}00',
                    command = lambda r=row, c=col: display_question_label(r, c),
                    font = ('Helvetica', 20)
                )
                button.grid(
                    row = row, column = col,
                    padx = 5, pady = 5,
                    sticky = 'nsew'
                )
                buttons[row][col] = button


# Read and store questions from .txt file
questions_list = defaultdict(lambda: defaultdict(int))
with open(QUESTIONS, 'r', encoding='utf8') as f:
    question_data = f.readlines()
for line in question_data:
    q = line.replace('\n', '').split(';')
    questions_list[q[0]][int(q[1])] = [q[2], q[3]]
categories = ['Команды'] + [x for x in questions_list]

# Create the main window
root = tk.Tk()
root.title('Квиз')

# Set the window size to the screen size
root.geometry(f'{root.winfo_screenwidth()}x{root.winfo_screenheight()}')

# Specify the number of rows and columns in the grid and scores
num_rows = 6
num_columns = 7
score1 = 0
score2 = 0
teams = [None, None]
counter = 0

# Initialize a list to hold references to buttons
buttons = [[None for _ in range(num_columns)] for _ in range(num_rows)]

# Create the grid of buttons and LabelFrame
create_grid(num_rows, num_columns)

# Music control
mixer.init()
mixer.music.load(INTRO)
mixer.music.play()

# Configure row and column weights to make the buttons and LabelFrame expand with the window
for i in range(num_rows):
    root.grid_rowconfigure(i, weight=1)
for i in range(num_columns):
    root.grid_columnconfigure(i, weight=1)

# Start the Tkinter event loop
root.state('zoomed')
root.mainloop()
