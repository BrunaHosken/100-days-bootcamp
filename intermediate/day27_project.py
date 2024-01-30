from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width = 50, height = 100)
window.config(padx = 20, pady = 20)

def button_clicked():
    text = miles.get()
    if(text):
        text_converted = float(text)*1.609
        km.config(text=f"{text_converted}")

label = Label(text="is equal to")
label.grid(column=0, row=1)
label.config(padx = 5, pady = 5)

miles= Entry(width=5)
miles.grid(column=1, row=0)
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)
miles_label.config(padx = 5, pady = 5)

km= Label(text="0")
km.grid(column=1, row=1)
km_label = Label(text="Km")
km_label.grid(column=2, row=1)
km_label.config(padx = 5, pady = 5)


button = Button(text = "Calculate", command=button_clicked)
button.grid(column=1, row=2)

window.mainloop()