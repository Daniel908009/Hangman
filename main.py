# necesary imports
import tkinter
import random
import os 
import sys
if hasattr(sys, '_MEIPASS'):
    base_path = sys._MEIPASS
else:
    base_path = os.path.abspath(".")

# function to reset the game
def reset():
    global word, length, buffer_size, center_size
    # clearing the entry
    entry.delete(0, "end")
    # changing the sizes of the labels
    label_size = window.winfo_width() // 32
    label.config(font=("Arial", label_size))
    info_label_size = window.winfo_width() // 64
    info_label.config(font=("Arial", info_label_size))
    word_label_size = info_label_size + 5
    word_label.config(font=("Arial", word_label_size))
    # changing the size of the entry and buttons
    entry_size = window.winfo_width() // 64
    entry.config(font=("Arial", entry_size))
    submit_button_size = window.winfo_width() // 64
    submit_button_height = window.winfo_height() // 64
    submit_button.config(width=submit_button_size, font=("Arial", submit_button_height))
    reset_button_size = window.winfo_width() // 64
    reset_button.config(font=("Arial", reset_button_size))
    settings_button_size = window.winfo_width() // 64
    settings_button.config(font=("Arial", settings_button_size))

    # clearing the info label
    info_label.config(text="Guess a letter")
    # deleting everything in the canvas
    canvas.delete("all")
    # changing the size of the canvas
    canvas_width = window.winfo_width() // 2 + 50
    canvas.config(width=canvas_width, height=window.winfo_height())
    # getting the buffer size and center size
    buffer_size = window.winfo_height() // 6
    center_size = window.winfo_width() // 6

    # drawing the hangman pole
    canvas.create_line(center_size+50, buffer_size+50, center_size+50, buffer_size+400)
    canvas.create_line(center_size+50, buffer_size+50, center_size+200, buffer_size+50)
    canvas.create_line(center_size+200, buffer_size+50, center_size+200, buffer_size+100)
    # picking a new random word
    # checking if the word is empty if yes than another word will be picked
    word = random.choice(words)
    while len(word) == 0:
        word = random.choice(words)
    # changing the word to uppercase for easier comparison and better playability of the game
    word = word.upper()
    # deleting any spaces in the word
    word = word.replace(" ", "")

    # getting the length of the word
    length = len(word)
    # creating a new word label
    word_label.config(text="_ " * length)
    # resetting the submit button
    submit_button.config(state="normal")
    # resetting the hangman parts
    global difficulty, hangman_parts
    if difficulty == "easy":
        hangman_parts = ["head", "body", "left arm", "right arm", "left leg", "right leg", "left foot", "right foot", "left hand", "right hand"]
    elif difficulty == "medium":
        hangman_parts = ["head", "body", "left arm", "right arm", "left leg", "right leg", "left foot", "right foot"]
    elif difficulty == "hard":
        hangman_parts = ["head", "body", "left arm", "right arm", "left leg", "right leg"]
    window.update()

# function to apply the settings
def apply_settings(answer_resizable, answer_difficulty):
    # checking if the user wants the window to be resizable
    if answer_resizable:
        window.resizable(True, True)
    else:
        window.resizable(False, False)
    # changing the difficulty
    global difficulty
    difficulty = answer_difficulty
    # changing the hangman parts based on the difficulty
    global hangman_parts
    hangman_parts.clear()
    if difficulty == "easy":
        hangman_parts = ["head", "body", "left arm", "right arm", "left leg", "right leg", "left foot", "right foot", "left hand", "right hand"]
    elif difficulty == "medium":
        hangman_parts = ["head", "body", "left arm", "right arm", "left leg", "right leg", "left foot", "right foot"]
    elif difficulty == "hard":
        hangman_parts = ["head", "body", "left arm", "right arm", "left leg", "right leg"]
    # resetting to apply the changes
    reset()

# function to save the words to the file
def save_words(words):
    # opening the file in write mode
    with open(os.path.join(base_path,"words.txt"), "w") as file:
        # writing the words to the file
        file.write(words)
    # changing the info label
    info_label.config(text="Words saved!")
    
