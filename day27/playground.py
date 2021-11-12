from tkinter import *

window = Tk()
window.title("Test GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I am a label", font=("Arial", 24))
my_label.grid(column=0, row=0)

# New Button
new_button = Button(text="Click me")
new_button.grid(column=2, row=0)

# my_label.pack(expand=True)

# Button

def button_clicker():
    text = input.get()
    my_label["text"] = str(text)


button = Button(text="Click me", command=button_clicker)
button.grid(column=1, row=1)

# Entry
input = Entry()
input.grid(column=3, row=2)




window.mainloop()
