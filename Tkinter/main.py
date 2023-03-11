from tkinter import *

window=Tk()
window.title("My first GUI ")

window.minsize(height=500,width=500)

my_label =Label(text="Hello Everyone!", font=("Arial", 24, "bold"))
my_label.grid(column=0,row=0)

def Onclick():
    my_label["text"]="  Button got clicked"
    my_label.config(text="Button got clicked")

button=Button(text="click me",command=Onclick)
button.grid(column=1,row=1)

entry = Entry(width=10)
# entry.insert(END,string="Email")
print(entry.get())
entry.grid(column=3,row=2)

button1=Button(text="Daba na bsdk")
button1.grid(column=2,row=0)








window.mainloop()