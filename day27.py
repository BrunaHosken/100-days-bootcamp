from tkinter import *

window = Tk()
window.title("Widget Examples")
window.minsize(width = 500, height = 300)
window.config(padx = 20, pady = 20)

#Label
label = Label(text="I'm a Label", font =("Arial", 24, "bold"))
label.config(text="New Text")
label.pack()
# label.grid(column=0, row=0)
# label.place(x=0, y=0)


#Button
def button_clicked():
    text = entry.get()
    label.config(text=text)

button = Button(text = "Click Me", command=button_clicked)
button.pack()

#Entry
entry= Entry(width=30)
entry.insert(END, string="Some text to begin with.")
entry.pack()

#Text
text = Text(height=5, width=30)
text.focus()
text.insert(END, "Example of multi-line text entry.")
print(text.get("1.0", END))
text.pack()



#Spinbox
def spinbox_used():
    print(spinbox.get())

spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#Scale
def scale_used(value):
    print(value)

scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Checkbutton
def checkbutton_used():
    print(checked_state.get())

checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable = checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#Radiobutton
def radio_used():
    print(radio_state.get())

radio_state = IntVar()
radiobutton1 = Radiobutton(text = "Option1", value = 1, variable = radio_state, command=radio_used)
radiobutton2 = Radiobutton(text = "Option2", value = 2, variable = radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

#Listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple","Pear","Orange","Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)

listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

window.mainloop()