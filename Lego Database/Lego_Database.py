import sqlite3
import tkinter as tk
from tkinter import messagebox
from turtle import clear

class Createtable:
    #method to create new table
    def newtable(NewTableName):
        create = sqlite3.connect(NewTableName)
        create.close()

    def addtitles(TableName, Titles):
        create = sqlite3.connect(TableName)
        cursor = create.cursor()

        # SQL query to create a table if it doesn't exist
        cursor.execute(Titles)

        # Commit and close connection
        create.commit()
        create.close

    def createtitles(ColumnNames, ColumnTypes):
        newtitles = """CREATE TABLE IF NOT EXISTS users ("""
        for i in range(len(ColumnNames)):
            newtitles = newtitles + ColumnNames[i] + " " + ColumnTypes[i] + ","
        newtitles = newtitles[:-1]
        newtitles += """)"""
        return newtitles


#Create main database called "Lego Database"
databasename = "Lego Database"
Createtable.newtable(databasename)

columnnames = ["ID_Number","Name","Theme","Subtheme"]
columntypes = ["INTEGER UNIQUE NOT NULL", "TEXT NOT NULL", "TEXT NOT NULL", "TEXT NOT NULL"]

titles = Createtable.createtitles(columnnames,columntypes)
Createtable.addtitles(databasename, titles)
##


def toplabel():
    # Create a label at the top
    label = tk.Label(root, text="Welcome to the Lego Kit Manager!", font=("Arial", 14))
    label.grid(row=0, column=0, columnspan=2, pady=20, sticky="nsew")

def addbutton():
    # Create "Add Lego Kits" button
    add_button = tk.Button(root, text="Add Lego Kits", command=add_lego_kits, font=("Arial", 12), width=20)
    add_button.grid(row=2, column=0, padx=10)

def viewbutton():
    # Create "View Lego Kits" button (positioned on the right)
    view_button = tk.Button(root, text="View Lego Kits", command=view_lego_kits, font=("Arial", 12), width=20)
    view_button.grid(row=2, column=1, padx=10)

#Clear Screen
def clear_window():
    for widget in root.winfo_children():
        widget.destroy()

#Main Screen
def go_to_main_screen():
    # Hide the input box and buttons for the search
    clear_window()

    toplabel()

    # Show the main buttons
    addbutton()
    viewbutton()

# Function to handle "Add Lego Kits" button click
def add_lego_kits():
    clear_window()

    toplabel()

# Function to handle "View Lego Kits" button click
def view_lego_kits():
    messagebox.showinfo("View Lego Kits", "This is where you can view existing Lego kits!")

# Create main window
root = tk.Tk()
root.title("Lego Kit Manager")
root.geometry("420x200")  # Width x Height

go_to_main_screen()

# Run the main event loop
root.mainloop()