# function to edit the file with the words, add or remove words
def change_words():
    # creating a new window for the text editor
    change_words_window = tkinter.Toplevel(window)
    change_words_window.title("Edit words")
    change_words_window.geometry("700x400")
    change_words_window.resizable(False, False)
    change_words_window.config(bg="gray")
    change_words_window.iconbitmap(os.path.join(base_path, "Hangman.ico"))
    # creating a frame for the text editor and submit button
    frame = tkinter.Frame(change_words_window, bg="gray")
    frame.pack()
    # creating a text editor for the file with the words
    text_editor = tkinter.Text(frame, font=("Arial", 10))
    text_editor.grid(row=0, column=0)
    # filling the text editor with the words from the file
    with open(os.path.join(base_path,"words.txt"), "r") as file:
        line = file.readline()
        while line:
            text_editor.insert("end", line)
            line = file.readline()
    # creating a submit button that will save the changes to the file
    submit_button = tkinter.Button(frame, text="Submit", font=("Arial", 10), command=lambda: save_words(text_editor.get("1.0", "end")), width=10, height=2)
    submit_button.grid(row=0, column=1)

# function for the settings window
def settings():
    # creating a new window for the settings
    global difficulty
    settings_window = tkinter.Toplevel(window)
    settings_window.title("Settings")
    settings_window.geometry("300x200")
    settings_window.resizable(False, False)
    settings_window.config(bg="gray")
    settings_window.iconbitmap(os.path.join(base_path,"Hangman.ico"))
    # creating a main label
    settings_label = tkinter.Label(settings_window, text="Settings", font=("Arial", 20), bg="gray")
    settings_label.pack()
    # creating a frame for the entry and label
    frame = tkinter.Frame(settings_window, bg="gray")
    frame.pack()

    # creating a button for changing the words
    change_words_button = tkinter.Button(frame, text="Edit file", font=("Arial", 10), command=lambda: change_words())
    change_words_button.grid(row=0, column=1)
    # creating a label for adding a word
    label = tkinter.Label(frame, text="Adding or removing a word", font=("Arial", 10), bg="gray")
    label.grid(row=0, column=0)

    # creating a label for the resizability choice
    resizable_label = tkinter.Label(frame, text="Resizable window", font=("Arial", 10), bg="gray")
    resizable_label.grid(row=1, column=0)
    # creating a checkbutton for resizability
    resizable = tkinter.IntVar()
    resizable.set(False)
    resizable_checkbutton = tkinter.Checkbutton(frame, variable=resizable, bg="gray")
    resizable_checkbutton.grid(row=1, column=1)

    # creating a label for the difficulty choice
    difficulty_label = tkinter.Label(frame, text="Difficulty", font=("Arial", 10), bg="gray")
    difficulty_label.grid(row=2, column=0)
    # creating a multiple choice for the difficulty (easy, medium, hard)
    difficultya = tkinter.StringVar()
    # setting the difficulty based on the current difficulty of the game
    if difficulty == "easy":
        difficultya.set("easy")
    elif difficulty == "medium":
        difficultya.set("medium")
    elif difficulty == "hard":
        difficultya.set("hard")
    difficulty_menu = tkinter.OptionMenu(frame, difficultya, "easy", "medium", "hard")
    difficulty_menu.grid(row=2, column=1)
    
    # creating a submit button
    submit_button = tkinter.Button(settings_window, text="Submit", font=("Arial", 10), command=lambda: apply_settings(resizable.get(), difficultya.get()))
    submit_button.pack(side="bottom")

    settings_window.mainloop()

