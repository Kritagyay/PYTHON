import random
from tkinter import *
from tkinter import messagebox
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generate():
    letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
             'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
             'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
             'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter=[random.choice(letters) for _ in range(random.randint(8,10))]
    password_number=[random.choice(numbers) for _ in range(random.randint(2,4))]
    password_symbol=[random.choice(symbols) for _ in range(random.randint(2,4))]
    passcode=password_number+password_symbol+password_letter
    random.shuffle(passcode)
    final_password="".join(passcode)
    password_entry.insert(0,final_password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()
    new_data={
        website:
            {
                "email":email,
                "password":password,
            }
              }

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Warning", message="Please fill the entry you have left.")

    else:
        try:
            with open("data.json", "r") as data_file:
                data=json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data,data_file,indent=4)

        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)


        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- find password ------------------------------- #
def find_password():
    website=website_entry.get()
    try:
        with open ("data.json") as data_file:
            data=json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="WARNING",message="The website you are looking for is not present in our database.")
    else:
        if website in data:
            email=data[website]["email"]
            password=data[website]["password"]
            messagebox.showinfo(title=f"{website}",message=f"Email: {email} \n Password: {password}\n")
        else:
            messagebox.showinfo(title="Warniing",message="No such website is present. ")
# ---------------------------- UI SETUP ------------------------------- #


window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas=Canvas(width=200,height=200,highlightthickness=1)
lock_png=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=lock_png)
canvas.grid(column=1,row=0)

website_label=Label(text="Website:")
website_label.grid(column=0,row=1)

email_label=Label(text="Email:")
email_label.grid(column=0,row=2)

password_label=Label(text="Password:")
password_label.grid(column=0,row=3)

#Entry
website_entry=Entry(width=17)
website_entry.grid(column=1,row=1,sticky="EW")
website_entry.focus()
email_entry=Entry(width=35)
email_entry.grid(column=1,row=2,columnspan=3,sticky="EW")
email_entry.insert(0,"venom@gmail.com")
password_entry=Entry(width=17)
password_entry.grid(column=1,row=3,sticky="EW")

#Buttons
generate_paas=Button(text="GeneratePassword", command=password_generate)
generate_paas.grid(column=2,row=3,sticky="EW")
search_button=Button(text="Search",width=10,command=find_password)
search_button.grid(column=2,row=1,sticky="EW")
add=Button(text="ADD",width=30,command=save)
add.grid(column=1,row=4,columnspan=2,sticky="EW")



window.mainloop()
