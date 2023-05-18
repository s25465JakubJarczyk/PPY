import tkinter as tk
import sqlite3
from tkinter import messagebox

# Funkcja do utworzenia tabeli w bazie danych
def create_table():
    try:
        connection = sqlite3.connect("students.db")
        cursor = connection.cursor()
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS students (
                email TEXT PRIMARY KEY,
                first_name TEXT,
                last_name TEXT,
                grade1 INTEGER,
                grade2 INTEGER,
                grade3 INTEGER,
                grade4 INTEGER,
                grade5 INTEGER,
                grade6 INTEGER,
                grade7 INTEGER,
                grade8 INTEGER,
                grade9 INTEGER,
                grade10 INTEGER,
                grade11 INTEGER,
                grade12 INTEGER,
                grade13 INTEGER,
                grade14 INTEGER,
                grade15 INTEGER,
                status TEXT
            )"""
        )
        connection.commit()
        connection.close()
    except sqlite3.Error as error:
        messagebox.showerror("Error", str(error))


# Funkcja do wyświetlania danych
def display_data():
    try:
        connection = sqlite3.connect("students.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM students")
        data = cursor.fetchall()
        connection.close()
        if data:
            for row in data:
                print(row)
        else:
            print("No data found.")
    except sqlite3.Error as error:
        messagebox.showerror("Error", str(error))


# Funkcja do dodawania danych
def add_data(email, first_name, last_name, grades, status):
    try:
        connection = sqlite3.connect("students.db")
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO students VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (email, first_name, last_name) + tuple(grades) + (status,),
        )
        connection.commit()
        connection.close()
        messagebox.showinfo("Success", "Data added successfully.")
    except sqlite3.Error as error:
        messagebox.showerror("Error", str(error))


# Funkcja do usuwania danych
def delete_data(email):
    try:
        connection = sqlite3.connect("students.db")
        cursor = connection.cursor()
        cursor.execute("DELETE FROM students WHERE email=?", (email,))
        connection.commit()
        connection.close()
        messagebox.showinfo("Success", "Data deleted successfully.")
    except sqlite3.Error as error:
        messagebox.showerror("Error", str(error))


# Funkcja do edytowania danych
def edit_data(email, new_email, first_name, last_name, grades, status):
    try:
        connection = sqlite3.connect("students.db")
        cursor = connection.cursor()
        cursor.execute(
            "UPDATE students SET email=?, first_name=?, last_name=?, grade1=?, grade2=?, grade3=?, grade4=?, grade5=?, grade6=?, grade7=?, grade8=?, grade9=?, grade10=?, grade11=?, grade12=?, grade13=?, grade14=?, grade15=?, status=? WHERE email=?",
            (new_email, first_name, last_name) + tuple(grades) + (status, email),
        )
        connection.commit()
        connection.close()
        messagebox.showinfo("Success", "Data edited successfully.")
    except sqlite3.Error as error:
        messagebox.showerror("Error", str(error))


def handle_db_exception(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except sqlite3.Error as error:
            messagebox.showerror("Error", str(error))
    return wrapper


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Student Database")
        self.geometry("400x200")

        # Przyciski
        self.display_button = tk.Button(self, text="Display Data", command=self.display_data)
        self.display_button.pack(pady=10)

        self.add_button = tk.Button(self, text="Add Data", command=self.add_data_window)
        self.add_button.pack(pady=10)

        self.delete_button = tk.Button(self, text="Delete Data", command=self.delete_data_window)
        self.delete_button.pack(pady=10)

        self.edit_button = tk.Button(self, text="Edit Data", command=self.edit_data_window)
        self.edit_button.pack(pady=10)

    @handle_db_exception
    def display_data(self):
        display_data()

    def add_data_window(self):
        window = tk.Toplevel(self)
        window.title("Add Data")

        # Pola tekstowe
        email_label = tk.Label(window, text="Email:")
        email_label.pack()
        email_entry = tk.Entry(window)
        email_entry.pack()

        first_name_label = tk.Label(window, text="First Name:")
        first_name_label.pack()
        first_name_entry = tk.Entry(window)
        first_name_entry.pack()

        last_name_label = tk.Label(window, text="Last Name:")
        last_name_label.pack()
        last_name_entry = tk.Entry(window)
        last_name_entry.pack()

        grades_label = tk.Label(window, text="Grades (comma-separated):")
        grades_label.pack()
        grades_entry = tk.Entry(window)
        grades_entry.pack()

        status_label = tk.Label(window, text="Status:")
        status_label.pack()
        status_entry = tk.Entry(window)
        status_entry.pack()

        add_button = tk.Button(
            window,
            text="Add",
            command=lambda: self.add_data(
                email_entry.get(),
                first_name_entry.get(),
                last_name_entry.get(),
                grades_entry.get().split(","),
                status_entry.get(),
            ),
        )
        add_button.pack(pady=10)

    def delete_data_window(self):
        window = tk.Toplevel(self)
        window.title("Delete Data")

        # Pole tekstowe
        email_label = tk.Label(window, text="Email:")
        email_label.pack()
        email_entry = tk.Entry(window)
        email_entry.pack()

        delete_button = tk.Button(window, text="Delete", command=lambda: self.delete_data(email_entry.get()))
        delete_button.pack(pady=10)

    def edit_data_window(self):
        window = tk.Toplevel(self)
        window.title("Edit Data")

        # Pola tekstowe
        email_label = tk.Label(window, text="Email:")
        email_label.pack()
        email_entry = tk.Entry(window)
        email_entry.pack()

        new_email_label = tk.Label(window, text="New Email:")
        new_email_label.pack()
        new_email_entry = tk.Entry(window)
        new_email_entry.pack()

        first_name_label = tk.Label(window, text="First Name:")
        first_name_label.pack()
        first_name_entry = tk.Entry(window)
        first_name_entry.pack()

        last_name_label = tk.Label(window, text="Last Name:")
        last_name_label.pack()
        last_name_entry = tk.Entry(window)
        last_name_entry.pack()

        grades_label = tk.Label(window, text="Grades (comma-separated):")
        grades_label.pack()

        grades_entry = tk.Entry(window)
        grades_entry.pack()
        status_label = tk.Label(window, text="Status:")
        status_label.pack()
        status_entry = tk.Entry(window)
        status_entry.pack()

        edit_button = tk.Button(
            window,
            text="Edit",
            command=lambda: self.edit_data(
                email_entry.get(),
                new_email_entry.get(),
                first_name_entry.get(),
                last_name_entry.get(),
                grades_entry.get().split(","),
                status_entry.get(),
            ),
        )
        edit_button.pack(pady=10)


if __name__ == "__main__":
    create_table()
    app = Application()
    app.mainloop()