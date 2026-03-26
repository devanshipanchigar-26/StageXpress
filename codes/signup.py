import os
from tkinter import *
import pymysql
from tkinter import messagebox
from PIL import Image, ImageTk

#functions

def login_page():
    signup_window.destroy()
    os.system(r'python "codes\login_page.py"')

def clear():
    email_entry.delete(0, END)
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    confirm_password_entry.delete(0, END)
    check.set(0)

def connect_database():
    if email_entry.get() == '' or username_entry.get() == '' or password_entry.get() == '' or confirm_password_entry.get() == '':
        messagebox.showerror("Error", "All fields are required")
    elif password_entry.get() != confirm_password_entry.get():
        messagebox.showerror("Error", "Password and Confirm Password should be same")
    elif check.get() == 0:
        messagebox.showerror("Error", "Please agree to the Terms and Conditions")
    else:
        try:
            con=pymysql.connect(host="localhost", user="root", password="")
            mycursor=con.cursor()
        except:
            messagebox.showerror("Error", "Database connectivity issue, please try again")
            return
        
        try:
            query = "create database userdata"
            mycursor.execute(query)
            query = "use userdata"
            mycursor.execute(query)
            query = "create table login(id int auto_increment primary key not null, email varchar(50), username varchar(100), password varchar(20))"
            mycursor.execute(query)
        except:
            mycursor.execute("use userdata")

        query = "select * from login where username=%s"
        mycursor.execute(query, (username_entry.get(),))
        result = mycursor.fetchone()

        if result:
            messagebox.showerror("Error", "Username already exists")
            return
        else:
            query = "insert into login(email, username, password) values(%s, %s, %s)"
            mycursor.execute(query, (email_entry.get(), username_entry.get(), password_entry.get()))
            con.commit()
            con.close()
            messagebox.showinfo("Success", "Registration is successful")
            clear()
            login_page()



# GUI

signup_window = Tk()
signup_window.resizable(False, False)
signup_window.title("Signup Page")
signup_window.geometry("1200x800")

# Background Image
bgImage = ImageTk.PhotoImage(file=r"images/Backgorund.png")

bgLabel = Label(signup_window, image=bgImage)
bgLabel.place(x=0, y=0, relwidth=1, relheight=1)



# Signup Label
signup_label = Label(signup_window, text="Create An Account", font=("Arial", 26, "bold"), fg="#222564", bg="#ffffff")
signup_label.place(x=725, y=150)

# Email
email_label = Label(signup_window, text="Email :", font=("Arial", 14, "bold"), fg="#222564", bg="#ffffff")
email_label.place(x=725, y=225)

email_entry = Entry(signup_window, width=35, font=("Arial", 12),bd=0 , fg="#ffffff" , bg="#222564")
email_entry.place(x=735, y=255)

# Username
username_label = Label(signup_window, text="Username :", font=("Arial", 14, "bold"), fg="#222564", bg="#ffffff")
username_label.place(x=725, y=290)

username_entry = Entry(signup_window, width=35, font=("Arial", 12),bd=0 , fg="#ffffff" , bg="#222564")
username_entry.place(x=735, y=320)

# Password
password_label = Label(signup_window, text="Password :", font=("Arial", 14, "bold"), fg="#222564", bg="#ffffff")
password_label.place(x=725, y=355)

password_entry = Entry(signup_window, width=35, font=("Arial", 12),bd=0 , fg="#ffffff" , bg="#222564")
password_entry.place(x=735, y=385)


# Confirm Password
confirm_password_label = Label(signup_window, text="Confirm Password :", font=("Arial", 14, "bold"), fg="#222564", bg="#ffffff")
confirm_password_label.place(x=725, y=420)

confirm_password_entry = Entry(signup_window, width=35, font=("Arial", 12),bd=0 , fg="#ffffff" , bg="#222564")
confirm_password_entry.place(x=735, y=450)

#terms and conditions
check=IntVar()
terms = Checkbutton(signup_window, text="I agree to the Terms and Conditions", font=("Arial", 12), fg="#222564", bg="#ffffff" , activebackground="#ffffff", activeforeground="#222564", variable=check)
terms.place(x=725, y=480)

#signup button
signupButton = Button(signup_window, text="Signup", font=("Arial", 26, "bold"), bd=0, bg="#222564" , fg="#ffffff", activebackground="#222564", cursor="hand2",command=connect_database)
signupButton.place(x=725, y=550, width=350)

#slogin label and button
signup_label = Label(signup_window, text="already have an account?", font=("Arial", 12, "bold"), fg="#B61515", bg="#ffffff")
signup_label.place(x=750, y=625)
signupButton = Button(signup_window, text="Login", font=("Arial", 12, "bold"), bd=0, bg="#ffffff" , fg="#222564", activebackground="#ffffff", cursor="hand2", command=login_page)
signupButton.place(x=980, y=625)


signup_window.mainloop()