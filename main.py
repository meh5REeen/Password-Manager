from tkinter import * #classes
from tkinter import messagebox #module
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def fill_password():
    """An autfill of password when App start"""
    pa = generate_password()
    pass_entry.delete(0,END)
    pass_entry.insert(0,pa)

def generate_password():
    """Random password generator"""
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []


    password_let = [random.choice(letters) for l in range(nr_letters)]
    password_num = [random.choice(numbers) for n in range(nr_numbers)]
    password_sym = [random.choice(symbols) for s in range(nr_symbols)]

    password_list =  password_sym + password_num + password_let
    random.shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    return password

# ---------------------------- SAVE PASSWORD ------------------------------- #
def added():
    """Saves all the details in the file"""
    web = web_entry.get()
    email = email_entry.get()
    passw = pass_entry.get()
    if len(web) == 0 or len(email) == 0 or len(passw) == 0:
        messagebox.showinfo(title="Empty Fields",message="Please Dont Leave any Field Empty.")
    else:
        ok =messagebox.askokcancel(title=web,message=f"These are the details entered :\n Email : {email}"
                                                 f"\nPassword: {passw} \nIs it ok to save?")
        if ok:
            with open("file.txt", "a") as file:
                file.write(f"{web} | {email} | {passw}\n")
            web_entry.delete(0, END)
            pass_entry.delete(0, END)





# ---------------------------- UI SETUP ------------------------------- #

# window
window = Tk()
window.title("My Password Manager")
window.config(padx=50,pady=50)

#canvas at the mid
canvas = Canvas(height=200,width=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image = img)# image to the canvas
canvas.grid(column=1,row = 0)

#website label at c0 r1
website = Label(text ="Website:")
website.grid(column=0,row=1)

#website entry field
web_entry = Entry(width = 45)
web_entry.grid(column=1,row=1,columnspan=2,sticky="W")
web_entry.focus()

# email/ username at c0 r2
email = Label(text="Email/Username:")
email.grid(column=0,row=2)

# email entry field
email_entry = Entry(width = 45)
email_entry.insert(0,"mehreens123@gmail.com")
email_entry.grid(column=1,row=2,columnspan=2,sticky="W")

# Password at c0  r3
passwords = Label(text="Password: ")
passwords.grid(column=0, row=3)

#password entry field
pass_entry = Entry(width=35)
pass_entry.insert(0, generate_password())
pass_entry.grid(column=1,row=3,sticky="W")

# generate password button
generate = Button(text = "Generate",command=fill_password)
generate.grid(column = 2,row=3,sticky="W")

#add button
add = Button(text="Add",width=38,command=added)
add.grid(column=1,row=4,columnspan=2,sticky="W")

# def on_enter():
#     add.config(bg="blue",fg="white")
# def on_leave():
#     add.config(bg="SystemButtonFace",fg = 'black')
# add('<Enter>',on_enter)
# add('<leave>',on_leave)

window.mainloop()