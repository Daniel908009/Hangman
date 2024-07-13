# necesary imports
import tkinter
import time
import random

# function to reset the game
def reset():
    global word, length
    # deleting everything in the canvas
    canvas.delete("all")
    # picking a new random word
    word = random.choice(words)
    # getting the length of the word
    length = len(word)
    # creating a new word label
    word_label.config(text="_ " * length)
    window.update()

# function to apply the settings
def apply_settings():
    pass

# function for the settings window
def settings():
    settings_window = tkinter.Toplevel(window)
    settings_window.title("Settings")
    settings_window.geometry("300x200")
    settings_window.resizable(False, False)
    settings_window.config(bg="gray")
    # creating a main label
    settings_label = tkinter.Label(settings_window, text="Settings", font=("Arial", 20), bg="gray")
    settings_label.pack()
    # creating a frame for the entry and label
    frame = tkinter.Frame(settings_window, bg="gray")
    frame.pack()

    # creating an entry for adding a word
    entry = tkinter.Entry(frame)
    entry.grid(row=0, column=1)
    # creating a label for ???
    label = tkinter.Label(frame, text="Adding a new word", font=("Arial", 10), bg="gray")
    label.grid(row=0, column=0)

    # creating a label for the resizability choice
    resizable_label = tkinter.Label(frame, text="Resizable", font=("Arial", 10), bg="gray")
    resizable_label.grid(row=1, column=0)
    # creating a checkbutton for resizability
    resizable = tkinter.IntVar()
    resizable.set(1)
    resizable_checkbutton = tkinter.Checkbutton(frame, variable=resizable, bg="gray")
    resizable_checkbutton.grid(row=1, column=1)

    # creating a label for the difficulty choice
    difficulty_label = tkinter.Label(frame, text="Difficulty", font=("Arial", 10), bg="gray")
    difficulty_label.grid(row=2, column=0)
    # creating a multiple choice for the difficulty (easy, medium, hard)
    difficulty = tkinter.StringVar()
    difficulty.set("easy")
    difficulty_menu = tkinter.OptionMenu(frame, difficulty, "easy", "medium", "hard")
    difficulty_menu.grid(row=2, column=1)
    
    # creating a submit button
    submit_button = tkinter.Button(settings_window, text="Submit", font=("Arial", 10), command=lambda: apply_settings())
    submit_button.pack(side="bottom")

    settings_window.mainloop()

# function to submit a guessed letter
def submit_guess(letter):
    # clearing the entry
    entry.delete(0, "end")
    # checking if only one letter was entered
    if len(letter) != 1:
        print("Please enter only one letter!")
        return
    # checking if the letter is in the word
    if letter in word:
        print("Correct!")
        # finding the index of the letter in the word
        index = word.index(letter)
        print(index)
        # replacing the _ with the letter in the word_label
        word_label.config(text=word_label.cget("text")[:index * 2] + letter + word_label.cget("text")[index * 2 + 1:])
        # checking if there is a letter left to guess, if no the player won
        if "_" not in word_label.cget("text"):
            print("You won!")
        window.update()
    else:
        print("Incorrect!")

# Main window settings
window = tkinter.Tk()
window.title("Hangman")
window.geometry("700x500")
window.resizable(False, False)
window.iconbitmap("hangman.ico")
window.config(bg="gray")

# creating a list of words from the words.txt file
words = []
with open("words.txt", "r") as file:
    line = file.readline()
    while line:
        words.append(line.strip())
        line = file.readline()
print(words)

# picking a random word from the list
word = random.choice(words)
print(word)
# getting the length of the word
length = len(word)

# creating a main frame
main_frame = tkinter.Frame(window, bg="gray", width=700, height=500)
main_frame.pack()

# creating a canvas
canvas = tkinter.Canvas(main_frame, width=400, height=500, bg="white")
canvas.grid(row=0, column=0)

# creating a sub frame for the buttons entry and label
sub_frame = tkinter.Frame(main_frame, bg="gray", width=300, height=500)
sub_frame.grid(row=0, column=1)

# creating a label
label = tkinter.Label(sub_frame, text="Welcome to Hangman", font=("Arial", 20), bg="gray")
label.pack()

# creating a label for the word, this label displays the number of letters in the word with _ for each letter, if a letter is guessed correctly it will be displayed instead of the _
word_label = tkinter.Label(sub_frame, text="_ " * length, font=("Arial", 15), bg="gray")
word_label.pack()

# creating a frame for the entry and submit button
entry_frame = tkinter.Frame(sub_frame, bg="gray")
entry_frame.pack()

# creating an entry
entry = tkinter.Entry(entry_frame, font=("Arial", 10))
entry.grid(row=0, column=0)

# creating a submit button
submit_button = tkinter.Button(entry_frame, text="Submit", font=("Arial", 7), width=10, command=lambda: submit_guess(entry.get()))
submit_button.grid(row=0, column=1)

# creating a frame for the reset and settings button
button_frame = tkinter.Frame(sub_frame, bg="gray")
button_frame.pack()

# creating a reset button
reset_button = tkinter.Button(button_frame, text="Reset", font=("Arial", 10), command=lambda: reset())
reset_button.grid(row=0, column=0)

# creating a settings button
settings_button = tkinter.Button(button_frame, text="Settings", font=("Arial", 10), command=lambda: settings())
settings_button.grid(row=0, column=1)

window.mainloop()
