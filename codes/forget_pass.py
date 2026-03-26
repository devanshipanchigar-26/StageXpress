import os
import pymysql
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

# Functions

def on_enter_username(event):
    if username_entry.get() == "Username":
        username_entry.delete(0, END)

def on_enter_password(event):
    if password_entry.get() == "Password":
        password_entry.delete(0, END)

def on_leave_username(event):
    if username_entry.get() == "":
        username_entry.insert(0, "Username")

def on_leave_password(event):
    if password_entry.get() == "":
        password_entry.insert(0, "Password")

def hide():
    eyeButton.config(image=close_eye)
    password_entry.config(show="*")
    eyeButton.config(command=show)

def show():
    eyeButton.config(image=open_eye)
    password_entry.config(show="")
    eyeButton.config(command=hide)

def signup_page():
    login_window.destroy()
    os.system(r'python "codes\signup.py"')

def clear():
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    username_entry.insert(0, "Username")
    password_entry.insert(0, "Password")


# GUI
reset_window = Tk()
reset_window.resizable(0, 0)
reset_window.title("Reset Password")
reset_window.geometry("1200x800")

# Background Image
bgImage = ImageTk.PhotoImage(file=r"images/forget_pass_bg.png")

bgLabel = Label(reset_window, image=bgImage)
bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

# Login Label
login_label = Label(reset_window, text="Reset Password", font=("Arial", 30, "bold"), fg="#eb4d40", bg="#ffffff")
login_label.place(x=730, y=175)

# Username Entry
username_entry = Entry(reset_window, width=25, font=("Arial", 18, "bold"),bd=0 , fg="#f0925a")
username_entry.place(x=725, y=300)
username_entry.insert(0, "Username")

username_entry.bind("<FocusIn>", on_enter_username)
username_entry.bind("<FocusOut>", on_leave_username)

Frame(reset_window, width=325, height=2, bg="#eb4d40").place(x=725, y=330)

# Password Entry 
password_entry = Entry(reset_window, width=25, font=("Arial", 18, "bold"),bd=0 , fg="#f0925a")
password_entry.place(x=725, y=380)
password_entry.insert(0, "Password")

password_entry.bind("<FocusIn>", on_enter_password)
password_entry.bind("<FocusOut>", on_leave_password)

Frame(reset_window, width=325, height=2, bg="#eb4d40").place(x=725, y=410)

# Confirm Password Entry 
confirm_password_entry = Entry(reset_window, width=25, font=("Arial", 18, "bold"),bd=0 , fg="#f0925a")
confirm_password_entry.place(x=725, y=460)
confirm_password_entry.insert(0, "Confirm Password")

confirm_password_entry.bind("<FocusIn>", on_enter_password)
confirm_password_entry.bind("<FocusOut>", on_leave_password)

Frame(reset_window, width=325, height=2, bg="#eb4d40").place(x=725, y=490)


#login button
loginButton = Button(reset_window, text="Submit", font=("Arial", 26, "bold"), bd=0, bg="#eb4d40" , fg="#ffffff", activebackground="#eb4d40", cursor="hand2")
loginButton.place(x=725, y=550, width=345)


reset_window.mainloop()