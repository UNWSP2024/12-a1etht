#Programmer: Alethea Lo
#Date: 4/22/25
#Title: Joe's Automotive
import tkinter as tk
from tkinter import messagebox

#Dictonary of services and cost
services = {
    "Oil Change": 30.00,
    "Lube Job": 20.00,
    "Radiator Flush": 40.00,
    "Transmission Fluid": 100.00,
    "Inspection": 35.00,
    "Muffler Replacement": 200.00,
    "Tire Rotation": 20.00
}

def calculate_total():
    total = 0.0
    for service, var in service_vars.items():
        if var.get():
            total += services[service]
    label_total.config(text=f"Total Charges: ${total:.2f}")

root = tk.Tk()
root.title("Joe's Automotive Services")
root.geometry("300x350")

service_vars = {}

tk.Label(root, text="Select Services:", font=('Arial', 12, 'bold')).pack(pady=5)
for service in services:
    var = tk.IntVar()
    chk = tk.Checkbutton(root, text=f"{service} - ${services[service]:.2f}", variable=var)
    chk.pack(anchor='w', padx=20)
    service_vars[service] = var

btn_total = tk.Button(root, text="Calculate Total", command=calculate_total)
btn_total.pack(pady=10)

#Display total
label_total = tk.Label(root, text="Total Charges: $0.00", font=('Arial', 12))
label_total.pack(pady=5)


root.mainloop()
