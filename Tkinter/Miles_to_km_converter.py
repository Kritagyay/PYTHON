from tkinter import *

def mile_converter():
    miles=float(miles_input.get())
    km=round(miles*1.60934,2)
    km_result.config(text=f"{km}")

window=Tk()
window.title("Mile to Km Converter")
window.config(padx=20 ,pady=20)

miles_input=Entry(width=7)
miles_input.grid(column=1,row=0)

label=Label(text="Miles")
label.grid(column=2,row=0)

label1=Label(text="is equal to")
label1.grid(column=0,row=1)

km_result=Label(text="0")
km_result.grid(column=1,row=1)

km_label=Label(text="Km")
km_label.grid(column=2,row=1)

calculate_button=Button(text="Calculate",command=mile_converter)
calculate_button.grid(column= 1,row=2)




window.mainloop()