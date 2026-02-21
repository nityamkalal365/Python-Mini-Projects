from tkinter import messagebox
import random
import pyperclip
import json
FONT_NAME="Courier"

def search():
    try:
        with open("data.json","r") as d:
            data = json.load(d)
    except FileNotFoundError:
        messagebox.showinfo(message="The file not found.No data stored yet!!")
    else:
        to_search=website_entry.get()
        if to_search in data:
            messagebox.showinfo(title=to_search,message=f"Email: {data[to_search]['Email']}\nPassword: {data[to_search]['Password']}")
        else:
            messagebox.showinfo(title="NOT FOUND",message="There is no such data stored")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def pass_generator():
    password_entry.delete(0, last=END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)



    password_list = [random.choice(letters) for char in range(nr_letters)]


    password_list +=[random.choice(symbols) for char in range(nr_symbols)]


    password_list += [random.choice(numbers)for char in range(nr_numbers)]


    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website=website_entry.get()
    password=password_entry.get()
    username=username_entry.get()
    new_data={website:{
        "Email":f"{username}","Password":f"{password}"
    }}
    if len(website)==0 or len(password)==0 or len(username)==0:
        messagebox.showinfo(title="Error",message="Please fill all the entry first")
    else:
        try:
            with open("data.json", "r") as data_file:
        # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
            # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
             website_entry.delete(0, END)
             password_entry.delete(0, END)
             username_entry.delete(0, last=END)
# ---------------------------- UI SETUP ------------------------------- #

from tkinter import *

window=Tk()
window.title("My Password Manager")
window.config(padx=50,pady=50)
canvas=Canvas(width=200,height=200)
logo=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo)
canvas.grid(row=0,column=1)
website_label=Label(text="Website:",)
website_label.grid(row=1,column=0)
website_entry=Entry(width=50)
website_entry.focus()
website_entry.grid(row=1,column=1,columnspan=3)
username_label=Label(text="Email/Username:")
username_label.grid(row=2,column=0)
username_entry=Entry(width=50)
username_entry.grid(row=2,column=1,columnspan=3)
password_label=Label(text="Password:")
password_label.grid(row=3,column=0)
password_entry=Entry(width=50)
password_entry.grid(row=3,column=1,columnspan=3)
password_button=Button(text="Generate Password",width=14,command=pass_generator)
password_button.grid(row=3,column=4)
add_button=Button(text="Add",width=30,command=save)
add_button.grid(row=4,column=1,columnspan=2)
search_button=Button(width=14,text="Search",command=search)
search_button.grid(row=1,column=4)



window.mainloop()
