import csv
import smtplib
import random
import tkinter as tk
from tkinter import ttk
from datetime import datetime
from email.mime.text import MIMEText
from config import EMAIL, PASSWORD

FILE_PATH = "/Users/ronakchavhan/Python/Bday_Wish/contacts.csv"

def load_contacts():
    contacts = []
    try:
        with open(FILE_PATH, "r", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                clean_row = {key.strip(): value.strip() for key, value in row.items()}
                contacts.append(clean_row)
        return contacts
    except FileNotFoundError:
        print("Error: contacts.csv file not found!")
        return []

def save_contact(name, email, birthday):
    with open(FILE_PATH, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([name, email, birthday])

def email_send(to_email, subject, message):
    try:
        print(f"Attempting to log in as: {EMAIL}")  
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = EMAIL
        msg['To'] = to_email

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL, PASSWORD) 
            print("Logged in successfully!")  
            server.sendmail(EMAIL, to_email, msg.as_string())
            print(f"Email sent to {to_email} successfully!") 

    except Exception as e:
        print("Error:", e)  

wishes = [
    "Happy Birthday! 🎉 Have a fantastic day!",
    "Wishing you happiness and success. Enjoy your day! 🎂",
    "Another year, another adventure! Have a great birthday!"
]

def random_wish():
    return random.choice(wishes)

def show_main_menu():
    root = tk.Tk()
    root.title("Birthday Wishes 🎉")
    root.geometry("400x300")
    root.configure(bg="#121212")  # Dark background

    label = tk.Label(root, text="WELCOME", font=("Montserrat", 20, "bold"), fg="gold", bg="#121212")
    label.pack(pady=20)

    style = ttk.Style()
    style.configure("TButton", font=("Arial", 14), padding=5, background="gold", foreground="black")

    btn_display = ttk.Button(root, text="1️⃣ Display Data", command=lambda: [root.destroy(), display_data()])
    btn_display.pack(pady=10)

    btn_add = ttk.Button(root, text="2️⃣ Add Data", command=lambda: [root.destroy(), add_contact()])
    btn_add.pack(pady=10)

    root.mainloop()

def display_data():
    root = tk.Tk()
    root.title("Upcoming Birthdays 🎉")
    root.configure(bg="#121212")

    label = tk.Label(root, text="Upcoming Birthdays", font=("Montserrat", 16, "bold"), fg="gold", bg="#121212")
    label.pack()

    tree = ttk.Treeview(root, columns=("Name", "Birthday"), show="headings")
    tree.heading("Name", text="Name")
    tree.heading("Birthday", text="Birthday")
    tree.pack()

    contacts = load_contacts()
    for contact in contacts:
        if "Name" in contact and "Birthday" in contact:
            tree.insert("", "end", values=(contact["Name"], contact["Birthday"]))

    root.mainloop()

def add_contact():
    add_win = tk.Tk()
    add_win.title("Add New Contact")
    add_win.geometry("400x300")
    add_win.configure(bg="#121212")

    tk.Label(add_win, text="Enter Name:", fg="gold", bg="#121212").pack()
    entry_name = tk.Entry(add_win)
    entry_name.pack()

    tk.Label(add_win, text="Enter Email:", fg="gold", bg="#121212").pack()
    entry_email = tk.Entry(add_win)
    entry_email.pack()

    tk.Label(add_win, text="Enter Birthday (YYYY-MM-DD):", fg="gold", bg="#121212").pack()
    entry_birthday = tk.Entry(add_win)
    entry_birthday.pack()

    def save():
        name = entry_name.get()
        email = entry_email.get()
        birthday = entry_birthday.get()
        if name and email and birthday:
            save_contact(name, email, birthday)
            add_win.destroy()
            show_main_menu()

    ttk.Button(add_win, text="Save Contact", command=save).pack(pady=10)
    add_win.mainloop()

show_main_menu()

email_send("ronakchavhan89@gmail.com", "Test", "This is a text mail.")
