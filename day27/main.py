from tkinter import *

window = Tk()
window.title("Test GUI program")
window.minsize(width=500, height=300)

# Label
my_label = Label(text="I am a label", font=("Arial", 24))
my_label.pack()
#my_label.pack(expand=True)

def button_clicker():
    text = input.get()
    my_label["text"] = str(text)


button = Button(text="Click me", command=button_clicker)
button.pack()

input = Entry(width=20)
input.pack()







window.mainloop()
