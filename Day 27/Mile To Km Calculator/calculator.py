from tkinter import *

def miles_to_km():
    miles_value = float(miles_input.get())
    calc_km = miles_value * 1.609
    calculated_label.config(text=calc_km)


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=150, pady=200)

# Labels
miles_label = Label(text="Miles")
miles_label.config(padx=20, pady=20)
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to")
equal_label.config(padx=20, pady=20)
equal_label.grid(column=0, row=1)

kilometer_label = Label(text="Km")
kilometer_label.config(padx=20, pady=20)
kilometer_label.grid(column=2, row=1)

calculated_label = Label()
calculated_label.config(padx=20, pady=20)
calculated_label.grid(column=1, row=1)

# Button
calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

# Input
miles_input = Entry()
miles_input
miles_input.grid(column=1, row=0)



window.mainloop()