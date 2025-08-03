# Python program to generate random
# password using Tkinter module
import random
import pyperclip
from tkinter import *
from tkinter.ttk import *
import string
import secrets
from tkinter import messagebox
import hashlib
from datetime import datetime
from tkinter import Button, Tk, mainloop, Radiobutton

# Function for calculation of password


def low():
    entry.delete(0, END)

    # Get the length of password
    length = var1.get()
    
    lower = string.ascii_lowercase
    upper = string.ascii_letters
    digits = string.ascii_letters + string.digits + string.punctuation
    password = ""
    

    # if strength selected is low
    if var.get() == 1:
        for i in range(0, length):
            password = password + random.choice(lower)
        return password

    # if strength selected is medium
    if var.get() == 0:
        for i in range(0, length):
            password = password + random.choice(upper)
        return password

    # if strength selected is strong
    if var.get() == 3:
        for i in range(0, length):
            password = password + random.choice(digits)
        return password
    
    else:
        messagebox.showinfo("Error", "Please choose an option")

    # Example of hashing the password using hashlib
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    print("Hashed Password:", hashed_password)

    # Example of using secrets to generate a random token
    random_token = secrets.token_hex(16)
    print("Random Token:", random_token)
    
    return password

# Function for generation of password
def generate():
    password1 = low()
    entry.insert(10, password1)

# Function for copying password to clipboard
def copy1():
    random_password = entry.get()
    pyperclip.copy(random_password)
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# Function for saving password and timestamp to a file
def save_to_file():
    random_password = entry.get()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} - {random_password}\n"
    with open("password_log.txt", "a") as log_file:
        log_file.write(log_entry)
    messagebox.showinfo("Saved", "Password and timestamp saved to file!")


# Main Function

# Create GUI Window
root = Tk()
var = IntVar()
var1 = IntVar()


# Title,size and colour of your GUI window
root.configure(bg='black')
root.title("Random Password Generator")
root.geometry('520x200')


# create label and entry to show
# password generated
Random_password = Label(root, text="Password", background='black', foreground='white').place(x=40,y=70)
#Random_password.grid(row=30)
entry = Entry(root)
entry.place(x=100,y=70)

# Create welcome label
x_label= Label(root, text="Password Generator", background='black', foreground='cyan', font=("Helvetica", 12, "bold")).place(x=190,y=30)

# create label for length of password
c_label = Label(root, text="Length", background='black', foreground='white').place(x=40,y=110)

# create Buttons Copy which will copy password to clipboard
# and Generate which will generate the password
# and Save which will save the date, time and password in a file
copy_button = Button(root, text="Copy", command=copy1, fg="white", bg="pink", font=("Helvetica", 8, "bold")).place(x=240,y=70)

generate_button = Button(root, text="Generate", command=generate, fg="white", bg="light blue", font=("Helvetica", 8, "bold")).place(x=300,y=70)

save_button = Button(root, text="Save in a File", command=save_to_file, fg="white", bg="light green", font=("Helvetica", 8, "bold")).place(x=380,y=70)

# Radio Buttons for deciding the strength of password
# Default strength is Medium
radio_low = Radiobutton(root, text="Low", variable=var, value=1, bg="black", fg="white").place(x=240,y=110)

radio_middle = Radiobutton(root, text="Medium", variable=var, value=0, bg="black", fg="white").place(x=300,y=110)

radio_strong = Radiobutton(root, text="Strong", variable=var, value=3, bg="black", fg="white").place(x=380,y=110)


# Combo Box for length of your password
combo = Combobox(root, textvariable=var1)
combo['values'] = (8, 9, 10, 11, 12, 13, 14, 15, 16,
                17, 18, 19, 20, 21, 22, 23, 24, 25,
                26, 27, 28, 29, 30, 31, 32, "Length")
combo.current(0)
combo.bind('<<ComboboxSelected>>')
combo.place(x=85,y=110)

# start the GUI
root.mainloop()