# function to submit a guessed letter
def submit_guess(letter):
    global buffer_size
    # making the guessed letter all uppercase
    letter = letter.upper()
    # clearing the entry
    entry.delete(0, "end")
    # checking if only one letter was entered
    if len(letter) != 1:
        info_label.config(text="Please enter only one letter!")
        return
    # checking if the letter is in the word
    if letter in word:
        info_label.config(text="Correct!")
        # finding all the indexes of the letter in the word
        indexes = [i for i in range(length) if word[i] == letter]
        # replacing the _ with the letter in the word_label
        for index in indexes:
            word_label.config(text=word_label.cget("text")[:index * 2] + letter + word_label.cget("text")[index * 2 + 1:])
        # checking if there is a letter left to guess, if no the player won
        if "_" not in word_label.cget("text"):
            info_label.config(text="You won! The word was: "+word)
            submit_button.config(state="disabled")
        window.update()
    else:
        global number_of_wrong_guesses, difficulty, hangman_parts
        info_label.config(text="Incorrect!")
        if difficulty == "easy":
            # creating the hangman parts
            if hangman_parts[0] == "head":
                canvas.create_oval(center_size+150, buffer_size+100, center_size+250, buffer_size+200)
                hangman_parts.pop(0)
            elif hangman_parts[0] == "body":
                canvas.create_line(center_size+200, buffer_size+200, center_size+200, buffer_size+300)
                hangman_parts.pop(0)
            elif hangman_parts[0] == "left arm":
                canvas.create_line(center_size+200, buffer_size+200, center_size+150, buffer_size+250)
                hangman_parts.pop(0)
            elif hangman_parts[0] == "right arm":
                canvas.create_line(center_size+200, buffer_size+200, center_size+250, buffer_size+250)
                hangman_parts.pop(0)
            elif hangman_parts[0] == "left leg":
                canvas.create_line(center_size+200, buffer_size+300, center_size+150, buffer_size+350)
                hangman_parts.pop(0)
            elif hangman_parts[0] == "right leg":
                canvas.create_line(center_size+200, buffer_size+300, center_size+250, buffer_size+350)
                hangman_parts.pop(0)
            elif hangman_parts[0] == "left foot":
                canvas.create_line(center_size+150, buffer_size+350, center_size+100, buffer_size+350)
                hangman_parts.pop(0)
            elif hangman_parts[0] == "right foot":
                canvas.create_line(center_size+250, buffer_size+350, center_size+300, buffer_size+350)
                hangman_parts.pop(0)
            elif hangman_parts[0] == "left hand":
                canvas.create_line(center_size+150, buffer_size+250, center_size+100, buffer_size+250)
                hangman_parts.pop(0)
            elif hangman_parts[0] == "right hand":
                canvas.create_line(center_size+250, buffer_size+250, center_size+300, buffer_size+250)
                hangman_parts.pop(0)
            # checking if the player lost
            if len(hangman_parts) == 0:
                info_label.config(text="You lost! The word was: "+word)
                submit_button.config(state="disabled")
                return

        elif difficulty == "medium":
            #creating the hangman parts
            if hangman_parts[0] == "head":
                canvas.create_oval(center_size+150, buffer_size+100, center_size+250, buffer_size+200)
                hangman_parts.pop(0)
            elif hangman_parts[0] == "body":
                canvas.create_line(center_size+200, buffer_size+200, center_size+200, buffer_size+300)
                hangman_parts.pop(0)
            elif hangman_parts[0] == "left arm":
                canvas.create_line(center_size+200, buffer_size+200, center_size+150, buffer_size+250)
                hangman_parts.pop(0)
            elif hangman_parts[0] == "right arm":
                canvas.create_line(center_size+200, buffer_size+200, center_size+250, buffer_size+250)
                hangman_parts.pop(0)
            elif hangman_parts[0] == "left leg":
                canvas.create_line(center_size+200, buffer_size+300, center_size+150, buffer_size+350)
                hangman_parts.pop(0)
            elif hangman_parts[0] == "right leg":
                canvas.create_line(center_size+200, buffer_size+300, center_size+250, buffer_size+350)
                hangman_parts.pop(0)
            elif hangman_parts[0] == "left foot":
                canvas.create_line(center_size+150, buffer_size+350, center_size+100, buffer_size+350)
                hangman_parts.pop(0)
            elif hangman_parts[0] == "right foot":
                canvas.create_line(center_size+250, buffer_size+350, center_size+300, buffer_size+350)
                hangman_parts.pop(0)
            # checking if the player lost
            if len(hangman_parts) == 0:
                info_label.config(text="You lost! The word was: "+word)
                submit_button.config(state="disabled")
                return

        elif difficulty == "hard":
            #creating the hangman parts
            if hangman_parts[0] == "head":
                canvas.create_oval(center_size+150, buffer_size+100, center_size+250, buffer_size+200)
                hangman_parts.pop(0)
            elif hangman_parts[0] == "body":
                canvas.create_line(center_size+200, buffer_size+200, center_size+200, buffer_size+300)
                hangman_parts.pop(0)
            elif hangman_parts[0] == "left arm":
                canvas.create_line(center_size+200, buffer_size+200, center_size+150, buffer_size+250)
                hangman_parts.pop(0)
            elif hangman_parts[0] == "right arm":
                canvas.create_line(center_size+200, buffer_size+200, center_size+250, buffer_size+250)
                hangman_parts.pop(0)
            elif hangman_parts[0] == "left leg":
                canvas.create_line(center_size+200, buffer_size+300, center_size+150, buffer_size+350)
                hangman_parts.pop(0)
            elif hangman_parts[0] == "right leg":
                canvas.create_line(center_size+200, buffer_size+300, center_size+250, buffer_size+350)
                hangman_parts.pop(0)
            # checking if the player lost
            if len(hangman_parts) == 0:
                info_label.config(text="You lost! The word was: "+word)
                submit_button.config(state="disabled")
                return     

