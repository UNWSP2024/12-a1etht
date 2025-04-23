#Programmer: Alethea Lo
#Date: 4/22/25
#Title: MPG Calculator
import tkinter as tk
from tkinter import messagebox

def calculate_mpg():
    try:
        gallons = float(entry_gallons.get())
        miles = float(entry_miles.get())
        if gallons <= 0:
            raise ValueError("Gallons must be greater than 0.")
        mpg = miles / gallons
        label_result.config(text=f"Miles per Gallon (MPG): {mpg:.2f}")
    except ValueError as e:
        messagebox.showerror("Invalid Input", f"Please enter valid numbers.\n{e}")

root = tk.Tk()
root.title("Car Gas Mileage Calculator")
root.geometry("300x200")

#Creating Widgets
label_gallons = tk.Label(root, text="Gallons of gas:")
label_gallons.pack(pady=5)
entry_gallons = tk.Entry(root)
entry_gallons.pack(pady=5)

label_miles = tk.Label(root, text="Miles on full tank:")
label_miles.pack(pady=5)
entry_miles = tk.Entry(root)
entry_miles.pack(pady=5)

btn_calculate = tk.Button(root, text="Calculate MPG", command=calculate_mpg)
btn_calculate.pack(pady=10)

label_result = tk.Label(root, text="Miles per Gallon (MPG):")
label_result.pack(pady=5)

root.mainloop()