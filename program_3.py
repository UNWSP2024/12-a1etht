#Programmer: Alethea Lo
#Date: 4/22/25
#Title: Long-Distance Calls
import tkinter as tk
from tkinter import messagebox

#Categories and charges
rates = {
    "Daytime (6:00 AM - 5:59 PM)": 0.02,
    "Evening (6:00 PM - 11:59 PM)": 0.12,
    "Off-Peak (12:00 AM - 5:59 AM)": 0.05
}

def calculate_charge():
    try:
        minutes = float(entry_minutes.get())
        if minutes <= 0:
            raise ValueError("Minutes must be greater than 0.")
        rate = rates[rate_var.get()]
        total = minutes * rate
        messagebox.showinfo("Call Charge", f"Total charge for the call: ${total:.2f}")
    except ValueError as e:
        messagebox.showerror("Invalid Input", f"Please enter a valid number of minutes.\n{e}")

#Main Window
root = tk.Tk()
root.title("Long-Distance Call Charge Calculator")
root.geometry("350x300")


tk.Label(root, text="Select Rate Category:", font=('Arial', 12, 'bold')).pack(pady=10)
rate_var = tk.StringVar(value=list(rates.keys())[0])  # Default selected

for rate_label in rates:
    tk.Radiobutton(root, text=f"{rate_label} - ${rates[rate_label]:.2f}/min",
                   variable=rate_var, value=rate_label).pack(anchor='w', padx=20)


tk.Label(root, text="Enter call duration (minutes):", font=('Arial', 11)).pack(pady=10)
entry_minutes = tk.Entry(root)
entry_minutes.pack(pady=5)

#Calculating
btn_calculate = tk.Button(root, text="Calculate Charge", command=calculate_charge)
btn_calculate.pack(pady=15)

root.mainloop()