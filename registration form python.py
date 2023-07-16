import tkinter as tk
from tkinter import StringVar, IntVar

root = tk.Tk()
root.title("Registration")
root.geometry("600x470")
root.resizable(False, False)

def register():
    print("registered")

tk.Label(root, text="Python Registration Form", font="Arial 25").pack(pady=50)

tk.Label(root, text="Name", font=('', 23)).place(x=100, y=150)
tk.Label(root, text="Phone", font=('', 23)).place(x=100, y=200)
tk.Label(root, text="Gender", font=('', 23)).place(x=100, y=250)
tk.Label(root, text="Email", font=('', 23)).place(x=100, y=300)

# Entry
nameValue = StringVar()
phoneValue = StringVar()
genderValue = StringVar()
emailValue = StringVar()

nameEntry = tk.Entry(root, textvariable=nameValue, width=30, bd=2, font=('', 20))
phoneEntry = tk.Entry(root, textvariable=phoneValue, width=30, bd=2, font=('', 20))
genderEntry = tk.Entry(root, textvariable=genderValue, width=30, bd=2, font=('', 20))
emailEntry = tk.Entry(root, textvariable=emailValue, width=30, bd=2, font=('', 20))

nameEntry.place(x=200, y=150)
phoneEntry.place(x=200, y=200)
genderEntry.place(x=200, y=250)
emailEntry.place(x=200, y=300)

# Check button
checkValue = IntVar()
checkButton = tk.Checkbutton(root, text="Remember me?", variable=checkValue)
checkButton.place(x=200, y=340)

tk.Button(root, text="Register", font=('', 20), width=11, height=2, command=register).place(x=250, y=380)

root.mainloop()
