import tkinter as tk
import customtkinter as ctk
import tkinter.messagebox as tkmb
import pymysql

def check_credentials():
    mydb = pymysql.connect(host="127.0.0.1", user="root", password="", database="members_db ", port=3368)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM users WHERE name = %s AND password = %s", (username_entry.get(), password_entry.get()))
    result = mycursor.fetchone()
    if result:
        # Replace 'new_file' with the name of your new file
        # new_file.start_app()
        tkmb.showinfo(title="Login Successful", message="Welcome!")
        root.hide()
    else:
        tkmb.showerror(title="Login Failed", message="Invalid username or password")

# Set appearance mode and color theme
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Login Page")
root.geometry("400x300")

frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=40, fill='both', expand=True)

username_label = ctk.CTkLabel(master=frame, text="Username:")
username_label.pack(pady=12, padx=10)
username_entry = ctk.CTkEntry(master=frame, placeholder_text="Username")
username_entry.pack(pady=12, padx=10)

password_label = ctk.CTkLabel(master=frame, text="Password:")
password_label.pack(pady=12, padx=10)
password_entry = ctk.CTkEntry(master=frame, placeholder_text="Password", show="*")
password_entry.pack(pady=12, padx=10)

login_button = ctk.CTkButton(master=frame, text="Login", command=check_credentials)
login_button.pack(pady=12, padx=10)

root.mainloop()