# Main window settings
window = tkinter.Tk()
window.title(os.path.join(base_path,"Hangman") )
window.geometry("700x500")
window.resizable(False, False)
window.iconbitmap(os.path.join(base_path,"hangman.ico") )
window.config(bg="gray")

# variable for difficulty
# based on the difficulty the number of parts of the hangman will be determined
difficulty = "medium"
hangman_parts = []
if difficulty == "easy":
    hangman_parts = ["head", "body", "left arm", "right arm", "left leg", "right leg", "left foot", "right foot", "left hand", "right hand"]
elif difficulty == "medium":
    hangman_parts = ["head", "body", "left arm", "right arm", "left leg", "right leg", "left foot", "right foot"]
elif difficulty == "hard":
    hangman_parts = ["head", "body", "left arm", "right arm", "left leg", "right leg"]


# creating a list of words from the words.txt file
words = []
with open(os.path.join(base_path,"words.txt") , "r") as file:
    line = file.readline()
    while line:
        words.append(line.strip())
        line = file.readline()

# picking a random word from the list
word = ""
# checking if the word is empty if yes than another word will be picked
while len(word) == 0:
    word = random.choice(words)
# changing the word to uppercase for easier comparison and better playability of the game
word = word.upper()
# deleting any spaces in the word
word = word.replace(" ", "")

# getting the length of the word
length = len(word)

# creating a main frame
main_frame = tkinter.Frame(window, bg="gray", width=700, height=500)
main_frame.pack()

# creating a variable for the canvas width
canvas_width = window.winfo_width() // 2 + 50

# creating a canvas
canvas = tkinter.Canvas(main_frame, width=canvas_width, height=window.winfo_height(), bg="white")
canvas.grid(row=0, column=0)

# creating a buffer size variable, that will be used to determine the height of the hangman parts, the bigger the window the bigger the buffer size
buffer_size = window.winfo_height() // 6
center_size = window.winfo_width() // 8
# drawing the hangman pole
canvas.create_line(center_size+50, buffer_size+50, center_size+50, buffer_size+400)
canvas.create_line(center_size+50, buffer_size+50, center_size+200, buffer_size+50)
canvas.create_line(center_size+200, buffer_size+50, center_size+200, buffer_size+100)

# creating a sub frame for the buttons entry and label
sub_frame = tkinter.Frame(main_frame, bg="gray", width=300, height=500)
sub_frame.grid(row=0, column=1)

# creating a variable for the main label size
label_size = window.winfo_width() // 32

# creating a label
label = tkinter.Label(sub_frame, text="Welcome to Hangman", font=("Arial", label_size), bg="gray")
label.pack()

# creating a variable for the info label size
info_label_size = window.winfo_width() // 64

# creating an info label
info_label = tkinter.Label(sub_frame, text="Guess a letter", font=("Arial", info_label_size), bg="gray")
info_label.pack()

# creating a variable for the word label size
word_label_size = info_label_size + 5

# creating a label for the word, this label displays the number of letters in the word with _ for each letter, if a letter is guessed correctly it will be displayed instead of the _
word_label = tkinter.Label(sub_frame, text="_ " * length, font=("Arial", word_label_size), bg="gray")
word_label.pack()

# creating a frame for the entry and submit button
entry_frame = tkinter.Frame(sub_frame, bg="gray")
entry_frame.pack()

# creating a variable for the entry size
entry_size = window.winfo_width() // 64

# creating an entry
entry = tkinter.Entry(entry_frame, font=("Arial", entry_size))
entry.grid(row=0, column=0)

# creating a variable for the submit button size
submit_button_size = window.winfo_width() // 64
submit_button_height = window.winfo_height() // 64

# creating a submit button
submit_button = tkinter.Button(entry_frame, text="Submit", font=("Arial", submit_button_height), width=submit_button_size, command=lambda: submit_guess(entry.get()))
submit_button.grid(row=0, column=1)

# creating a frame for the reset and settings button
button_frame = tkinter.Frame(sub_frame, bg="gray")
button_frame.pack()

# creating a variable for the reset button size
reset_button_size = window.winfo_width() // 64

# creating a reset button
reset_button = tkinter.Button(button_frame, text="Reset", font=("Arial", reset_button_size), command=lambda: reset())
reset_button.grid(row=0, column=0)

# creating a variable for the settings button size
settings_button_size = window.winfo_width() // 64

# creating a settings button
settings_button = tkinter.Button(button_frame, text="Settings", font=("Arial", settings_button_size), command=lambda: settings())
settings_button.grid(row=0, column=1)

window.mainloop()