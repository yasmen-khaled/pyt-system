import tkinter as tk
import customtkinter as ctk
import tkinter.messagebox as tkmb
import pymysql
import subprocess

# Define your button commands here
def button1_command():
     root.withdraw()
     subprocess.run(["python3", "Employee.py"], check=True)

def button2_command():
    root.withdraw()
    subprocess.run(["python3", "master.py"], check=True)

def button3_command():
    root.withdraw()
    subprocess.run(["python3", "Bc.py"], check=True)

def button4_command():
    root.withdraw()
    subprocess.run(["python3", "ph.py"], check=True)


def button5_command():
    root.withdraw()
    subprocess.run(["python3", "Contract.py"], check=True)

# Set appearance mode and color theme
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


root = ctk.CTk()
root.title("Button Page")
root.geometry("600x600")  # Increase window size

frame = ctk.CTkFrame(master=root)
frame.pack(pady=20, padx=40, fill='both', expand=True)

# Add four buttons to the frame with increased size
button1 = ctk.CTkButton(master=frame, text="Employees", command=button1_command, height=90, width=300)
button1.pack(pady=12, padx=10)

button2 = ctk.CTkButton(master=frame, text="Master", command=button2_command, height=90, width=300)
button2.pack(pady=12, padx=10)

button3 = ctk.CTkButton(master=frame, text="Bachelor's", command=button3_command, height=90, width=300)
button3.pack(pady=12, padx=10)

button4 = ctk.CTkButton(master=frame, text="Ph.D", command=button4_command, height=90, width=300)
button4.pack(pady=12, padx=10)

button5 = ctk.CTkButton(master=frame, text="Contract", command=button5_command, height=90, width=300)
button5.pack(pady=12, padx=10)



#button = tk.Button(root, text='Open Interface', command=button1_command)

root.mainloop()
