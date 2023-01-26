from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.config(padx=20,pady=20)

# create the buttons and texts
miles = Label(text="Miles")
km = Label(text="Km")
is_equal_to = Label(text="is_equal_to:")
result = Label(text=0)
input = Entry(width=7)

# sets the locations
km.grid(column=2,row=1)
is_equal_to.grid(column=0,row=1)
result.grid(column=1,row=1)
input.grid(column=1,row=0)
miles.grid(column=2,row=0)

def button_press():
    calulation = round(int(input.get()) * 1.60934, 2)
    # dispays in the middle the result
    result.config(text=calulation)

button = Button(text="Calculate", command=button_press)
button.grid(column=1,row=2)

window.mainloop()