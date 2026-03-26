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

def login_user():
    if username_entry.get() == '' or password_entry.get() == '' or username_entry.get() == "Username" or password_entry.get() == "Password":
        messagebox.showerror("Error", "All fields are required")

    else:
        try:
            con = pymysql.connect(host="localhost", user="root", password="")
            mycursor = con.cursor()
            query = "use userdata"
            mycursor.execute(query)
        except pymysql.err.OperationalError as e:
            if e.args[0] == 1049:
                messagebox.showerror("Error", "Database does not exist. Please sign up first.")
            else:
                messagebox.showerror("Error", f"Database connectivity issue: {e}")
            return
        except Exception as e:
            messagebox.showerror("Error", "Database connectivity issue, please try again")
            return

        query = "select * from login where username=%s and password=%s"
        mycursor.execute(query, (username_entry.get(), password_entry.get()))
        result = mycursor.fetchone()
        if result:
            messagebox.showinfo("Success", "Login is successful")
            clear()
        else:
            messagebox.showerror("Error", "Invalid username or password")

# GUI
login_window = Tk()
login_window.resizable(0, 0)
login_window.title("Login Page")
login_window.geometry("1200x800")

# Background Image
bgImage = ImageTk.PhotoImage(file=r"images/Backgorund.png")

bgLabel = Label(login_window, image=bgImage)
bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

# Login Label
login_label = Label(login_window, text="Login User", font=("Arial", 30, "bold"), fg="#222564", bg="#ffffff")
login_label.place(x=800, y=175)

# Username Entry
username_entry = Entry(login_window, width=25, font=("Arial", 18, "bold"),bd=0 , fg="#222564")
username_entry.place(x=725, y=315)
username_entry.insert(0, "Username")

username_entry.bind("<FocusIn>", on_enter_username)
username_entry.bind("<FocusOut>", on_leave_username)

Frame(login_window, width=325, height=2, bg="#222564").place(x=725, y=345)

# Password Entry and Eye Button
password_entry = Entry(login_window, width=25, font=("Arial", 18, "bold"),bd=0 , fg="#222564")
password_entry.place(x=725, y=395)
password_entry.insert(0, "Password")

password_entry.bind("<FocusIn>", on_enter_password)
password_entry.bind("<FocusOut>", on_leave_password)

Frame(login_window, width=325, height=2, bg="#222564").place(x=725, y=428)


close = Image.open(r"images/close_eye.png")
close = close.resize((35, 25), Image.LANCZOS)
close_eye = ImageTk.PhotoImage(close)

open_img = Image.open(r"images/open_eye.png")
open_img = open_img.resize((35, 30), Image.LANCZOS)
open_eye = ImageTk.PhotoImage(open_img)

eyeButton = Button(login_window, image=open_eye, bd=0, bg="#ffffff", activebackground="#ffffff", cursor="hand2", command=hide)
eyeButton.place(x=1015, y=390)

eyeButton.image = open_eye

#frget password button
forgteButton = Button(login_window, text="Forgot Password?",font=("Arial", 11, "bold") , bd=0, bg="#ffffff" , fg="#B61515", activebackground="#ffffff", cursor="hand2")
forgteButton.place(x=900, y=440)

#login button
loginButton = Button(login_window, text="Login", font=("Arial", 26, "bold"), bd=0, bg="#222564" , fg="#ffffff", activebackground="#222564", cursor="hand2", command=login_user)
loginButton.place(x=725, y=525, width=345)

#signup label and button
signup_label = Label(login_window, text="Don't have an account?", font=("Arial", 11, "bold"), fg="#B61515", bg="#ffffff")
signup_label.place(x=750, y=600)
signupButton = Button(login_window, text="Create new ", font=("Arial", 11, "bold"), bd=0, bg="#ffffff" , fg="#222564", activebackground="#ffffff", cursor="hand2", command=signup_page)
signupButton.place(x=950, y=600)



login_window.mainloop()