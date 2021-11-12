from tkinter import *

window = Tk()
window.title("Test GUI program")
#window.minsize(width=500, height=300)
window.config(padx=10, pady=10)

def calculate():
    milets_entered = miles.get()
    out = round(float(milets_entered)*1.609344)
    km_label["text"] = str(out)

# Entry
miles = Entry()
miles.grid(column=1, row=0)

# Miles Label
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

# Equal Label
equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

# KM Label
km_label = Label(text="0")
km_label.grid(column=1, row=1)

# KM text Label
km_text_label = Label(text="Km")
km_text_label.grid(column=2, row=1)

# Calculate Button
calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)





window.mainloop()
