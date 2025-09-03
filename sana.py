import tkinter as tk
from time import strftime

# Create window
root = tk.Tk()
root.title("Digital Clock")

# Set up label
label = tk.Label(root, font=("Arial", 20), background="black", foreground="red")
label.pack(anchor='center')

# Define time update function
def time():
    current_time = strftime('%I:%M:%S %p')  # 12-hour format with AM/PM
    label.config(text=current_time)
    label.after(1000, time)  # Update every 1 second (1000 ms)

# Initialize the clock
time()

# Run the application
root.mainloop()